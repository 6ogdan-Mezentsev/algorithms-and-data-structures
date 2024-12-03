from lab5.utils import read_file, write_result, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def check_array(n, A):
    """Проверяет, является ли массив кучей или нет"""
    A = [0] + A
    for i in range(1, n + 1):
        if 2 * i <= n and A[i] > A[2 * i]:
            return 'NO'
        if ((2 * i) + 1) <= n and A[i] > A[(2 * i) + 1]:
            return 'NO'
    return 'YES'


if __name__ == "__main__":
    n, A = read_file(FILE_INPUT_PATH)
    if (1 <= n <= 10 ** 6) and all(abs(x) <= 2 * 10 ** 9 for x in A):
        result = check_array(n, A)
        write_result(FILE_OUTPUT_PATH, result)
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab5 Task1---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)
