from unittest.mock import Mock


class MyDatabase:
    def __init__(self):
        pass

    def query(self, sql):
        pass


class MyServcie:
    def __init__(self, db: MyDatabase):
        self.db = db

    def get_data(self):
        return self.db.query("select * from user_table")


def test_service_get_data_with_stub():
    """
    It should query from database.
    """
    # arrange
    stub_db = Mock(MyDatabase)
    stub_db.query = Mock()
    stub_db.query.return_value = "world"

    # act
    service = MyServcie(stub_db)
    reuslt = service.get_data()

    # assert
    assert reuslt == "world"
