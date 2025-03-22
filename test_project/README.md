
UI & API Automated Testing Project — TakeNote
📋 Project Description
This project contains both UI and API automated tests for the TakeNote application and a training REST API (FakeStoreAPI).

UI tests are written using Playwright and Python following the Page Object Model (POM) design pattern.

API tests are written using pytest, requests, and Allure, covering endpoints of the FakeStoreAPI.

The project is structured for scalability, clarity, and maintainability. All test layers are separated (tests/ui, tests/api, utils, pages), and the code is modular thanks to the use of __init__.py in all necessary folders.

All dependencies are listed in requirements.txt, and Allure is used for visual test reporting.

▶️ Installing and Running UI Tests
Requirements
Python 3.9+

pip

Git

Playwright

1. Clone the repository:
git clone <repository_URL>
cd test_project

2. Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate # macOS/Linux
.venv\Scripts\activate # Windows

3. Install dependencies and Playwright:
pip install -r requirements.txt
playwright install

4. Run UI tests with Allure report generation:
pytest tests/ui --browser=chromium --headless=false --alluredir=allure-results

5. Open the Allure report:
allure serve allure-results

🧪 Running API Tests
We created 18 API tests for the products, users, and carts endpoints of FakeStoreAPI.

1. Run all API tests:
pytest tests/api --alluredir=allure-results

2. Run a specific API test file (e.g., users):
pytest tests/api/test_users.py --alluredir=allure-results

3. Open the Allure report:
allure serve allure-results

The tests use custom fixtures in conftest.py, including:

api_client — a reusable request wrapper with Allure steps

base_url — the target API endpoint

headers — standard JSON headers

📂 Project Structure
test_project/
├── .github/ # GitHub workflows or configs
├── .venv/ # Virtual environment
├── allure-results/ # Allure test results
├── reports/ # Test run reports (if applicable)
├── structure.txt # Project structure notes
├── conftest.py # Global test fixtures
├── requirements.txt
├── pytest.ini
├── README.md
│
├── pages/ # Page Object classes for UI tests
│ ├── base_page.py
│ ├── note_page.py
│ └── init.py
│
├── tests/
│ ├── api/ # API tests
│ │ ├── test_products.py
│ │ ├── test_users.py
│ │ ├── test_carts.py
│ │ ├── conftest.py
│ │ └── init.py
│ │
│ ├── ui/ # UI tests (POM)
│ │ ├── test_notes.py
│ │ ├── test_context_menu.py
│ │ ├── test_sidebar.py
│ │ └── init.py
│ │
│ └── utils/ # Utility functions
│ ├── test_data.py
│ └── init.py

📫 Author
Marina Belorusova

