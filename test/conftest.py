import os
import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.abspath(os.path.join(script_directory, "..", "downloads"))
    os.makedirs(download_dir, exist_ok=True)
    chrome_prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True  # ensures downloads are allowed
    }
    options.add_experimental_option('prefs', chrome_prefs)
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Required for running in containers
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited shared memory in Docker
    options.add_argument("--disable-gpu")  # Recommended for headless mode
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
