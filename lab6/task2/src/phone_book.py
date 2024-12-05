from lab6.utils import read_file, write_result, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def phone_book_commands(A):
    """Выполняет операции с 'телефонной книгой' и возвращает """
    phonebook = {}
    results = []

    for query in A:
        parts = query.split()
        command = parts[0]
        number = parts[1]

        if command == "add":
            name = parts[2]
            phonebook[number] = name  # Добавление номера
        elif command == "del":
            phonebook.pop(number, None)  # Удаление номера
        elif command == "find":
            results.append(phonebook.get(number, "not found"))  # Поиск номера

    return results


if __name__ == "__main__":
    n, A = read_file(FILE_INPUT_PATH, 0, 'task2')
    if 1 <= n <= 10 ** 5:
        write_result(FILE_OUTPUT_PATH, phone_book_commands(A))
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab6 Task2---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)

