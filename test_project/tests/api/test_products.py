import allure


@allure.feature("Products")
@allure.story("Get all products")
def test_get_all_products(api_client, base_url):
    with allure.step("Send GET request to /products"):
        response = api_client.get(f"{base_url}/products")
    with allure.step("Validate response status and data format"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Products")
@allure.story("Get product by valid ID")
def test_get_product_by_valid_id(api_client, base_url):
    with allure.step("Send GET request to /products/1"):
        response = api_client.get(f"{base_url}/products/1")
    with allure.step("Validate response content"):
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "title" in data and "price" in data


@allure.feature("Products")
@allure.story("Get product by invalid ID")
def test_get_product_by_invalid_id(api_client, base_url):
    with allure.step("Send GET request to non-existent /products/9999"):
        response = api_client.get(f"{base_url}/products/9999")
    with allure.step("Check for 404 or empty response"):
        assert response.status_code == 404 or response.status_code == 200


@allure.feature("Products")
@allure.story("Get products by category")
def test_get_products_by_category(api_client, base_url):
    with allure.step("Send GET request to /products/category/electronics"):
        response = api_client.get(f"{base_url}/products/category/electronics")
    with allure.step("Validate response is list of products"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Products")
@allure.story("Create a new product")
def test_create_product(api_client, base_url, headers):
    payload = {
        "title": "Test Product",
        "price": 99.99,
        "description": "Test description",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }
    with allure.step("Send POST request to create a product"):
        response = api_client.post(f"{base_url}/products", json=payload, headers=headers)
    with allure.step("Validate creation response"):
        assert response.status_code in [200, 201]
        assert "id" in response.json()


@allure.feature("Products")
@allure.story("Delete a product")
def test_delete_product(api_client, base_url):
    payload = {
        "title": "To Delete",
        "price": 12.99,
        "description": "To be deleted",
        "image": "https://i.pravatar.cc",
        "category": "test"
    }
    with allure.step("Create a product to be deleted"):
        create_resp = api_client.post(f"{base_url}/products", json=payload)
        product_id = create_resp.json().get("id")

    with allure.step(f"Send DELETE request to /products/{product_id}"):
        delete_resp = api_client.delete(f"{base_url}/products/{product_id}")

    with allure.step("Validate deletion response"):
        assert delete_resp.status_code == 200
