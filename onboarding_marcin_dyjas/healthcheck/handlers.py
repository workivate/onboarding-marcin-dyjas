from chocs import HttpRequest, HttpResponse, HttpStatus
from lw_api_status import ApiStatus
from onboarding_marcin_dyjas.application import app  # noqa: E999


@app.get("/ping")
def get_ping(request: HttpRequest) -> HttpResponse:
    return HttpResponse(status=HttpStatus.NO_CONTENT)


@app.get("/status")
def get_status(request: HttpRequest) -> HttpResponse:
    return ApiStatus(api_id="onboarding-marcin-dyjas").generate_status_response()


@app.options("/status")
def options_status(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status=HttpStatus.OK,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Headers": "accept, Authorization",
            "Access-Control-Allow-Methods": "OPTIONS, GET",
        },
    )
