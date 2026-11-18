import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.webtest
@pytest.mark.green
def test_search_yahoo_for_testery(selenium):
    selenium.get("https://www.yahoo.com")
    original_window = selenium.current_window_handle

    search_box = selenium.find_element("id", "uh-sbq")
    search_box.send_keys("testery")
    search_box.send_keys(Keys.RETURN)

    # Yahoo opens search results in a new tab rather than navigating in place.
    WebDriverWait(selenium, 10).until(EC.number_of_windows_to_be(2))
    new_window = [h for h in selenium.window_handles if h != original_window][0]
    selenium.switch_to.window(new_window)

    WebDriverWait(selenium, 10).until(EC.title_contains("testery"))
    assert "testery" in selenium.title.lower()

    results = WebDriverWait(selenium, 10).until(
        EC.presence_of_all_elements_located(
            ("css selector", "div.algo-sr h3, ol.searchCenterMiddle h3")
        )
    )
    assert any("testery" in result.text.lower() for result in results)
