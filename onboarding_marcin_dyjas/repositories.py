from kink import inject
from mypy_boto3_dynamodb.type_defs import ScanOutputTableTypeDef
from mypy_boto3_dynamodb.service_resource import Table


class TimestampRepository:
    @inject
    def __init__(self, timestamp_table: Table):
        self.timestamp_table = timestamp_table

    def add_timestamp(self, uuid: str, timestamp: str) -> None:
        self.timestamp_table.put_item(Item={"id": uuid, "timestamp": timestamp})
