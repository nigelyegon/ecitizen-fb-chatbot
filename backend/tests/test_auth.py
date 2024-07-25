import json


def test_register(test_client):
    response = test_client.post(
        "/api/v1/auth/register",
        data=json.dumps({"email": "test@ecitizen.com", "password": "test123"}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201
