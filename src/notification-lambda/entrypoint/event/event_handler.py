import abc
import json
import logging
from typing import Any, Dict

logging.getLogger().setLevel(logging.INFO)

logger = logging.getLogger()


class EventHandler(abc.ABC):

    @abc.abstractmethod
    def handle(self, event: Dict[str, Any]) -> None:
        """Process an specific received event

        Args:
            event (Dict[str, Any]): event received
        """


class SendNotificationEventHandler(EventHandler):
    def handle(self, event: Dict[str, Any]) -> None:
        logger.info("Send Notification Event processed [%s]", event)
