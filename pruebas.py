from tests.test_users import api

response = api.get_users()

data = response.json()

print(type(data))
print(data.keys())
print(data["page"])
print(data["data"][0])