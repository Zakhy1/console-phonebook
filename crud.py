import json

from utils import PhoneBookBase


class PhoneBookCrud(PhoneBookBase):
    """
    Данный класс выполняет операции с json файлом
    """

    def get_all(self) -> list[dict]:
        """Возвращает список из словарей, содержащий контакты"""
        with open(self.filename, "r") as file:  # Чтение файла
            data = json.load(file)  # Десериализация из json в list[dict]
        return data

    def add(self, **kwargs) -> None:
        """Добавляет новую запись в файл используя kwargs"""
        with open(self.filename, 'r') as pre_file:  # Чтение файла
            old_data = json.load(pre_file)  # Десериализация из json в list[dict]

        new_person = {"name": kwargs["name"],
                      "surname": kwargs["surname"],
                      "patronymic": kwargs["patronymic"],
                      "organization-name": kwargs["organization_name"],
                      "work-phone": kwargs["work_phone"],
                      "personal-phone": kwargs["personal_phone"]}
        old_data.append(new_person)  # Добавление данных

        with open(self.filename, "w") as post_file:
            json.dump(old_data, post_file)  # Сериализация в json

    def find(self, **kwargs) -> dict | None:
        """Ищет совпадения в файле используя kwargs"""
        with open(self.filename, "r") as file:  # Чтение файла
            data = json.load(file)

        for i in data:  # Проход по list[dict]
            for key, value in kwargs.items():  # Проход по kwargs
                if i[key] == value:  # Если dict и kwargs пересекаются, то вернуть i
                    return i
                else:
                    return None

    def edit(self, person: dict, **kwargs) -> str:
        """Использует метод find при поиске записи, для дальнейшего ее изменения"""
        with open(self.filename, "r") as file:  # Чтение файла
            data = json.load(file)  # Десериализация из json в list[dict]

        to_edit = self.find(**person)  # Происходит поиск по характеристикам с целью найти запись для изменения
        to_replace = None  # Объект в файле, который будет редактироваться
        for i in data:  # Проход по list[dict]
            if i == to_edit:  # Если запись в файле == записи найденной с помощью поиска, то его нужно будет изменить
                to_replace = i

        for key, value in kwargs.items():  # Замена данных в записи
            to_replace[key] = value

        with open(self.filename, "w") as post_file:  # Запись в файл
            json.dump(data, post_file)
