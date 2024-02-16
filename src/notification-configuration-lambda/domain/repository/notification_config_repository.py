import abc
import logging
from typing import Optional

from adapter import database_adapter
from domain.model import aggregate

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()


class NotificationConfigurationRepository(abc.ABC):

    @abc.abstractmethod
    def get_notification_configuration(
        self, mine_id: str
    ) -> Optional[aggregate.NotificationConfiguration]: ...

    @abc.abstractmethod
    def create_notification_configuration(
        self, notification_configuration: aggregate.NotificationConfiguration
    ) -> bool: ...


class NotificationConfigurationDynamoDBRepository(NotificationConfigurationRepository):

    def __init__(self, db_adapter: database_adapter.DynamoDBAdapter) -> None:
        self.dynamodb_adapter = db_adapter
        super().__init__()

    def get_notification_configuration(
        self, mine_id: str
    ) -> Optional[aggregate.NotificationConfiguration]:
        logger.info(
            "Get notification configuration Repository started with [%s]", mine_id
        )
        item_dict = self.dynamodb_adapter.get_item_by_partition_key(
            table_name="NotificationConfigurationTable",
            partition_key_name="mineId",
            partition_key_value=mine_id,
        )

        if not item_dict:
            logger.info("No notification configuration found for mineId: %s", mine_id)
            return None

        notification_configuration = aggregate.NotificationConfiguration(**item_dict)

        return notification_configuration

    def create_notification_configuration(
        self, notification_configuration: aggregate.NotificationConfiguration
    ) -> bool:
        logger.info(
            "Create notification configuration Repository started with [%s]",
            notification_configuration.model_dump_json(),
        )

        self.dynamodb_adapter.put_item(
            table_name="NotificationConfigurationTable",
            item=notification_configuration.model_dump(by_alias=True),
        )

        return True
