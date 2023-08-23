from math import ceil

from crud import PhoneBookCrud
from utils import PhoneBookBase


class PhoneBookService(PhoneBookBase):
    """
    Данный класс принимает пользовательский ввод и отправляет его в PhoneBookCrud,
    А так же обрабатывает вывод PhoneBookCrud
    """

    def __init__(self, filename: str, repository: PhoneBookCrud):
        super().__init__(filename)
        self.repository = repository

    @staticmethod
    def print_menu():
        print("Для просмотра следующей страницы введите n: ")
        print("Для просмотра предыдущей страницы введите p: ")
        print("Для выхода введите E: ")

    def get_all_persons(self) -> list[str]:  # todo вынести в 2 слоя
        paginate_by = 2
        persons = self.repository.get_all(self)
        pages = ceil(len(persons) / 2)
        cur_page = 1
        start = 0
        end = start + paginate_by
        for i in persons[start:end]:
            for key, value in i.items():
                print("{0}: {1}".format(key, value))
            print("***********************************************")
        self.print_menu()
        print(f"Страница {cur_page}/{pages}")

        while True:
            user_input = input()  # Todo debug
            if user_input == "n" and cur_page == pages:
                print("Нет следующей страницы")
            elif user_input == "n":
                cur_page += 1
                start += paginate_by
                end += paginate_by
                for i in persons[start:end]:
                    for key, value in i.items():
                        print("{0}: {1}".format(key, value))
                    print("***********************************************")
                print(f"Страница {cur_page}/{pages}")

            elif user_input == "p" and cur_page == 1:
                print("Нет предыдущей страницы")
            elif user_input == "p":
                cur_page -= 1
                start -= paginate_by
                end -= paginate_by
                for i in persons[start:end]:
                    for key, value in i.items():
                        print("{0}: {1}".format(key, value))
                    print("***********************************************")
                print(f"Страница {cur_page}/{pages}")

            elif user_input == "e":
                break

    def add_person(self) -> str:

        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        patronymic = input("Введите отчество: ")
        organization_name = input("Введите название организации: ")
        work_phone = input("Введите рабочий номер телефона: ")
        personal_phone = input("Введите личный номер телефона: ")

        self.repository.add(self, name, surname, patronymic, organization_name, work_phone, personal_phone)
        return "Запись добавлена"

    def edit_person(self):  # проверка на уникальность
        pass

    def find_person(self):
        pass
