import abc
import logging
from typing import Optional

from domain.model import aggregate
from domain.repository import notification_config_repository

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()


class NotificationConfigurationService(abc.ABC):

    @abc.abstractmethod
    def get_notification_configuration(
        self, mine_id: str
    ) -> Optional[aggregate.NotificationConfiguration]: ...

    @abc.abstractmethod
    def create_notification_configuration(
        self, notification_configuration: aggregate.NotificationConfiguration
    ) -> bool: ...


class NotificationConfigurationServiceImpl(NotificationConfigurationService):

    configuration_repository: (
        notification_config_repository.NotificationConfigurationRepository
    )

    def __init__(
        self,
        configuration_repository: notification_config_repository.NotificationConfigurationRepository,
    ) -> None:
        self.configuration_repository = configuration_repository
        super().__init__()

    def get_notification_configuration(
        self, mine_id: str
    ) -> Optional[aggregate.NotificationConfiguration]:
        logger.info("Get notification configuration service started with [%s]", mine_id)
        return self.configuration_repository.get_notification_configuration(
            mine_id=mine_id
        )

    def create_notification_configuration(
        self, notification_configuration: aggregate.NotificationConfiguration
    ) -> bool:
        logger.info(
            "Create notification configuration Service started with [%s]",
            notification_configuration.model_dump_json(),
        )
        return self.configuration_repository.create_notification_configuration(
            notification_configuration=notification_configuration
        )
