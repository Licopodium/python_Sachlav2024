import pytest
import requests
import allure

# Базовый URL для FakeStoreAPI
@pytest.fixture(scope="session")
def base_url():
    return "https://fakestoreapi.com"

# Заголовки (если понадобится)
@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json"
    }

# Универсальный API клиент с логированием в Allure
@pytest.fixture
def api_client():
    class APIClient:
        def get(self, url, **kwargs):
            with allure.step(f"GET {url}"):
                response = requests.get(url, **kwargs)
                self.attach_response(response)
                return response

        def post(self, url, **kwargs):
            with allure.step(f"POST {url}"):
                response = requests.post(url, **kwargs)
                self.attach_response(response)
                return response

        def put(self, url, **kwargs):
            with allure.step(f"PUT {url}"):
                response = requests.put(url, **kwargs)
                self.attach_response(response)
                return response

        def delete(self, url, **kwargs):
            with allure.step(f"DELETE {url}"):
                response = requests.delete(url, **kwargs)
                self.attach_response(response)
                return response

        @staticmethod
        def attach_response(response):
            allure.attach(
                body=response.request.method + " " + response.request.url + "\n\n" +
                     f"Status Code: {response.status_code}\n\n" +
                     response.text,
                name="Response",
                attachment_type=allure.attachment_type.TEXT
            )

    return APIClient()
