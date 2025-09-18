def test_title(chrome_browser):
    """
    Test the title of the Python.org website
    """
    chrome_browser.get("https://www.python.org")
    assert chrome_browser.title == "Welcome to Python.org"
