from lab4.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def stack_commands(M, commands):
    """Возвращает элементы, которые были удалены из стека."""
    stack = []  # стек
    deleted_elements = []  # удалённые элементы
    for command in commands:
        if command[0] == '+':
            _, number = command.split('+')
            stack.append(int(number))  # добавление элемента в стек
        elif command == '-':
            deleted_elements.append(stack.pop())
    return deleted_elements


if __name__ == "__main__":
    M, commands = read_file(file_input_path)
    result = stack_commands(M, commands)
    if 1 <= M <= 10**6:
        write_result(file_output_path, result, 0)
    else:
        write_except(file_output_path)

    print("---Lab4 Task1---")
    print_input(file_input_path)
    print_output(file_output_path)
