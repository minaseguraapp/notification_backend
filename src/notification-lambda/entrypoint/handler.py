import logging
from typing import Any, Dict, Optional, Type

from entrypoint.event import event_handler as handler

logging.getLogger().setLevel(logging.INFO)

logger = logging.getLogger()


class Router:
    router: Dict[str, Type[handler.EventHandler]] = {
        "SendNotification": handler.SendNotificationEventHandler,
    }

    @classmethod
    def route(cls, event: Dict[str, Any]) -> None:

        event_name = "SendNotification"

        cls_handler: Optional[Type[handler.EventHandler]] = cls.router.get(event_name)

        if not cls_handler:
            logger.error(
                "There is not found a valid configuration for the specified route [%s]",
                event_name,
            )
            return

        cls_handler().handle(event)


def lambda_handler(event: Dict[str, Any], context: Any) -> None:
    Router.route(event=event)
