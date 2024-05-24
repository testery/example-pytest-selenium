# Example Pytest Selenium

## Tags

- **webtest**: marks a test that uses selenium
- **fail**: marks a test that should fail
- **green**: marks a test that should pass

## To Run locally in vscode

### Test Explorer settings.json file

##Setup
1) Install Python 3.9
https://www.python.org/downloads/ (this also installs the python package-management system - pip)
2) Set Python as the interpreter in your IDE
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
3) Install the ``requirements.txt`` through the IDE

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

## Command Line

```bash
pytest . --driver Chrome
```

Install required python libraries

```pip install -r requirements.txt```

Install pytest

```pip install pytest```

Install pytest and pytest-selenium

```pip install pytest pytest-selenium```

Install addition dependencies

```pip install webdriver-manager```

##Sample pytest commands and arguments

Pytest help

```pytest --help```

Run sample tests in a file

```pytest -s test/test_basic.py```