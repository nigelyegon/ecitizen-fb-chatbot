def test_register(test_client):
    response = test_client.post(
        "/api/v1/chatbot/auth/register",
        json={"email": "test@ecitizen.com", "password": "test123"},
    )
    assert response.status_code == 201


def test_login_success(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    res = test_client.post("/api/v1/chatbot/auth/login", json=user)
    assert res.status_code == 200


def test_login_fail(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    res = test_client.post(
        "/api/v1/chatbot/auth/login", json={"email": "test@ecitizen.com", "password": "test12"}
    )
    assert res.status_code == 401


def test_jwt_token_generation_success(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    res = test_client.post("/api/v1/chatbot/auth/login", json=user)
    response = res.get_json()
    assert "access_token" in response


def test_user_logout_success(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    data = test_client.post("/api/v1/chatbot/auth/login", json=user)
    res = data.get_json()
    headers = {"Authorization": "Bearer {}".format(res["access_token"])}
    response = test_client.post("/api/v1/chatbot/auth/logout", headers=headers)
    message = response.get_json()["message"]
    assert message == "logout successful"


def test_refresh_token_generation_success(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    res = test_client.post("/api/v1/chatbot/auth/login", json=user)
    response = res.get_json()
    assert "refresh_token" in response


def test_access_token_generation_from_refresh_token(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    data = test_client.post("/api/v1/chatbot/auth/login", json=user)
    res = data.get_json()
    headers = {"Authorization": "Bearer {}".format(res["refresh_token"])}
    res = test_client.post("/api/v1/chatbot/auth/refresh", headers=headers)
    response = res.get_json()
    assert "access_token" in response


def test_successful_authorization_with_access_token(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    data = test_client.post("/api/v1/chatbot/auth/login", json=user)
    res = data.get_json()
    headers = {"Authorization": "Bearer {}".format(res["access_token"])}
    response = test_client.get("/api/v1/chatbot/", headers=headers)
    assert response.status_code == 200


def test_authorization_with_revoked_access_token(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/chatbot/auth/register",
        json=user,
    )
    data = test_client.post("/api/v1/chatbot/auth/login", json=user)
    res = data.get_json()
    headers = {"Authorization": "Bearer {}".format(res["access_token"])}
    test_client.post("/api/v1/chatbot/auth/logout", headers=headers)
    response = test_client.get("/api/v1/chatbot/", headers=headers)
    message = response.get_json()["msg"]
    assert response.status_code == 401
    assert message == "Token has been revoked"
