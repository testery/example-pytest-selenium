import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from datetime import datetime
import pytz


def take_screenshot(chrome_browser):
    date = datetime.now().strftime('%Y%m%d_%H%M%S')
    path = "screenshots/" + "{0}.png".format(date)
    print("Saving screenshot to: " + path)
    chrome_browser.save_screenshot(path)


def test_title(chrome_browser):
    chrome_browser.get("https://www.python.org")
    take_screenshot(chrome_browser)
    assert chrome_browser.title == "Welcome to Python.org"


def test_timezone(chrome_browser):
    response = requests.get("https://timeapi.io/api/time/current/zone?timeZone=America/Los_Angeles")
    json_response = response.json()
    print(json_response['dateTime'])
    actual_time = datetime.strptime(json_response['dateTime'].split('.')[0], "%Y-%m-%dT%H:%M:%S")

    # Get the current UTC time
    utc_now = datetime.now(pytz.UTC)

    # Convert to Pacific Time
    pacific_timezone = pytz.timezone('America/Los_Angeles')
    pacific_time = utc_now.astimezone(pacific_timezone)
    expected_tz = pacific_time.utcoffset().total_seconds() / 3600
    expected_tz = f"(UTC{int(expected_tz)})"
    print(expected_tz)

    # Format the time as a string
    formatted_time = pacific_time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current Pacific Time: {formatted_time}")

    assert formatted_time == actual_time.strftime("%Y-%m-%d %H:%M:%S")

    chrome_browser.get("https://time.gov/")
    time.sleep(10)
    #WebDriverWait(chrome_browser, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    #.until(EC.visibility_of_element_located((By.ID, 'analog-clock')))
    browser_tz = chrome_browser.find_element(By.ID, 'myTimeTitle').text
    take_screenshot(chrome_browser)
    assert expected_tz == browser_tz
