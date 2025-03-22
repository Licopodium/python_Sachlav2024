@echo off
echo Cleaning old Allure results...
if exist allure-results (
    rmdir /s /q allure-results
)

echo Running API tests...
pytest tests/api --alluredir=allure-results

echo Opening Allure report...
allure serve allure-results
