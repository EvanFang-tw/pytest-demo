import pytest


@pytest.mark.parametrize(
    "x, y, z",
    [
        (0, 0, 0),
        (1, 1, 0),
        (3, 2, 1),
        (3, 5, -2),
        (-1, -2, 1),
        (100, 100, 0),
        (-100, -200, 100),
    ],
)
def test_minus(x, y, z):
    assert x - y == z
