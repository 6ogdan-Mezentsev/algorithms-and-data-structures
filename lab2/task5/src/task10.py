from lab2.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def merge_sort_ref(A, n):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        merge_sort_ref(left, n)
        merge_sort_ref(right, n)
        # i - индекс в списке left
        # j - индекс в списке right
        # k - индекс в исходном списке A

        # Проверка, нужно ли объединять массивы в том случае, если массивы отсортированы!
        if left[-1] <= right[0]:
            A[:] = left + right

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

        return A
    else:
        return A


if __name__ == "__main__":
    n, A = read_file(file_input_path)
    result = ' '.join(map(str, merge_sort_ref(A, n)))
    if (1 <= n <= 20000) and all(abs(x) <= 10 ** 9 for x in A):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab2 Task5---")
    print_input(file_input_path)
    print_output(file_output_path)

