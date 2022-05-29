import pytest


@pytest.fixture
def userdata():
    yield [
        {"name": "Bob", "age": 16},
        {"name": "Mary", "age": 23},
        {"name": "David", "age": 31},
    ]
    # do clear job here
    pass


# refs:
# conftest.py:
# https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
