import json

from utils import PhoneBookBase


class PhoneBookCrud(PhoneBookBase):
    """
    Данный класс выполняет операции с json файлом
    """

    def get_all(self) -> list[dict]:
        with open(self.filename, "r") as file:
            data = json.load(file)
        return data

    def add(self, **kwargs) -> None:
        with open(self.filename, 'r') as pre_file:  # Чтение файла
            old_data = json.load(pre_file)  # Десериализация из json в list[dict]

        new_person = {"name": kwargs["name"],
                      "surname": kwargs["surname"],
                      "patronymic": kwargs["patronymic"],
                      "organization-name": kwargs["organization_name"],
                      "work-phone": kwargs["work_phone"],
                      "personal-phone": kwargs["personal_phone"]}
        old_data.append(new_person)

        with open(self.filename, "w") as post_file:
            json.dump(old_data, post_file)  # Сериализация в json

    def find(self, **kwargs) -> dict | None:
        with open(self.filename, "r") as file:
            data = json.load(file)
        for i in data:
            for key, value in kwargs.items():
                if i[key] == value:
                    return i
                else:
                    return None

    def edit(self, person: dict, **kwargs) -> str:
        with open(self.filename, "r") as file:
            data = json.load(file)
        to_edit = self.find(**person)
        to_replace = None
        for i in data:
            if i == to_edit:
                to_replace = i

        for key, value in kwargs.items():
            to_replace[key] = value

        with open(self.filename, "w") as post_file:
            json.dump(data, post_file)