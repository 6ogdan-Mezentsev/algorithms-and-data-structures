from lab5.utils import read_file, write_result, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def heapify(A, n, i):
    """Построение max-heap для каждого поддерева"""
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] > A[root]:
        root = left
    if right < n and A[right] > A[root]:
        root = right

    if root != i:
        A[i], A[root] = A[root], A[i]
        heapify(A, n, root)


def heap_sort_reverse(n, A):
    """Пирамидальная сортировка в убывающем порядке"""

    # Построение max-heap для каждого корня i
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    # Извлечение элементов из кучи в порядке убывания
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

    # Перестановка элементов в убывающем порядке
    for i in range(n // 2):
        A[i], A[n - 1 - i] = A[n - 1 - i], A[i]

    return A


if __name__ == "__main__":
    n, A = read_file(FILE_INPUT_PATH)
    if (1 <= n <= 10 ** 5) and all(abs(x) <= 10 ** 9 for x in A):
        result = " ".join(map(str, heap_sort_reverse(n, A)))
        write_result(FILE_OUTPUT_PATH, result)
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab5 Task4---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)
