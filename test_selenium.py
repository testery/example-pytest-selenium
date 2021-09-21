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

    assert selenium.title == "Testery - Cloud-based continuous testing platform"


@pytest.mark.parametrize(
    ("url", "title"), [pytest.param('http://www.testery.io',
                                    "Testery - Cloud-based continuous testing platform", marks=pytest.mark.webtest),
                       pytest.param('http://www.testery.io',
                                    "Bad Title", marks=[pytest.mark.fail, pytest.mark.webtest])]
)
def test_site(selenium, url, title):
    selenium.get(url)

    take_screenshot(selenium)
    assert selenium.title == title


def take_screenshot(selenium):
    fulldate = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = '/{0}.png'.format(fulldate)
    path = "screenshots/" + file_name
    print("Saving screenshot at: " + path)
    selenium.save_screenshot(path)
