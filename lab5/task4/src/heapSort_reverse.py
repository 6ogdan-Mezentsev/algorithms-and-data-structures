from lab5.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


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
    n, A = read_file(file_input_path)
    if (1 <= n <= 10 ** 5) and all(abs(x) <= 10 ** 9 for x in A):
        result = " ".join(map(str, heap_sort_reverse(n, A)))
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab5 Task4---")
    print_input(file_input_path)
    print_output(file_output_path)

