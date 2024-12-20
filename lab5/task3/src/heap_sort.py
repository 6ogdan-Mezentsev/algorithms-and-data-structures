from lab5.utils import read_file, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def create_heap(n, A):

    swaps = []  # массив с перестановками

    def min_heap(i):
        min_index = i
        left = 2 * i + 1  # Левый ребенок
        right = 2 * i + 2  # Правый ребенок

        if left < n and A[left] < A[min_index]:
            min_index = left
        if right < n and A[right] < A[min_index]:
            min_index = right

        # Если ребенок меньше текущего узла, то меняем их местами
        if i != min_index:
            A[i], A[min_index] = A[min_index], A[i]
            swaps.append((i, min_index))
            min_heap(min_index)

    for i in range(n // 2 - 1, -1, -1):
        min_heap(i)

    return swaps


if __name__ == "__main__":
    n, A = read_file(FILE_INPUT_PATH)
    if (1 <= n <= 10 ** 5) and all(abs(x) <= 10 ** 9 for x in A):
        swaps = create_heap(n, A)
        with open(FILE_OUTPUT_PATH, "w") as f:
            f.write(f"{len(swaps)}\n")
            for i, j in swaps:
                f.write(f"{i} {j}\n")
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab5 Task3---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)
