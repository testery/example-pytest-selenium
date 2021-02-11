import pytest


class TestClass:
    def test_one(self):
        print("Hello from test_one")
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hello"
