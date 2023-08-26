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
        self.file_repository = PhoneBookCrud(self.filename)  # Работа с файлом
        self.output_repository = OutputRepository()  # Работа с выводом
        self.fields = {1: "name", 2: "surname", 3: "patronymic", 4: "organization_name", 5: "work_phone",
                       6: "personal_phone"}  # Словарь полей

    def get_all_persons(self) -> list[str]:
        """Реализовывает постраничный вывод контактов"""
        paginate_by = 2  # Отвечает за количество записей в странице
        persons = self.file_repository.get_all()  # Получение всех контактов
        pages = ceil(len(persons) / 2)  # Подсчет количество страниц
        cur_page = 1  # Хранит текущую страницу
        start = 0  # Хранит индекс начала среза для вывода страницы
        end = start + paginate_by  # Хранит индекс конца среза для вывода страницы

        self.output_repository.print_menu_for_pages()  # Вывод меню
        self.output_repository.print_page(persons[start:end])  # Вывод страницы
        self.output_repository.print_current_page(pages, cur_page)  # Вывод номера страницы

        while True:
            user_input = input()
            if user_input == "1" and cur_page == pages:  # Попытка перехода на следующую страницу
                self.output_repository.print_end_page_notification(True)  # Вывод сообщения о конце страниц
            elif user_input == "1":  # Удачный переход на следующую страницу
                cur_page += 1  # Увеличение номера текущей страницы
                start += paginate_by  # Смещение среза
                end += paginate_by

                self.output_repository.print_page(persons[start:end])  # Вывод страницы
                self.output_repository.print_current_page(pages, cur_page)  # Вывод номера страницы

            elif user_input == "2" and cur_page == 1:  # Попытка перехода на предыдущую страницу
                self.output_repository.print_end_page_notification(False)  # Вывод сообщения о конце страниц
            elif user_input == "2":
                cur_page -= 1  # Уменьшение номера страницы
                start -= paginate_by  # Смещение среза
                end -= paginate_by

                self.output_repository.print_page(persons[start:end])  # Вывод страницы
                self.output_repository.print_current_page(pages, cur_page)  # Вывод номера страницы

            elif user_input == "0":  # Выход из цикла
                break
            else:
                self.output_repository.unknown_command()

    def add_person(self) -> str:
        """Реализовывает добавление контакта"""
        name = input("Введите имя: ")  # Получение ввода от пользователя
        surname = input("Введите фамилию: ")
        patronymic = input("Введите отчество: ")
        organization_name = input("Введите название организации: ")
        work_phone = input("Введите рабочий номер телефона: ")
        personal_phone = input("Введите личный номер телефона: ")

        self.file_repository.add(name=name, surname=surname, patronymic=patronymic,
                                 organization_name=organization_name, work_phone=work_phone,
                                 personal_phone=personal_phone)  # Добавление пользователя
        self.output_repository.print_add_success()  # Вывод информационного сообщения

    def edit_person(self) -> str:
        """Реализовывает изменение контакта"""
        self.output_repository.print_message_for_edit()  # Вывод информационного сообщения
        person = self.find_person()  # Поиск пользователя
        if person:  # Если пользователь найден
            user_input = input("Введите поля, которые хотите изменить через пробел: ")
            num_fields = [int(i) for i in user_input.split()]
            fields = [self.fields[i] for i in num_fields]
            kwargs = {}

            for i in fields:  # Создание словаря типа - {Имя поля: Пользовательский ввод}
                data = input(f"Введите {i}: ")
                kwargs[i] = data
            self.file_repository.edit(person, **kwargs)  # Изменения в файле
            self.output_repository.print_edit_success()  # Вывод сообщения

    def find_person(self) -> dict | str:
        """Основной метод для поиска контактов"""
        self.output_repository.print_menu_for_find()  # Вывод меню
        user_input = input("Характеристики поиска: ")  # Получение ввода от пользователя
        num_fields = [int(i) for i in user_input.split()]  # Создание списка с номерами полей
        fields = [self.fields[i] for i in num_fields]
        kwargs = {}

        for i in fields:  # Создание словаря типа - {Имя поля: Пользовательский ввод}
            data = input(f"Введите {i}: ")
            kwargs[i] = data

        person = self.file_repository.find(**kwargs)  # Поиск пользователя
        if person:  # Если есть пользователь, вернуть его, иначе сообщение об отсутствии пользователя
            return self.output_repository.print_person(person)
        else:
            self.output_repository.not_found()
