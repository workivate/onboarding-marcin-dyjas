import os
import boto3

from chocs_middleware.trace import Logger
from kink import di

from onboarding_marcin_dyjas.repositories import TimestampRepository


def bootstrap_di() -> None:
    di["log"] = Logger.get(name=__name__, level=os.getenv("LOG_LEVEL", "ERROR"))
    di["timestamp_table"] = boto3.resource("dynamodb", "eu-west-1").Table("onboarding-marcin-dyjas-timestampTable-RRS8GDPCU4RD")
    di[TimestampRepository] = TimestampRepository()
