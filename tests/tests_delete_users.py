from api.users_api import UsersAPI

api = UsersAPI()

#Test para comprobar la eliminación de un usuario
def test_delete_user():

    response = api.delete_user(7)

    assert response.status_code == 204
    assert response.elapsed.total_seconds() < 2
    assert response.text == ""