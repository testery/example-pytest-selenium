import pytest
import os
import datetime


@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    if os.environ.get('IS_TESTERY') == 'true':
        for arg in os.environ.get('TESTERY_CHROME_ARGS').split(';'):
            chrome_options.add_argument(arg)

    return chrome_options


@pytest.mark.green
@pytest.mark.webtest
def test_title_example(selenium):
    selenium.get('https://www.testery.com')
    take_screenshot(selenium)

    assert selenium.title.startswith("Testery:")
    assert "Flake-Free" in selenium.title


@pytest.mark.green
@pytest.mark.webtest
def test_title_two_example(selenium):
    selenium.get('https://testery.com/services')
    take_screenshot(selenium)

    assert "Professional Services" in selenium.title


@pytest.mark.parametrize(
    ("url", "title"), [pytest.param('https://testery.io/pricing',
                                    "Flake-Free",
                                    marks=[pytest.mark.webtest, pytest.mark.green]),
                       pytest.param('https://testery.io/case-studies',
                                    "Bad Title",
                                    marks=[pytest.mark.fail, pytest.mark.webtest])]
)
def test_site(selenium, url, title):
    selenium.get(url)

    take_screenshot(selenium)
    assert selenium.title.startswith("Testery:")
    assert title in selenium.title


def take_screenshot(selenium):
    date = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    path = "screenshots/" + "{0}.png".format(date)
    print("Saving screenshot to: " + path)
    selenium.save_screenshot(path)
