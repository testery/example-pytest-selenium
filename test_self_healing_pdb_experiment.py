"""
Self-healing pdb/CDP experiment.

Run with:

    pytest test_self_healing_pdb_experiment.py --pdb --driver Chrome

What happens:
  1. Chrome launches with --remote-debugging-port=<cdp-port> (default 9922
     -- deliberately NOT 9222, the ubiquitous default every other CDP tool
     reaches for first; override with --cdp-port or the CDP_PORT env var).
  2. The test drives the page and hits a broken locator on purpose, raising
     NoSuchElementException.
  3. Because the run used --pdb, pytest drops into a live (Pdb) prompt at
     the exact point of failure -- BEFORE the `selenium` fixture tears the
     browser down. The browser stays open and connected.

pdb's post-mortem prompt lands you in the innermost frame -- i.e. inside
selenium's own client code (errorhandler.py/webdriver.py), NOT your test
function -- so `selenium` isn't a local there yet. Run `up` (`u`) three
times to climb out of selenium's find_element -> execute -> check_response
call chain and land back in test_self_healing_locator's frame, where
`selenium` is:

    (Pdb) u
    (Pdb) u
    (Pdb) u
    (Pdb) selenium.title
    (Pdb) selenium.page_source
    (Pdb) selenium.save_screenshot("debug.png")
    (Pdb) selenium.find_elements("css selector", "nav a")
    (Pdb) heading = selenium.find_element("css selector", "h1")   # fixed locator
    (Pdb) heading.text

(If the exact frame depth ever shifts with a library/pytest version bump,
`bt`/`where` shows the full stack -- look for the frame whose file is this
test file and `up`/`down` to it directly.)

Because Chrome was launched with a fixed CDP port, any *other* tool can
attach to that same browser instance at the same time -- without
disturbing the paused pdb session -- e.g.:

    curl http://localhost:9922/json           # list live CDP targets/pages
    playwright.chromium.connect_over_cdp("http://localhost:9922")

Before picking a port, check nothing else already owns it
(`netstat -ano | findstr :9922` on Windows) -- and if you ever do find a
stray process squatting on it, don't just kill it; it may belong to
someone else's session.

`c` (continue) or `q` (quit) at the (Pdb) prompt resumes/aborts the test and
lets the `selenium` fixture close the browser as normal.
"""
import pytest


@pytest.mark.pdb_experiment
@pytest.mark.webtest
def test_self_healing_locator(selenium):
    selenium.get("https://www.testery.com")

    # Deliberately wrong locator -- stands in for a selector that broke
    # because the page changed. This is the "exception" the experiment is
    # built around: it should land you at a live (Pdb) prompt with
    # `selenium` still attached to the open browser.
    broken_locator = ("css selector", "#this-id-does-not-exist-on-the-page")
    element = selenium.find_element(*broken_locator)

    assert element.is_displayed()
