from typing import Optional

import boto3
from adapter import database_adapter
from domain.repository import notification_config_repository
from domain.service import notification_config_service


class ContextManager:

    notification_service: Optional[
        notification_config_service.NotificationConfigurationService
    ] = None
    notification_repository: Optional[
        notification_config_repository.NotificationConfigurationRepository
    ] = None
    db_adapter: Optional[database_adapter.DynamoDBAdapter] = None

    @classmethod
    def get_notification_configuration_service(
        cls,
    ) -> notification_config_service.NotificationConfigurationService:
        if not cls.notification_service:
            cls.notification_service = (
                notification_config_service.NotificationConfigurationServiceImpl(
                    cls.get_notification_configuration_repository()
                )
            )
        return cls.notification_service

    @classmethod
    def get_notification_configuration_repository(
        cls,
    ) -> notification_config_repository.NotificationConfigurationRepository:
        if not cls.notification_repository:
            cls.notification_repository = (
                notification_config_repository.NotificationConfigurationDynamoDBRepository()
            )
        return cls.notification_repository

    @classmethod
    def get_database_adapter(
        cls,
    ) -> database_adapter.DynamoDBAdapter:
        boto_client_dynamodb = boto3.client("dynamodb")

        if not cls.db_adapter:
            cls.db_adapter = database_adapter.DynamoDBAdapter(
                boto3_client_dynamodb=boto_client_dynamodb
            )
        return cls.db_adapter
