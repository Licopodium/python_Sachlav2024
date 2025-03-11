# Test Project

## Description
This project contains automated tests for the TakeNote application. Testing is performed using Playwright for UI and Requests for API.

## Requirements
Before starting, make sure you have installed:
- Python 3.9+
- pip
- Git
- Playwright

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_URL>
   cd test_project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Playwright and required browsers:
   ```bash
   playwright install
   ```

## Running Tests

### UI Tests
Run UI tests with Allure report generation:
```bash
pytest tests/ui --alluredir=reports/
```

### API Tests
Run API tests:
```bash
pytest tests/api --alluredir=reports/
```

## Viewing Allure Reports
After running the tests, open the report:
```bash
allure serve reports/
```

## CI/CD
The project is configured for automatic test execution in GitHub Actions (if workflow is set up).

## Authors
- Marina Belorusova

