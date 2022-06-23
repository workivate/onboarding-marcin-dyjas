from chocs import HttpStatus, HttpResponse, HttpRequest
from chocs.testing import TestClient

from onboarding_marcin_dyjas.onboarding.handlers import get_timestamps
from onboarding_marcin_dyjas.repositories import TimestampRepository


def test_get_onboarding_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/onboarding/Marcin")
    assert response.status_code == HttpStatus.OK

def test_get_timestamps_endpoint() -> None:
    timestamps_repo = TimestampRepository()
    response = get_timestamps(HttpRequest("GET"), timestamps_repo)
    assert response.status_code == HttpStatus.OK