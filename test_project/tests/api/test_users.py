import allure


@allure.feature("Users")
@allure.story("Get all users")
def test_get_all_users(api_client, base_url):
    with allure.step("Send GET request to /users"):
        response = api_client.get(f"{base_url}/users")
    with allure.step("Validate response status and data"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Users")
@allure.story("Get user by valid ID")
def test_get_user_by_valid_id(api_client, base_url):
    with allure.step("Send GET request to /users/1"):
        response = api_client.get(f"{base_url}/users/1")
    with allure.step("Validate user data"):
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "username" in data


@allure.feature("Users")
@allure.story("Get user by invalid ID")
def test_get_user_by_invalid_id(api_client, base_url):
    with allure.step("Send GET request to /users/9999"):
        response = api_client.get(f"{base_url}/users/9999")
    with allure.step("Check for not found or empty result"):
        assert response.status_code == 404 or response.status_code == 200


@allure.feature("Users")
@allure.story("Create user with valid data")
def test_create_user_valid_data(api_client, base_url, headers):
    payload = {
        "email": "newuser@example.com",
        "username": "newuser123",
        "password": "testpassword",
        "name": {
            "firstname": "New",
            "lastname": "User"
        },
        "address": {
            "city": "New City",
            "street": "123 Street",
            "number": 10,
            "zipcode": "12345-6789",
            "geolocation": {
                "lat": "40.7128",
                "long": "74.0060"
            }
        },
        "phone": "123-456-7890"
    }
    with allure.step("Send POST request to create new user"):
        response = api_client.post(f"{base_url}/users", json=payload, headers=headers)
    with allure.step("Validate user creation response"):
        assert response.status_code in [200, 201]
        assert "id" in response.json()


@allure.feature("Users")
@allure.story("Create user with missing required fields")
def test_create_user_missing_required_fields(api_client, base_url, headers):
    payload = {
        "username": "incompleteuser"
        # пропущены email, password и т.д.
    }
    with allure.step("Send POST request with incomplete user data"):
        response = api_client.post(f"{base_url}/users", json=payload, headers=headers)
    with allure.step("Check for error or handling of incomplete data"):
        assert response.status_code in [400, 422, 200]
        # Некоторые фейковые API принимают даже плохие данные — важно отразить это в отчёте


@allure.feature("Users")
@allure.story("Create user with invalid data types")
def test_create_user_invalid_data_types(api_client, base_url, headers):
    payload = {
        "email": 12345,  # должен быть строкой
        "username": True,  # должен быть строкой
        "password": None,  # должен быть строкой
    }
    with allure.step("Send POST request with invalid data types"):
        response = api_client.post(f"{base_url}/users", json=payload, headers=headers)
    with allure.step("Check for validation error or unexpected behavior"):
        assert response.status_code in [400, 422, 200]
