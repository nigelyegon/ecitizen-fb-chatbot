def test_register(test_client):
    response = test_client.post(
        "/api/v1/auth/register",
        json={"email": "test@ecitizen.com", "password": "test123"},
    )
    assert response.status_code == 201


def test_login_success(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/auth/register",
        json=user,
    )
    res = test_client.post("/api/v1/auth/login", json=user)
    assert res.status_code == 200


def test_login_fail(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/auth/register",
        json=user,
    )
    res = test_client.post(
        "/api/v1/auth/login", json={"email": "test@ecitizen.com", "password": "test12"}
    )
    assert res.status_code == 401


def test_jwt_token_generation_success(test_client):
    user = {"email": "test@ecitizen.com", "password": "test123"}
    test_client.post(
        "/api/v1/auth/register",
        json=user,
    )
    res = test_client.post("/api/v1/auth/login", json=user)
    response = res.get_json()
    assert "access_token" in response
