def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    Обробляє помилки типу KeyError, ValueError, IndexError.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Command requires exactly 2 arguments (name and phone)."
        except IndexError:
            return "Error: Invalid command format."
    return inner

def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та аргументи.

    :param user_input: Введений користувачем рядок
    :return: Кортеж з команди та аргументів
    """
    cmd, *args = user_input.split()  # Розділяє введений рядок на команду та аргументи
    cmd = cmd.strip().lower()  # Видаляє пробіли навколо команди та перетворює на нижній регістр
    return cmd, args  # Повертає команду та аргументи

@input_error
def add_contact(args, contacts):
    """
    Додає новий контакт до словника контактів.

    :param args: Список з імені та номеру телефону
    :param contacts: Словник контактів
    :return: Повідомлення про результат операції
    """
    if len(args) != 2:  # Перевіряє, чи містить args два елементи
        raise ValueError
    name, phone = args  # Розпаковує ім'я та номер телефону
    contacts[name] = phone  # Додає контакт до словника
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.

    :param args: Список з імені та нового номеру телефону
    :param contacts: Словник контактів
    :return: Повідомлення про результат операції
    """
    if len(args) != 2:  # Перевіряє, чи містить args два елементи
        raise ValueError
    name, phone = args  # Розпаковує ім'я та новий номер телефону
    if name in contacts:  # Перевіряє, чи існує контакт
        contacts[name] = phone  # Оновлює номер телефону контакту
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    """
    Показує номер телефону для заданого імені.

    :param args: Список з одного елементу - імені
    :param contacts: Словник контактів
    :return: Повідомлення про результат операції
    """
    if len(args) != 1:  # Перевіряє, чи містить args один елемент
        raise IndexError
    name = args[0]  # Отримує ім'я
    if name in contacts:  # Перевіряє, чи існує контакт
        return f"{name}: {contacts[name]}"  # Повертає ім'я та номер телефону
    else:
        raise KeyError

@input_error
def show_all(contacts):
    """
    Показує всі збережені контакти.

    :param contacts: Словник контактів
    :return: Повідомлення з усіма контактами
    """
    if contacts:  # Перевіряє, чи є контакти
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())  # Повертає всі контакти
    else:
        return "No contacts found."

def main():
    """
    Основна функція програми, що управляє основним циклом обробки команд.
    """
    contacts = {}  # Ініціалізує словник контактів
    print("Welcome to the assistant bot!")  # Виводить привітання
    while True:
        user_input = input("Enter a command: ").strip()  # Отримує команду від користувача
        command, args = parse_input(user_input)  # Розбирає команду на команду та аргументи

        if command in ["close", "exit"]:  # Перевіряє, чи потрібно завершити роботу
            print("Good bye!")  # Виводить прощання
            break  # Завершує цикл
        elif command == "hello":  # Перевіряє команду "hello"
            print("How can I help you?")  # Виводить відповідь
        elif command == "add":  # Перевіряє команду "add"
            print(add_contact(args, contacts))  # Додає контакт та виводить результат
        elif command == "change":  # Перевіряє команду "change"
            print(change_contact(args, contacts))  # Змінює контакт та виводить результат
        elif command == "phone":  # Перевіряє команду "phone"
            print(show_phone(args, contacts))  # Показує номер телефону та виводить результат
        elif command == "all":  # Перевіряє команду "all"
            print(show_all(contacts))  # Показує всі контакти та виводить результат
        else:
            print("Invalid command.")  # Виводить повідомлення про невідому команду

if __name__ == "__main__":
    main()  # Запускає основну функцію