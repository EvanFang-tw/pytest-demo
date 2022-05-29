from unittest.mock import Mock


class MyDatabase:
    def __init__(self):
        pass

    def query(self):
        return "hello"


class MyServcie:
    def __init__(self, db: MyDatabase):
        self.db = db

    def get_data(self):
        return self.db.query()


def test_service_get_data():
    """
    It should query from database.
    """
    # arrange
    spy_db = Mock(MyDatabase)
    spy_db.query.return_value = "world"

    # act
    service = MyServcie(spy_db)
    reuslt = service.get_data()

    # assert
    spy_db.query.assert_called()
    assert reuslt == "world"
    # or
    # assert spy_db.query.called
