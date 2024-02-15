from typing import List

import pydantic
from domain.model import aggregate


class GetNotificationConfigurationResponse(pydantic.BaseModel, frozen=True):
    configurations: List[aggregate.NotificationConfiguration] = pydantic.Field(
        default_factory=list
    )
