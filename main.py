import json

new_peaple = {"name": "Ivan", "surname": "Petrov",
              "patronymic": "Gagov",
              "organization-name": "MacDonalds",
              "work-phone": "87-23-45",
              "personal-phone": "+7-978-657-76-54"}

to_json = json.dumps(new_peaple)

with open("data.json", "a") as file:
    data = file.write(to_json)
