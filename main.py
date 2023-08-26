from main_service import PhoneBookService
from output_repository import OutputRepository


def main() -> None:
    """Запускает основной цикл программы"""
    OutputRepository.print_main_menu()
    service = PhoneBookService("example.json")
    while True:
        user_input = int(input())
        if user_input == 1:  # Постраничный вывод
            service.get_all_persons()
            main()  # После выполнения метода -> возврат в основной цикл
        elif user_input == 2:  # Добавление записи
            service.add_person()
            main()
        elif user_input == 3:  # Редактирование записи
            service.edit_person()
            main()
        elif user_input == 4:  # Поиск записи
            service.find_person()
            main()
        elif user_input == 0:  # Выход из цикла
            break
        else:
            print("Неизвестная команда")


if __name__ == '__main__':
    main()
