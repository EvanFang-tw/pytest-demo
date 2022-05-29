# note that: userdata fixture is injected from conftest.py


def test_users(userdata):
    assert len(userdata) == 3


# ref:
# https://docs.pytest.org/en/6.2.x/fixture.html
