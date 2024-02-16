import logging
from typing import Any, Dict, Optional

from adapter import commons

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()


class DynamoDBAdapter:

    def __init__(self, boto3_client_dynamodb: Any):
        self.dynamodb_client = boto3_client_dynamodb

    def get_item_by_partition_key(
        self, table_name: str, partition_key_name: str, partition_key_value: str
    ) -> Optional[Dict[str, Any]]:

        deserialized_item = None

        response = self.dynamodb_client.get_item(
            TableName=table_name, Key={partition_key_name: {"S": partition_key_value}}
        )

        item = response.get("Item")

        if item:
            deserialized_item = commons.deserialize_dynamodb_item(item)

        return deserialized_item

    def put_item(self, table_name: str, item: Dict[str, Any]) -> None:
        logger.info("The item [%s] will be created on table [%s]", item, table_name)
        serialized_item = commons.serialize_dynamodb_item(item)

        self.dynamodb_client.put_item(TableName=table_name, Item=serialized_item)
