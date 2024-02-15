import pydantic


class NotificationConfigurationInfo(pydantic.BaseModel):
    email: str = pydantic.Field(alias="email")
    cellphone: str = pydantic.Field(alias="cellphone")


class NotificationConfiguration(pydantic.BaseModel):
    mine_id: str = pydantic.Field(alias="mineId")
    timestamp: int = pydantic.Field(alias="timestamp")
    notification_info: NotificationConfigurationInfo = pydantic.Field(
        alias="notificationInfo"
    )
