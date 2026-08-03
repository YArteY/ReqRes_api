from api.users_api import UsersAPI #Se importa la clase donde se almacenan las validaciones a la API

api = UsersAPI()

#Test para comprobar la modificación completa de datos de un usuario
def test_update_user():

    payload = {"email": "esteban.dan@reqres.in",
      "first_name": "Esteban",
      "last_name": "Villamil",
      "avatar": ""}

    response = api.put_user(2,payload)
    data = response.json()

    assert response.status_code == 200
    assert data["email"] == payload["email"]
    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["avatar"] == payload["avatar"]
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert "updatedAt" in data
    assert response.elapsed.total_seconds() < 2

#Test para comprobar la modificación parcial de datos de un usuario
def test_partially_update_user():
    payload = {"email": "estebandido@fakemail.com",}

    response = api.patch_user(2,payload)
    data = response.json()

    assert response.status_code == 200
    assert data["email"] == payload["email"]
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert "updatedAt" in data
    assert response.elapsed.total_seconds() < 2
