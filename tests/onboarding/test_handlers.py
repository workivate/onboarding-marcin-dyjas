from chocs import HttpStatus
from chocs.testing import TestClient


def test_get_onboarding_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/onboarding?name=Marcin")
    assert response == HttpResponse((f"Hello Marcin, it is {datetime.now(timezone.utc)}"))

    response = test_client.get("/onboarding?name=marcin")
    assert response == HttpResponse((f"Hello Marcin, it is {datetime.now(timezone.utc)}"))