import pytest
import os
from dotenv import dotenv_values


@pytest.mark.env
def test_env():
    print('\nvar from file')
    config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
    for v in config:
        print(f'{v}: {config[v]}')
    print('vars from env')
    print(os.environ)
