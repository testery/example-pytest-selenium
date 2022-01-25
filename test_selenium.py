import pytest
import os
import datetime


@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    if os.environ.get('IS_TESTERY') == 'true':
        for arg in os.environ.get('TESTERY_CHROME_ARGS').split(';'):
            chrome_options.add_argument(arg)

    return chrome_options


@pytest.mark.webtest
def test_example(selenium):
    selenium.get('http://www.testery.io')
    take_screenshot(selenium)

    assert selenium.title == "Testery - full-stack parallel testing test"


@pytest.mark.parametrize(
    ("url", "title"), [pytest.param('http://www.testery.io',
                                    "Testery - full-stack parallel testing", marks=pytest.mark.webtest),
                       pytest.param('http://www.testery.io',
                                    "Bad Title", marks=[pytest.mark.fail, pytest.mark.webtest])]
)
def test_site(selenium, url, title):
    selenium.get(url)

    take_screenshot(selenium)
    assert selenium.title == title


def take_screenshot(selenium):
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    path = "screenshots/" + "{0}.png".format(date)
    print("Saving screenshot to: " + path)
    selenium.save_screenshot(path)
