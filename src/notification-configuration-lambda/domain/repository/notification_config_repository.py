import abc
import logging
from typing import List

from domain.model import aggregate

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()


class NotificationConfigurationRepository(abc.ABC):

    @abc.abstractmethod
    def get_notification_configuration(
        self, mine_id: str
    ) -> List[aggregate.NotificationConfiguration]: ...

    @abc.abstractmethod
    def create_notification_configuration(
        self, notification_configuration: aggregate.NotificationConfiguration
    ) -> bool: ...


class NotificationConfigurationDynamoDBRepository(NotificationConfigurationRepository):

    def __init__(self) -> None:
        super().__init__()

    def get_notification_configuration(
        self, mine_id: str
    ) -> List[aggregate.NotificationConfiguration]:
        logger.info(
            "Get notification configuration Repository started with [%s]", mine_id
        )
        return []

    def create_notification_configuration(
        self, notification_configuration: aggregate.NotificationConfiguration
    ) -> bool:
        logger.info(
            "Create notification configuration Repository started with [%s]",
            notification_configuration.model_dump_json(),
        )
        return True
