import requests
from jsonschema import validate


def test_user_service_response_fit_openapi_schema(load_openapi_spec):
    spec = load_openapi_spec("contracts/user-service-openapi.yaml")

    schema = spec["components"]["schemas"]["User"]

    response = requests.get("http://localhost:8001/users/1")
    assert response.status_code == 200

    validate(instance=response.json(), schema=schema)