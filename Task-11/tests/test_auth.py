from minitest import fixture

@fixture
def mock_user():
    return {
        "username": "admin",
        "password": "1234",
        "token": "valid_token"
    }

def login(username, password):
    if username == "admin" and password == "1234":
        return {"status": 200, "token": "valid_token"}
    return {"status": 401}

def test_login_valid_credentials(mock_user):
    response = login(mock_user["username"], mock_user["password"])
    assert response["status"] == 200

def test_login_invalid_password(mock_user):
    response = login(mock_user["username"], "wrong")
    assert response["status"] == 401

def test_login_expired_token(mock_user):
    response = {"status": 200}  # simulate bug
    assert response["status"] == 401, "Expected status=401, got status=200"