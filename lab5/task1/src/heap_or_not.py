from lab5.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


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
    n, A = read_file(file_input_path)
    if (1 <= n <= 10 ** 6) and all(abs(x) <= 2 * 10 ** 9 for x in A):
        result = check_array(n, A)
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab5 Task1---")
    print_input(file_input_path)
    print_output(file_output_path)