import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Required for running in containers
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited shared memory in Docker
    options.add_argument("--disable-gpu")  # Recommended for headless mode
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
