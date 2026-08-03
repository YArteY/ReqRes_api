import requests
from utils.config import URL_BASE, API_KEY #Importa la URL y KEY de la API


#Configura en una clase las distintas validaciones hechas a la API con su respectivo endpoint
class UsersAPI:

#Validación del metodo GET
    def get_users(self, page): #Este metodo validara una pagina que contiene distintos usuarios
        headers = {
            "x-api-key": API_KEY
        }
        response = requests.get(
            f"{URL_BASE}/api/users?page={page}",#Configura el endpoint
            headers= headers
        )
        return response

    def get_specific_user(self, user_id):
        headers = {
            "x-api-key": API_KEY
        }
        response = requests.get(
            f"{URL_BASE}/api/users/{user_id}",
            headers=headers
        )
        return response

#Validación del metodo POST
    def post_new_user(self, payload): #usa payload como argumento para generar el body en json
        headers = {
            "x-api-key": API_KEY
        }
        response = requests.post(
        f"{URL_BASE}/api/users",
        headers=headers,
        json=payload #se utiliza el argumento payload y se convierte a json
        )
        return response

#Validación del metodo PUT
    def put_user(self, user_id, payload):
        headers = {
            "x-api-key": API_KEY
        }
        response = requests.put(
            f"{URL_BASE}/api/users/{user_id}",
            headers=headers,
            json=payload
        )
        return response

#Validación del metodo PATCH
    def patch_user(self, user_id, payload):
        headers = {
            "x-api-key": API_KEY
        }
        response = requests.patch(
            f"{URL_BASE}/api/users/{user_id}",
            headers=headers,
            json=payload
        )
        return response

#Validación del metodo DELETE

    def delete_user(self, user_id):
        headers = {
            "x-api-key": API_KEY
        }
        response = requests.delete(
            f"{URL_BASE}/api/users/{user_id}",
            headers=headers,
        )
        return response