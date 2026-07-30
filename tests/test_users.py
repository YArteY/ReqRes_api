from api.users_api import UsersAPI #Se importa la clase donde se almacenan las validaciones a la API

api = UsersAPI()
#Creación de los test
def test_get_users_200():#Test para extraer un usuario desde una ruta page
    response = api.get_users(2) #le indicamos la pagina a la que debe buscar
    data = response.json()
    user = data['data'][0]
    assert response.status_code == 200
    assert "data" in data
    assert "id" in user
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert "avatar" in user
    assert isinstance(user["id"], int)
    assert isinstance(user["email"], str)
    assert isinstance(user["first_name"], str)
    assert response.elapsed.total_seconds() < 2
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_get_specific_user_200(): #Test para conseguir un usuario directamente con su ID.
    response = api.get_specific_user(1)
    data = response.json()
    user = data['data']
    print(response.json())
    assert response.status_code == 200
    assert "data" in data
    assert "id" in user
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert "avatar" in user
    assert user["id"] == 1
    assert isinstance(user["id"], int)
    assert isinstance(user["email"], str)
    assert isinstance(user["first_name"], str)
    assert response.elapsed.total_seconds() < 2
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_post_new_user(): #Test para confirmar la creación de usuarios
    payload = {"email": "arte.dan@reqres.in",
      "first_name": "Daniel",
      "last_name": "Arteaga",
      "avatar": "https://reqres.in/img/faces/4-image.jpg"}
    response = api.post_new_user(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["first_name"] == payload["first_name"]
    assert data["email"] == payload["email"]
    assert data["last_name"] == payload["last_name"]
    assert response.elapsed.total_seconds() < 2
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
