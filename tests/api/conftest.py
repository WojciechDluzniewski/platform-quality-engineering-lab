import pytest
import requests

@pytest.fixture(scope="session")
def user_service_base_url():
    return "http://localhost:8001"

@pytest.fixture(scope="session")
def product_service_base_url():
    return "http://localhost:8002"

@pytest.fixture
def http_client():
    return requests.Session()