from chocs.testing import TestClient
from chocs import HttpStatus


def test_get_onboarding_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/onboarding/Marcin")
    assert response.status_code == HttpStatus.OK

