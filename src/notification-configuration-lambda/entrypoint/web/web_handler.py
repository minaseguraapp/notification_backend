import abc
import json
import logging
from typing import Any, Dict, Optional

import context
import pydantic
from domain.model import aggregate
from domain.service import notification_config_service

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

        notification_configuration: Optional[aggregate.NotificationConfiguration] = (
            self.config_service.get_notification_configuration(mine_id=mine_id)
        )

        if not notification_configuration:
            return {
                "statusCode": 404,
            }

        return {
            "statusCode": 200,
            "body": notification_configuration.model_dump_json(by_alias=True),
        }


class PostNotificationConfiguration(WebHandler):

    def __init__(
        self,
    ) -> None:
        self.config_service = (
            context.ContextManager.get_notification_configuration_service()
        )
        super().__init__()

    def handle(self, event: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("POST Notification configuration handler started")
        body_str: Optional[str] = event.get("body")

        if body_str is None:
            logger.error("No body found in the request")
            return {"statusCode": 400}

        notification_configuration: Optional[aggregate.NotificationConfiguration] = None
        body: Dict[str, Any] = json.loads(body_str)

        try:
            notification_configuration = (
                aggregate.NotificationConfiguration.model_validate(body)
            )
        except pydantic.ValidationError as e:
            logger.error("Error parsing the Notification Config to create[%s]", e)

        if notification_configuration is None:
            return {
                "statusCode": 400,
            }

        success = self.config_service.create_notification_configuration(
            notification_configuration=notification_configuration
        )

        if success != True:
            return {
                "statusCode": 502,
            }

        return {
            "statusCode": 201,
        }
