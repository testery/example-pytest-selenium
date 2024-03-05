import pytest
import datetime
import random


@pytest.mark.parametrize(
    ("value_one", "value_two"),
    [
        ("a", "a"),
        ("b::b", "b::b"),
        (True, True),
    ],
)
@pytest.mark.green
def test_truth(value_one, value_two):
    assert value_one == value_two


@pytest.mark.green
class TestClass:
    def test_one(self):
        print("Hello from test_one")
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hello"


@pytest.mark.flaky
class TestFlaky:
    def test_flaky_time_based(self):
        now = datetime.datetime.now()
        minute = now.minute
        if minute <= 15:
            result = False
        elif 15 < minute <= 30:
            result = True
        elif 30 < minute <= 45:
            result = False
        else:
            result = True
        assert result is True

    def test_flaky_coin_toss(self):
        coin_toss = random.randint(0, 1)
        assert coin_toss == 0
