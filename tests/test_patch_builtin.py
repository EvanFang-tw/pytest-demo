from unittest.mock import Mock, patch


class Restaurant:
    def greatest_drink(self):
        return max(["water", "coke", "juice"])  # it shall return "water"


@patch("builtins.max")
def test_mock_built_in_function(mock_max: Mock):
    """
    Let's do some trick, make the built in function `max` to behave as `min`.
    """
    mock_max.side_effect = min
    assert Restaurant().greatest_drink() == "coke"
