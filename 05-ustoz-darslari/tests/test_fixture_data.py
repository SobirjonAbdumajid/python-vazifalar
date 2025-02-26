import pytest


@pytest.fixture(scope='session', autouse=True)
def mock_user_data():
    print("\nSession scope fixture was opened")
    users = {
        "id": 1, "username": "alice", "email": "alica@gmail.com", "age": 15
    }

    yield users

    print("\nSession scope fixture was closed")


def test_user_data_1():
    pass
    # assert mock_user_data["id"] == 1
    # assert mock_user_data["username"] == "alice"


# def test_user_data_2(mock_user_data):
#     assert mock_user_data["email"] == "alica@gmail.com"
#     assert mock_user_data["age"] == 15
