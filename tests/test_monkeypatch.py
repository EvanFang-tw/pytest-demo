from unittest.mock import Mock, patch


class Restaurant:
    def get_food():
        return "pizza"


def go_to_restaurant():
    """
    Go to a restaurant to get your food.
    """
    restaurant = Restaurant()
    return restaurant.get_food()


def test_go_to_restaurant():
    """
    Make sure we can get some kind of food from the restaurant.
    """
    with patch("tests.test_monkeypatch.Restaurant") as test_restaurant_class:
        # arrange
        mocked_restaurant = Mock()
        mocked_restaurant.get_food = Mock(return_value="hamburger")
        test_restaurant_class.return_value = mocked_restaurant

        # act
        food = go_to_restaurant()

        # assert
        assert food == "hamburger"


@patch("tests.test_monkeypatch.Restaurant")
def test_go_to_restaurant_with_decorator(test_restaurant_class):
    """
    Do the same test as above, but using `@patch` to make code cleaner
    """
    # arrange
    mocked_restaurant = Mock()
    mocked_restaurant.get_food = Mock(return_value="hamburger")
    test_restaurant_class.return_value = mocked_restaurant

    # act
    food = go_to_restaurant()

    # assert
    assert food == "hamburger"
