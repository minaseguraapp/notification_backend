import abc
from typing import List

from domain.model import aggregate


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
        return []

    def create_notification_configuration(
        self, notification_configuration: aggregate.NotificationConfiguration
    ) -> bool:
        return True
