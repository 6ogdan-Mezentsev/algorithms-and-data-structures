from lab7.utils import read_file, write_result, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def check_template(pattern, A):
    n, m = len(pattern), len(A)
    current_values = [[False] * (m + 1) for _ in range(n + 1)]
    current_values[0][0] = True  # Пустой шаблон соответствует пустой строке

    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            current_values[i][0] = current_values[i - 1][0]
        else:
            break

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == '*':
                current_values[i][j] = current_values[i - 1][j] or current_values[i][j - 1]
            elif pattern[i - 1] == '?' or pattern[i - 1] == A[j - 1]:
                current_values[i][j] = current_values[i - 1][j - 1]

    return "YES" if current_values[n][m] else "NO"


if __name__ == "__main__":
    pattern, A = read_file(FILE_INPUT_PATH, start_line=0, task='task4')
    write_result(FILE_OUTPUT_PATH, check_template(pattern, A))

    print("---Lab7 Task3---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)