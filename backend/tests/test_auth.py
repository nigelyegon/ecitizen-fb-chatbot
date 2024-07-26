import json


def test_register(test_client):
    response = test_client.post(
        "/api/v1/auth/register",
        data=json.dumps({"email": "test@ecitizen.com", "password": "test123"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201


def test_login(test_client):
    data = json.dumps({"email": "test@ecitizen.com", "password": "test123"})
    test_client.post(
        "/api/v1/auth/register",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    response = test_client.post(
        "/api/v1/auth/login",
        data=json.dumps({"email": "test@ecitizen.com", "password": "test123"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
