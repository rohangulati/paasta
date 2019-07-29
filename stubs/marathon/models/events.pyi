# Stubs for marathon.models.events (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from marathon.models.base import MarathonObject

class MarathonEvent(MarathonObject):
    KNOWN_ATTRIBUTES = ...  # type: Any
    attribute_name_to_marathon_object = ...  # type: Any
    event_type = ...  # type: Any
    timestamp = ...  # type: Any
    def __init__(self, event_type, timestamp, **kwargs) -> None: ...

class MarathonApiPostEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonStatusUpdateEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonFrameworkMessageEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonSubscribeEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonUnsubscribeEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonAddHealthCheckEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonRemoveHealthCheckEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonFailedHealthCheckEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonHealthStatusChangedEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonGroupChangeSuccess(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonGroupChangeFailed(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonDeploymentSuccess(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonDeploymentFailed(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonDeploymentInfo(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonDeploymentStepSuccess(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonDeploymentStepFailure(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonEventStreamAttached(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonEventStreamDetached(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonUnhealthyTaskKillEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonAppTerminatedEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonInstanceChangedEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonUnknownInstanceTerminated(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonInstanceHealthChangedEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonPodCreatedEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonPodUpdatedEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonPodDeletedEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class MarathonUnhealthyInstanceKillEvent(MarathonEvent):
    KNOWN_ATTRIBUTES = ...  # type: Any

class EventFactory:
    def __init__(self) -> None: ...
    event_to_class = ...  # type: Any
    class_to_event = ...  # type: Any
    def process(self, event): ...
