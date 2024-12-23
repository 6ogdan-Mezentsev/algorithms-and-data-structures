from lab7.utils import read_file, write_result, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def edit_distance(s1, s2):
    """Находит редакционное расстояние"""
    n, m = len(s1), len(s2)
    temp_values = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        temp_values[i][0] = i  # Удаление всех символов str1
    for j in range(m + 1):
        temp_values[0][j] = j  # Вставка всех символов str2

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                temp_values[i][j] = temp_values[i - 1][j - 1]
            else:
                temp_values[i][j] = 1 + min(temp_values[i - 1][j],
                                            temp_values[i][j - 1],
                                            temp_values[i - 1][j - 1])

    return temp_values[n][m]


if __name__ == "__main__":
    s1, s2 = read_file(FILE_INPUT_PATH, start_line=0, task='task3')
    write_result(FILE_OUTPUT_PATH, str(edit_distance(s1, s2)))

    print("---Lab7 Task3---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)
