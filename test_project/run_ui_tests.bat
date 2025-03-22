@echo off
echo Cleaning old Allure results...
if exist allure-results (
    rmdir /s /q allure-results
)

echo Running UI tests...
pytest tests/ui --browser=chromium --headless=false --alluredir=allure-results

echo Opening Allure report...
allure serve allure-results
