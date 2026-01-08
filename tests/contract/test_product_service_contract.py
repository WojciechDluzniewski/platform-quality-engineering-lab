import requests
from jsonschema import validate


def test_product_service_response_matches_openapi_schema(load_openapi_spec):
    spec = load_openapi_spec("contracts/product-service-openapi.yaml")

    schema = spec["components"]["schemas"]["Product"]

    response = requests.get("http://localhost:8002/products/1")
    assert response.status_code == 200

    validate(instance=response.json(), schema=schema)