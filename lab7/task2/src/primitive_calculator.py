from lab7.utils import read_file, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def primitive_calculator(n):
    count_operation = [0] * (n + 1)  # массив для хранения минимального количества операций
    previous_element = [0] * (n + 1)  # массив для хранения предыдущего числа в последовательности

    for i in range(2, n + 1):
        count_operation[i] = count_operation[i - 1] + 1
        previous_element[i] = i - 1

        if i % 2 == 0 and count_operation[i // 2] + 1 < count_operation[i]:
            count_operation[i] = count_operation[i // 2] + 1
            previous_element[i] = i // 2

        if i % 3 == 0 and count_operation[i // 3] + 1 < count_operation[i]:
            count_operation[i] = count_operation[i // 3] + 1
            previous_element[i] = i // 3

    sequence = []
    while n > 0:
        sequence.append(n)
        n = previous_element[n]

    sequence.reverse()
    return count_operation[-1], sequence


if __name__ == "__main__":
    n = read_file(FILE_INPUT_PATH, start_line=0, task='task2')
    if 1 <= n <= 10 ** 6:
        min_operations, sequence = primitive_calculator(n)
        with open(FILE_OUTPUT_PATH, "w") as file:
            file.write(f"{min_operations}\n")
            file.write(" ".join(map(str, sequence)) + "\n")
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab7 Task2---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)

