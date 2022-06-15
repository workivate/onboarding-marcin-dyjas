import pytest
from chocs.testing import TestClient
from onboarding_marcin_dyjas.application import app  # noqa: E999

# Suppress pytest errors due to class name
TestClient.__test__ = False


@pytest.fixture
def test_client() -> TestClient:
    app.use("onboarding_marcin_dyjas.healthcheck.handlers")

    client = TestClient(app)
    return client
