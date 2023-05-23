# Example Pytest Selenium

## Tags

- **webtest**: marks a test that uses selenium
- **fail**: marks a test that should fail
- **green**: marks a test that should pass

## To Run locally in vscode

### Test Explorer settings.json file

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
