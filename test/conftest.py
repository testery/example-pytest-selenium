import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(pytestconfig):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Required for running in containers
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited shared memory in Docker
    options.add_argument("--disable-gpu")  # Recommended for headless mode
    port = pytestconfig.getoption("--cdp-port")
    options.add_argument(f"--remote-debugging-port={port}")
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
