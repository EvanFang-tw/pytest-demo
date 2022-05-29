from unittest.mock import Mock


class MyDatabase:
    def __init__(self):
        pass

    def query(self, sql):
        return "hello"


class MyServcie:
    def __init__(self, db: MyDatabase):
        self.db = db

    def get_data(self):
        return self.db.query("select * from user_table")


def verify_sql():
    def query(sql):
        if sql != "select * from user_table":
            raise ValueError("oops")
        return "world"

    return query


def test_service_get_data_with_mock():
    """
    It should query from database.
    """
    # arrange
    mock_db = Mock(MyDatabase)
    mock_db.query = Mock(side_effect=verify_sql())

    # act
    service = MyServcie(mock_db)
    reuslt = service.get_data()

    # assert
    assert reuslt == "world"


def test_service_get_data_with_spy():
    """
    It should query from database.
    """
    # arrange
    spy_db = Mock(MyDatabase)
    spy_db.query = Mock()
    spy_db.query.return_value = "world"

    # act
    service = MyServcie(spy_db)
    reuslt = service.get_data()

    # assert
    assert reuslt == "world"
    spy_db.query.assert_called_once_with("select * from user_table")
