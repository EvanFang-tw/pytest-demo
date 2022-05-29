import pytest


def test_raises_error():
    a = [1, 2, 3]
    with pytest.raises(IndexError):
        a[3] = 4
