# Example Pytest Selenium

## Tags

- **webtest**: marks a test that uses selenium
- **fail**: marks a test that should fail
- **green**: marks a test that should pass

## To Run locally in vscode

### Test Explorer settings.json file

## Setup

1. Install [Python 3](https://www.python.org/downloads/) (this also installs the python package-management system - pip)

1. Set up [virtual environment](https://docs.python.org/3/library/venv.html)

1. Install the ``requirements.txt`` through the terminal
   run ```pip install -r requirements.txt```

1. Set up any IDE configurations

    ```json
    {
        "python.testing.pytestArgs": [
            ".",
            "--driver",
            "Chrome"
        ],
        "python.testing.unittestEnabled": false,
        "python.testing.pytestEnabled": true
    }
    ```

## Sample pytest commands and arguments

Pytest help

```pytest --help```

Run sample non-selenium tests in a file

```pytest -s test/test_class.py```

Run selenium tests in a file

```pytest ./test_selenium.py --driver Chrome```

```pytest ./test/test_basic.py --driver Chrome```
