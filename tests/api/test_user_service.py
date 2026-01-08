def test_get_existing_user_returns_data(http_client, user_service_base_url):
    """
    Method gets and verifies data of the existing user
    :param http_client: session
    :param user_service_base_url: basic url for user service
    :return: None
    """

    response = http_client.get(f"{user_service_base_url}/users/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["name"]
    assert "@" in data["email"]
    assert data["is_active"] is True


def test_get_non_existing_user_returns_not_found(http_client, user_service_base_url):
    """
    Method gets and verifies error of the not existing user
    :param http_client: session
    :param user_service_base_url: basic url for user service
    :return: None
    """
    response = http_client.get(f"{user_service_base_url}/users/100")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"