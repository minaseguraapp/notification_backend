import abc
import json
import logging
from typing import Any, Dict, List, Optional

import context
from domain.model import aggregate
from domain.service import notification_config_service
from entrypoint import commons

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()


class WebHandler(abc.ABC):

    @abc.abstractmethod
    def handle(self, event: Dict[str, Any]) -> Dict[str, Any]: ...


class GetNotificationConfiguration(WebHandler):

    config_service: notification_config_service.NotificationConfigurationService

    def __init__(
        self,
    ) -> None:
        self.config_service = (
            context.ContextManager.get_notification_configuration_service()
        )
        super().__init__()

    def handle(self, event: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("GET Notification configuration handler started")

        query_params: Dict[str, str] = event.get("queryStringParameters") or {}
        mine_id: Optional[str] = query_params.get("mine")

        if not mine_id:
            return {
                "statusCode": 400,
            }

        notification_configurations: List[aggregate.NotificationConfiguration] = (
            self.config_service.get_notification_configuration(mine_id=mine_id)
        )

        response: commons.GetNotificationConfigurationResponse = (
            commons.GetNotificationConfigurationResponse(
                configurations=notification_configurations
            )
        )

        return {
            "statusCode": 200,
            "body": response.model_dump_json(by_alias=True),
        }


class PostNotificationConfiguration(WebHandler):
    def handle(self, event: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("POST Notification configuration handler started")

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "POST Notification config",
                }
            ),
        }
