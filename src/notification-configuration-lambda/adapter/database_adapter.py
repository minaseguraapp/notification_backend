from typing import Any

from domain.model import aggregate


class DynamoDBAdapter:

    def __init__(self, boto3_client_dynamodb: Any):
        self.dynamodb_client = boto3_client_dynamodb

    def query_table(self, table_name: str, partition_key: str, sort_key: str):
        return self.dynamodb_client.scan(TableName=table_name)

    def put_item(self, table_name: str, item: dict):
        self.dynamodb_client.put_item(TableName=table_name, Item=item)
