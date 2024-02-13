import abc
import json
from typing import Any, Dict


class WebHandler(abc.ABC):

    @abc.abstractmethod
    def handle(self, event: Dict[str, Any]) -> Dict[str, Any]: ...


class GetNotificationConfiguration(WebHandler):
    def handle(self, event: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "GET Notification config",
                }
            ),
        }


class PostNotificationConfiguration(WebHandler):
    def handle(self, event: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "POST Notification config",
                }
            ),
        }
