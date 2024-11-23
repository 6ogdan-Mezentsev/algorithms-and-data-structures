from lab4.utils import read_file, write_result, write_except, print_input, print_output
from collections import deque
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def queue_commands_min(M, commands):
    """Возвращает элементы текущей очереди и мимнимальный элемент"""
    queue = deque()  # основаная очередь
    current_queue = []  # очередь для хранения текущего результата
    min_queue = []  # очередь для хранения минимального элемента

    for command in commands:
        if command[0] == '+':
            _, number = command.split("+")
            number = int(number)
            queue.append(number)  # Добавляем число в очередь

            while min_queue and min_queue[-1] > number:  # Обновляем очередь минимальных элементов
                min_queue.pop()
            min_queue.append(number)

        elif command == '-':
            if queue:
                removed = queue.popleft()  # Удаляем элемент из начала очереди
                if removed == min_queue[0]:
                    min_queue.pop(0)

        elif command == "?":
            if min_queue:  # Запрос минимального элемент
                current_queue.append(min_queue[0])
            else:
                current_queue.append("Queue is empty")  # Случай, если очередь пуста
    return current_queue


if __name__ == "__main__":
    M, commands = read_file(file_input_path)
    if 1 <= M <= 10 ** 6:
        result = queue_commands_min(M, commands)
        write_result(file_output_path, result, 0)
    else:
        write_except(file_output_path)

    print("---Lab4 Task4---")
    print_input(file_input_path)
    print_output(file_output_path)