import logging
from typing import Any, Callable, Dict, Optional, Type

import pydantic
from entrypoint.web import web_handler as handler

logging.getLogger().setLevel(logging.INFO)

logger = logging.getLogger()


class Route(pydantic.BaseModel, frozen=True):
    http_method: str
    path: str


class Router:
    router: Dict[Route, Type[handler.WebHandler]] = {
        Route(
            http_method="GET", path="/notification/configuration"
        ): handler.GetNotificationConfiguration,
        Route(
            http_method="POST", path="/notification/configuration"
        ): handler.PostNotificationConfiguration,
    }

    @classmethod
    def route(cls, event: Dict[str, Any]) -> Dict[str, Any]:

        route = Route(
            http_method=event.get("httpMethod", ""), path=event.get("path", "")
        )

        cls_handler: Optional[Type[handler.WebHandler]] = cls.router.get(route)

        if not cls_handler:
            logger.error(
                "There is not found a valid configuration for the specified route [%s]",
                route.model_dump_json(),
            )
            return {
                "statusCode": 400,
            }

        return cls_handler().handle(event)


def lambda_handler(event: Dict[str, Any], context: Any) -> Any:
    return Router.route(event=event)
