import uuid
import json

from boto3.dynamodb.conditions import Attr
from chocs import HttpRequest, HttpResponse, HttpStatus
from datetime import datetime, timezone
from onboarding_marcin_dyjas.application import app  # noqa: E999
from onboarding_marcin_dyjas.repositories import TimestampRepository


@app.get("/onboarding/{name}")
def get_onboarding(request: HttpRequest) -> HttpResponse:
    name = request.path_parameters.get("name")
    return HttpResponse(body=f"Hello {name}, it is {datetime.now(timezone.utc)}", status=HttpStatus.OK)


@app.get("/timestamps")
def get_timestamps(request: HttpRequest) -> HttpResponse:
    timestamp_repository = TimestampRepository()
    timestamp_repository.add_timestamp(str(uuid.uuid4()), str(datetime.now()))
    return HttpResponse(status=HttpStatus.OK)
