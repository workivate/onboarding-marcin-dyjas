from chocs import HttpRequest, HttpResponse, HttpStatus
from datetime import datetime
from lw_api_status import ApiStatus
from onboarding_marcin_dyjas.application import app  # noqa: E999


@app.get("/onboarding/{name}")
def get_onboarding(request: HttpRequest) -> HttpResponse:
    name = request.path_parameters["name"]
    name[0] = name[0].upper()
    return chocs.HttpResponse(f"Hello {name}, it is {datetime.now(timezone.utc)}")
