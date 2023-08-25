from math import ceil

from crud import PhoneBookCrud
from output_repository import OutputRepository
from utils import PhoneBookBase


class PhoneBookService(PhoneBookBase):
    """
    Данный класс принимает пользовательский ввод и отправляет его в PhoneBookCrud,
    А так же обрабатывает вывод PhoneBookCrud
    """

    def __init__(self, filename: str):
        super().__init__(filename)
        self.file_repository = PhoneBookCrud(self.filename)
        self.output_repository = OutputRepository()
        self.fields = {1: "name", 2: "surname", 3: "patronymic", 4: "organization_name", 5: "work_phone",
                       6: "personal_phone"}

    def get_all_persons(self) -> list[str]:  # todo test 2 layers
        paginate_by = 2
        persons = self.file_repository.get_all()
        pages = ceil(len(persons) / 2)
        cur_page = 1
        start = 0
        end = start + paginate_by

        self.output_repository.print_menu_for_pages()
        self.output_repository.print_page(persons[start:end])
        self.output_repository.print_current_page(pages, cur_page)

        while True:
            user_input = input()
            if user_input == "1" and cur_page == pages:
                self.output_repository.print_end_page_notification(True)
            elif user_input == "1":
                cur_page += 1
                start += paginate_by
                end += paginate_by

                self.output_repository.print_page(persons[start:end])
                self.output_repository.print_current_page(pages, cur_page)

            elif user_input == "2" and cur_page == 1:
                self.output_repository.print_end_page_notification(False)
            elif user_input == "2":
                cur_page -= 1
                start -= paginate_by
                end -= paginate_by

                self.output_repository.print_page(persons[start:end])
                self.output_repository.print_current_page(pages, cur_page)

            elif user_input == "0":
                break
            else:
                self.output_repository.unknown_command()

    def add_person(self) -> str:

        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        patronymic = input("Введите отчество: ")
        organization_name = input("Введите название организации: ")
        work_phone = input("Введите рабочий номер телефона: ")
        personal_phone = input("Введите личный номер телефона: ")

        self.file_repository.add(name=name, surname=surname, patronymic=patronymic,
                                 organization_name=organization_name, work_phone=work_phone,
                                 personal_phone=personal_phone)
        self.output_repository.print_add_success()

    def edit_person(self) -> str:
        self.output_repository.print_message_for_edit()
        person = self.find_person()
        if person:
            user_input = input("Введите поля, которые хотите изменить через пробел: ")
            num_fields = [int(i) for i in user_input.split()]  # todo вынести в отдельный метод
            fields = [self.fields[i] for i in num_fields]
            kwargs = {}

            for i in fields:
                data = input(f"Введите {i}: ")
                kwargs[i] = data
            self.file_repository.edit(person, **kwargs)
            self.output_repository.print_edit_sucess()

    def find_and_print_person(self) -> None:
        person = self.find_person()
        self.output_repository.print_person(person)

    def find_person(self) -> dict | str:
        self.output_repository.print_menu_for_find()
        user_input = input("Характеристики поиска: ")
        num_fields = [int(i) for i in user_input.split()]  # todo вынести в отдельный метод
        fields = [self.fields[i] for i in num_fields]
        kwargs = {}

        for i in fields:
            data = input(f"Введите {i}: ")
            kwargs[i] = data

        person = self.file_repository.find(**kwargs)
        if person:
            return self.output_repository.print_person(person)
        else:
            self.output_repository.not_found()
