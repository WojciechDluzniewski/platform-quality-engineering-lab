def test_get_existing_product_returns_product_data(http_client, product_service_base_url):
    """
    Method gets and verifies data of the existing product
    :param http_client: session
    :param product_service_base_url: basic url for product service
    :return: None
    """

    response = http_client.get(f"{product_service_base_url}/products/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["price"] > 0
    assert isinstance(data["available"], bool)

def test_get_non_existing_product_returns_product_data(http_client, product_service_base_url):
    """
    Method gets and verifies error of the not existing product
    :param http_client: session
    :param product_service_base_url: basic url for product service
    :return: None
    """
    response = http_client.get(f"{product_service_base_url}/products/100")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"