import uuid
import json

from chocs import HttpRequest, HttpResponse, HttpStatus
from datetime import datetime, timezone
from onboarding_marcin_dyjas.application import app  # noqa: E999
from onboarding_marcin_dyjas.repositories import TimestampRepository


@app.get("/onboarding/{name}")
def get_onboarding(request: HttpRequest) -> HttpResponse:
    name = request.path_parameters.get("name")
    message = f"Hello {name}, it is {datetime.now(timezone.utc)}"
    body = json.dumps({"message": message})
    return HttpResponse(body=body, status=HttpStatus.OK)


@app.post("/timestamps")
def post_timestamps(request: HttpRequest) -> HttpResponse:
    timestamp_repository = TimestampRepository()
    timestamp_repository.add_timestamp(str(uuid.uuid4()), str(datetime.now()))
    body = request.parsed_body
    if "from" in body.keys() and "to" in body.keys():
        start_date = body["from"]
        end_date = body["to"]
        results = timestamp_repository.get_filtered_timestamps(start_date, end_date)
    else:
        results = timestamp_repository.get_filtered_timestamps()
    return HttpResponse(status=HttpStatus.OK, body=json.dumps(results))
