import pytest


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
