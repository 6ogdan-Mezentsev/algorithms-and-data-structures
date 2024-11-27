from lab4.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def check_correct_pairs(sequence):
    """Проверяет на правильность последовательность скобок."""
    stack = []
    pairs = {')': '(', ']': '['}  # Правильное соответствие закрывающих и открывающих скобок
    for simbol in sequence:
        if simbol in "([":  # Если проверяем открывающюю скобку
            stack.append(simbol)
        elif simbol in ")]":  # Если проверяем закрывающюю скобку
            if not stack or stack[-1] != pairs[simbol]:  # Если стек пуст или есть несоответствие
                return "NO"
            stack.pop()  # Удаляем соответствующую открывающую скобку
    return "YES" if not stack else "NO"  # Если стек пуст, последовательность правильная


def main(sequences):
    """Проверяет правильность каждой последовательности."""
    return [check_correct_pairs(sequence) for sequence in sequences]


if __name__ == "__main__":
    M, sequences = read_file(file_input_path)
    if 1 <= M <= 10 ** 6:
        result = main(sequences)
        write_result(file_output_path, result, "task3")
    else:
        write_except(file_output_path)

    print("---Lab4 Task3---")
    print_input(file_input_path)
    print_output(file_output_path)
