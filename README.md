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

## Self-healing pdb/CDP experiment (`feature/self-healing-pdb-experiment`)

`test_self_healing_pdb_experiment.py` is a sandbox for driving Chrome through
Selenium while also exposing it on a Chrome DevTools Protocol (CDP) port, so
a live debugger session and an external tool can both look at the same
browser at once.

Run it with `--pdb` so pytest drops into a real `(Pdb)` prompt at the moment
the test throws, instead of tearing the browser down:

```pytest test_self_healing_pdb_experiment.py --pdb --driver Chrome```

- Every test gets `--remote-debugging-port=<port>` added to its Chrome
  options (default `9922`; override with `--cdp-port=<port>` or the
  `CDP_PORT` env var) -- see the root `conftest.py`. `9922` is deliberately
  *not* `9222` -- that's the port every other CDP tool (VS Code, Puppeteer,
  Playwright, `chrome://inspect`) reaches for first, so using it risks
  colliding with an unrelated session. Check a port is actually free before
  using it (`netstat -ano | findstr :<port>` on Windows) -- if something
  else already owns it, pick a different port rather than killing it.
- Because pytest's fixture teardown runs *after* the post-mortem debugger
  exits, the browser is still open and attached when you land at `(Pdb)`.
  `selenium` (or `chrome_browser`, for tests under `test/`) is in scope, but
  post-mortem `pdb` starts in the innermost frame -- inside Selenium's own
  client code, not your test function -- so run `up` a few times (`bt` to
  see the full stack) until the prompt shows your test file, then you have
  the live `WebDriver` to inspect the page, try a corrected locator, edit
  variables, etc. right there in real Python.
- Because the CDP port is fixed and external, any other tool can attach to
  that same running browser concurrently -- `curl http://localhost:9922/json`
  or `playwright.chromium.connect_over_cdp(...)` -- to look at the
  DOM/network/console without disturbing the paused session.
- `c` (continue) or `q` (quit) at the `(Pdb)` prompt resumes/aborts the test
  and lets the fixture close the browser normally.
