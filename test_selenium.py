import pytest


@pytest.fixture
def driver_args():
    if os.environ.get('IS_TESTERY') == 'true':
        return os.environ.get('TESTERY_CHROME_ARGS').split(';')
    else:
        return []


@pytest.mark.webtest
def test_example(selenium):
    selenium.get('http://www.testery.io')

    assert selenium.title == "Testery - Cloud-based continuous testing platform"


@pytest.mark.parametrize(
    ("url", "title"), [pytest.param('http://www.testery.io',
                                    "Testery - Cloud-based continuous testing platform", marks=pytest.mark.webtest)]
)
def test_increment(selenium, url, title):
    selenium.get(url)

    assert selenium.title == title
