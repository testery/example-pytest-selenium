import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
