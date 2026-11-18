import os

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cdp-port",
        action="store",
        default=os.environ.get("CDP_PORT", "9922"),
        help="Port Chrome exposes the DevTools Protocol on. Lets an external "
             "tool (Playwright's connect_over_cdp, chrome://inspect, a raw "
             "CDP client, ...) attach to the same browser pytest is driving "
             "-- including while pytest is paused at a --pdb breakpoint. "
             "Deliberately NOT the ubiquitous 9222 default (VS Code, "
             "Puppeteer, Playwright, chrome://inspect all reach for that "
             "one first) to avoid colliding with an unrelated Chrome/CDP "
             "session already using it.",
    )


@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    port = pytestconfig.getoption("--cdp-port")
    chrome_options.add_argument(f"--remote-debugging-port={port}")
    return chrome_options
