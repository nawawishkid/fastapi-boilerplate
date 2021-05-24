from app.main import app
from tests.setup import get_test_client

client = get_test_client(app)


def test_create_user_succeed():
    data = {"email": "hello@google.com", "password": "lorem"}
    response = client.post(
        '/v1/users', json=data)

    assert response.status_code == 201
    json = response.json()

    assert json["email"] == data["email"]
    assert "password" not in json
    assert "id" in json and isinstance(json["id"], int)


def test_create_user_already_exists():
    data = {"email": "hello@google.com", "password": "lorem"}
    response = client.post('/v1/users', json=data)

    assert response.status_code == 409
