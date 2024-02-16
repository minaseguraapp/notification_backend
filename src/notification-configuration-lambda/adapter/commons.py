from typing import Any, Dict

from boto3.dynamodb.types import TypeDeserializer, TypeSerializer


def deserialize_dynamodb_item(item: Dict[str, Any]) -> Dict[str, Any]:
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in item.items()}


def serialize_dynamodb_item(item: Dict[str, Any]) -> Dict[str, Any]:
    serializer = TypeSerializer()
    return {k: serializer.serialize(v) for k, v in item.items()}
