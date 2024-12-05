from lab6.utils import read_file, write_result, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def set_commands(A):
    """Выполняет операции для множества и проверяет наличие элемента в этом множестве"""
    set_num = set()
    res = []

    for operation, x in A:
        if operation == 'A':
            set_num.add(x)
        elif operation == 'D':
            set_num.discard(x)
        elif operation == '?':
            res.append('Y' if x in set_num else 'N')

    return res


if __name__ == "__main__":
    n, A = read_file(FILE_INPUT_PATH, 0, 'task1')
    if 1 <= n <= 5 * (10 ** 5):
        write_result(FILE_OUTPUT_PATH, set_commands(A))
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab6 Task1---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)