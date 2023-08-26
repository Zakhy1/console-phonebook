class OutputRepository:
    """Класс занимается выводом в консоль"""
    @staticmethod
    def print_menu_for_pages():
        print("Для просмотра следующей страницы введите 1: ")
        print("Для просмотра предыдущей страницы введите 2: ")
        print("Для выхода введите 0: ")

    @staticmethod
    def print_menu_for_find():
        print("1. Имя")
        print("2. Фамилия")
        print("3. Отчество")
        print("4. Название организации")
        print("5. Рабочий номер телефона")
        print("6. Личный номер телефона\n")
        print("Для поиска выберите соответсвующее поля, перечислив их через пробел")

    @staticmethod
    def print_page(page):
        for i in page:
            for key, value in i.items():
                print("{0}: {1}".format(key, value))
            print("***********************************************")

    @staticmethod
    def print_current_page(pages: int, cur_page: int):
        print(f"Страница {cur_page}/{pages}")

    @staticmethod
    def print_end_page_notification(is_no_next: bool):
        if is_no_next:
            print("Нет следующей страницы")
        else:
            print("Нет предыдущей страницы")

    @staticmethod
    def print_add_success():
        print("Запись добавлена")

    @staticmethod
    def print_person(person: dict):
        for key, value in person.items():
            print("{0}: {1}".format(key, value))
        return person

    @staticmethod
    def print_message_for_edit():
        print("Для изменения записи необходимо ввести характеристики поиска")

    @staticmethod
    def not_found():
        print("Запись не найдена")

    @staticmethod
    def print_edit_success():
        print("Запись изменена")

    @staticmethod
    def unknown_command():
        print("Неизвестная команда")

    @staticmethod
    def print_main_menu() -> None:
        """Выводит главное меню"""
        print("1. Вывод записей из справочника")
        print("2. Добавление новой записи в справочник")
        print("3. Редактирование записей в справочнике")
        print("4. Поиск записей по характеристикам")
        print("0. Выход")
