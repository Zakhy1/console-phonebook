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

    def add(self, name: str, surname: str, patronymic: str, organization_name: str, work_phone: str,
            personal_phone: str) -> None:
        with open(self.filename, 'r') as pre_file:  # Чтение файла
            old_data = json.load(pre_file)  # Десериализация из json в list[dict]

        new_person = {"name": name,
                      "surname": surname,
                      "patronymic": patronymic,
                      "organization-name": organization_name,
                      "work-phone": work_phone,
                      "personal-phone": personal_phone}
        old_data.append(new_person)

        with open(self.filename, "w") as post_file:
            json.dump(old_data, post_file)  # Сериализация в json

    def edit(self):
        pass

    def find(self):
        pass
