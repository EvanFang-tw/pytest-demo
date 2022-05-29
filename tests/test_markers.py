import pytest


@pytest.mark.skip
def test_1():
    assert 1 == 1


@pytest.mark.ignore
def test_2():
    assert 1 == 1
