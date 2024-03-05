import pytest
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
    def test_flaky_one(self):
        flip_coin = random.randint(0, 1)
        assert flip_coin == 0
