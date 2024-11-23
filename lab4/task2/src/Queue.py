from lab4.utils import read_file, write_result, write_except, print_input, print_output
from collections import deque
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def queue_commands(M, commands):
    """Возвращает элементы текущей очереди после каждой команды удаления элемента."""
    queue = deque()
    current_queue = []

    for command in commands:
        if command[0] == '+':
            _, number = command.split('+')
            queue.append(int(number))  # Добавляем число в очередь
        elif command == '-':
            if queue:
                current_queue.append(queue.popleft())  # Извлекаем элемент из начала очереди
            else:
                current_queue.append("Queue is empty")  # На случай, если очередь пуста
    return current_queue


if __name__ == "__main__":
    M, commands = read_file(file_input_path)
    result = queue_commands(M, commands)
    if 1 <= M <= 10 ** 6:
        write_result(file_output_path, result, 0)
    else:
        write_except(file_output_path)

    print("---Lab4 Task2---")
    print_input(file_input_path)
    print_output(file_output_path)