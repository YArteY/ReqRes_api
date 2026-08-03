from api.users_api import UsersAPI #Se importa la clase donde se almacenan las validaciones a la API

api = UsersAPI()

def test_post_new_user_201(): #Test para confirmar la creación de usuarios

    payload = {"email": "arte.dan@reqres.in",
      "first_name": "Daniel",
      "last_name": "Arteaga",
      "avatar": "https://reqres.in/img/faces/4-image.jpg"}

    response = api.post_new_user(payload)
    data = response.json()

    assert response.status_code == 201
    assert data["first_name"] == payload["first_name"]
    assert data["email"] == payload["email"]
    assert data["last_name"] == payload["last_name"]
    assert response.elapsed.total_seconds() < 2
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"