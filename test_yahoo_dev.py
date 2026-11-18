"""
Interactive development scratch test.

Navigates to https://www.yahoo.com and then pauses in a live_repl() session
-- with Chrome attached on the CDP port configured in conftest.py -- so the
page can be explored and the real assertions/interactions built up
statement by statement before being folded into a permanent test.

Commands are sent by appending lines to .live_repl/cmd.txt; results and
tracebacks appear in .live_repl/out.log. Write __CONTINUE__ to end the
session.
"""
import pytest

from live_repl import live_repl


@pytest.mark.webtest
def test_yahoo_dev(selenium):
    selenium.get("https://www.yahoo.com")
    live_repl(locals())
