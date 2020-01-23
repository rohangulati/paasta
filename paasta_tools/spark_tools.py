import logging
import os
import socket
import sys
from typing import Mapping
from typing import Optional
from typing import Tuple

import boto3
from botocore.session import Session
from ruamel.yaml import YAML
from typing_extensions import TypedDict

from paasta_tools.clusterman import get_clusterman_metrics
from paasta_tools.utils import paasta_print
from paasta_tools.utils import PaastaColors

AWS_CREDENTIALS_DIR = "/etc/boto_cfg/"
DEFAULT_SPARK_MESOS_SECRET_FILE = "/nail/etc/paasta_spark_secret"
DEFAULT_SPARK_RUN_CONFIG = "/nail/srv/configs/spark.yaml"
DEFAULT_SPARK_SERVICE = "spark"
clusterman_metrics, CLUSTERMAN_YAML_FILE_PATH = get_clusterman_metrics()
log = logging.getLogger(__name__)


class DockerVolumeDict(TypedDict):
    hostPath: str
    containerPath: str
    mode: str


def _load_aws_credentials_from_yaml(yaml_file_path) -> Tuple[str, str]:
    with open(yaml_file_path, "r") as yaml_file:
        try:
            credentials_yaml = YAML().load(yaml_file.read())
        except Exception as e:
            paasta_print(
                PaastaColors.red(
                    "Encountered %s when trying to parse AWS credentials yaml %s. "
                    "Suppressing further output to avoid leaking credentials."
                    % (type(e), yaml_file_path)
                )
            )
            sys.exit(1)

        return (
            credentials_yaml["aws_access_key_id"],
            credentials_yaml["aws_secret_access_key"],
        )


def get_aws_credentials(
    service: str = DEFAULT_SPARK_SERVICE,
    no_aws_credentials: bool = False,
    aws_credentials_yaml: Optional[str] = None,
    profile_name: Optional[str] = None,
) -> Tuple[Optional[str], Optional[str]]:
    if no_aws_credentials:
        return None, None
    elif aws_credentials_yaml:
        return _load_aws_credentials_from_yaml(aws_credentials_yaml)
    elif service != DEFAULT_SPARK_SERVICE:
        service_credentials_path = os.path.join(AWS_CREDENTIALS_DIR, f"{service}.yaml")
        if os.path.exists(service_credentials_path):
            return _load_aws_credentials_from_yaml(service_credentials_path)
        else:
            paasta_print(
                PaastaColors.yellow(
                    "Did not find service AWS credentials at %s.  Falling back to "
                    "user credentials." % (service_credentials_path)
                )
            )

    creds = Session(profile=profile_name).get_credentials()
    return creds.access_key, creds.secret_key


def get_default_event_log_dir(**kwargs) -> str:
    if "access_key" not in kwargs or "secret_key" not in kwargs:
        access_key, secret_key = get_aws_credentials(**kwargs)
    else:
        access_key, secret_key = kwargs["access_key"], kwargs["secret_key"]
    if access_key is None:
        log.warning(
            "Since no AWS credentials were provided, spark event logging "
            "will be disabled"
        )
        return None

    with open(DEFAULT_SPARK_RUN_CONFIG) as fp:
        spark_run_conf = YAML().load(fp.read())
    try:
        account_id = (
            boto3.client(
                "sts", aws_access_key_id=access_key, aws_secret_access_key=secret_key
            )
            .get_caller_identity()
            .get("Account")
        )
    except Exception as e:
        log.warning("Failed to identify account ID, error: {}".format(str(e)))
        return None

    for conf in spark_run_conf["environments"].values():
        if account_id == conf["account_id"]:
            default_event_log_dir = conf["default_event_log_dir"]
            paasta_print(f"default event logging at: {default_event_log_dir}")
            return default_event_log_dir
    return None


def load_mesos_secret_for_spark():
    try:
        with open(DEFAULT_SPARK_MESOS_SECRET_FILE, "r") as f:
            return f.read()
    except IOError as e:
        paasta_print(
            "Cannot load mesos secret from %s" % DEFAULT_SPARK_MESOS_SECRET_FILE,
            file=sys.stderr,
        )
        raise e


def _calculate_memory_per_executor(spark_memory_string, memory_overhead):
    # expected to be in format "dg" where d is an integer
    base_memory_per_executor = 1024 * int(spark_memory_string[:-1])

    # by default, spark adds an overhead of 10% of the executor memory, with
    # a minimum of 384mb
    if memory_overhead is None:
        memory_overhead = max(384, int(0.1 * base_memory_per_executor))
    else:
        memory_overhead = int(memory_overhead)

    return base_memory_per_executor + memory_overhead


def get_spark_resource_requirements(
    spark_config_dict: Mapping[str, str], webui_url: str,
) -> Mapping[str, Tuple[str, int]]:
    if not clusterman_metrics:
        return {}
    num_executors = int(spark_config_dict["spark.cores.max"]) / int(
        spark_config_dict["spark.executor.cores"]
    )
    memory_per_executor = _calculate_memory_per_executor(
        spark_config_dict["spark.executor.memory"],
        spark_config_dict.get("spark.mesos.executor.memoryOverhead"),
    )

    desired_resources = {
        "cpus": int(spark_config_dict["spark.cores.max"]),
        "mem": memory_per_executor * num_executors,
        # rough guess since spark does not collect this information
        "disk": memory_per_executor * num_executors,
    }
    dimensions = {
        "framework_name": spark_config_dict["spark.app.name"],
        "webui_url": webui_url,
    }
    qualified_resources = {}
    for resource, quantity in desired_resources.items():
        qualified_resources[resource] = (
            clusterman_metrics.generate_key_with_dimensions(
                f"requested_{resource}", dimensions
            ),
            desired_resources[resource],
        )

    return qualified_resources


def get_webui_url(port: int) -> str:
    return f"http://{socket.getfqdn()}:{port}"
