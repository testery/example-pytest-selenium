def test_title(chrome_browser):
    """
    Test the title of the Python.org website
    """
    chrome_browser.get("https://www.python.org")
    assert chrome_browser.title == "Welcome to Python.org"


def test_download(chrome_browser):
    """
    Test downloading a file from Python.org
    """
    chrome_browser.get("https://www.python.org/downloads/release/python-3140/")
    download_link = chrome_browser.find_element("link text", "Download Python install manager")
    download_link.click()
    second_download_link = chrome_browser.find_element("link text", "Download Installer (MSIX)")
    second_download_link.click()
    # Wait for the download to complete (you may want to add a more robust wait here)
    import time
    time.sleep(5)
    # Check if the file was downloaded
    import os
    script_directory = os.path.dirname(os.path.abspath(__file__))
    downloads_directory = os.path.join(script_directory, "..", "downloads")
    files_in_downloads = os.listdir(downloads_directory)
    assert len(files_in_downloads) > 0
