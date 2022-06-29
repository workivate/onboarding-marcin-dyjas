from datetime import datetime

from kink import inject
from mypy_boto3_dynamodb.service_resource import Table


class TimestampRepository:
    @inject
    def __init__(self, timestamp_table: Table):
        self.timestamp_table = timestamp_table

    def add_timestamp(self, uuid: str, timestamp: str) -> None:
        self.timestamp_table.put_item(Item={"id": uuid, "timestamp": timestamp})

    def get_filtered_timestamps(self, start_date=None, end_date=None) -> list:
        results = self.timestamp_table.scan()
        if not start_date or not end_date:
            return results["Items"]
        filtered_results = []
        for result in results["Items"]:
            if datetime.strptime(result["timestamp"], "%Y-%m-%d %H:%M:%S.%f") >= datetime.strptime(
                start_date, "%Y-%m-%d %H:%M:%S.%f"
            ) and datetime.strptime(result["timestamp"], "%Y-%m-%d %H:%M:%S.%f") <= datetime.strptime(
                end_date, "%Y-%m-%d %H:%M:%S.%f"
            ):
                filtered_results.append(result)
        return filtered_results
