from lab6.utils import read_file, write_result, write_except, print_input, print_output
import os
import math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def fibonacci(A):

    def is_fibonacci_number(number):
        """Проверка, является ли число x числом Фибоначчи"""
        x = int(number)
        # Если хотя бы одно из этих выражений является полным квадратом, то это число Фибоначчи
        return math.isqrt(5 * x * x + 4) ** 2 == 5 * x * x + 4 or math.isqrt(5 * x * x - 4) ** 2 == 5 * x * x - 4

    result = []
    for number in A:
        if is_fibonacci_number(number):
            result.append("Yes")
        else:
            result.append("No")

    return result


if __name__ == "__main__":
    n, A = read_file(FILE_INPUT_PATH, 0)
    if 1 <= n <= 10 ** 6:
        write_result(FILE_OUTPUT_PATH, fibonacci(A))
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab6 Task4---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)