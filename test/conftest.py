import os
import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    if os.environ.get('IS_TESTERY') == 'true':
        for arg in os.environ.get('TESTERY_CHROME_ARGS').split(';'):
            options.add_argument(arg)
    options.add_argument('--timezone="America/Los_Angeles"')
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(options=options, service=service)
    tz_params = {'timezoneId': 'America/Los_Angeles'}
    driver.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)
    yield driver
    driver.quit()
