from crud import PhoneBookCrud
from main_service import PhoneBookService
from output_repository import OutputRepository


def print_main_menu() -> None:
    print("1. Вывод записей из справочника")
    print("2. Добавление новой записи в справочник")
    print("3. Редактирование записей в справочнике")
    print("4. Поиск записей по характеристикам")
    print("0. Выход")


def main() -> None:
    print_main_menu()
    service = PhoneBookService("data.json")
    while True:
        user_input = int(input())
        if user_input == 1:
            service.get_all_persons()
            main()
        elif user_input == 2:
            service.add_person()
            main()
        elif user_input == 3:
            service.edit_person()
            main()
        elif user_input == 4:
            service.find_person()
            main()
        elif user_input == 0:
            break
        else:
            print("Неизвестная команда")


if __name__ == '__main__':
    main()
