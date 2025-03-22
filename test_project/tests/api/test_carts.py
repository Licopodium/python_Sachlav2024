import allure
from datetime import datetime


@allure.feature("Carts")
@allure.story("Get all carts")
def test_get_all_carts(api_client, base_url):
    with allure.step("Send GET request to /carts"):
        response = api_client.get(f"{base_url}/carts")
    with allure.step("Validate response status and format"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Carts")
@allure.story("Get cart by valid ID")
def test_get_cart_by_valid_id(api_client, base_url):
    with allure.step("Send GET request to /carts/1"):
        response = api_client.get(f"{base_url}/carts/1")
    with allure.step("Validate cart data"):
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "products" in data


@allure.feature("Carts")
@allure.story("Get cart by invalid ID")
def test_get_cart_by_invalid_id(api_client, base_url):
    with allure.step("Send GET request to non-existent /carts/9999"):
        response = api_client.get(f"{base_url}/carts/9999")
    with allure.step("Validate response code or empty body"):
        assert response.status_code == 404 or response.status_code == 200


@allure.feature("Carts")
@allure.story("Get carts for a specific user")
def test_get_carts_by_user_id(api_client, base_url):
    with allure.step("Send GET request to /carts/user/1"):
        response = api_client.get(f"{base_url}/carts/user/1")
    with allure.step("Validate user carts"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Carts")
@allure.story("Create a new cart")
def test_create_cart(api_client, base_url, headers):
    payload = {
        "userId": 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "products": [
            {"productId": 1, "quantity": 2},
            {"productId": 2, "quantity": 1}
        ]
    }
    with allure.step("Send POST request to create new cart"):
        response = api_client.post(f"{base_url}/carts", json=payload, headers=headers)
    with allure.step("Validate cart creation"):
        assert response.status_code in [200, 201]
        assert "id" in response.json()


@allure.feature("Carts")
@allure.story("Delete a cart by ID")
def test_delete_cart(api_client, base_url):
    payload = {
        "userId": 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "products": [
            {"productId": 1, "quantity": 1}
        ]
    }
    with allure.step("Create a new cart to delete"):
        create_resp = api_client.post(f"{base_url}/carts", json=payload)
        cart_id = create_resp.json().get("id")

    with allure.step(f"Send DELETE request to /carts/{cart_id}"):
        delete_resp = api_client.delete(f"{base_url}/carts/{cart_id}")

    with allure.step("Validate deletion response"):
        assert delete_resp.status_code == 200
