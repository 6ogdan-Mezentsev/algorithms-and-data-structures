from lab2.utils import read_file, write_result, write_except, print_input, print_output
import os

file_input_path = os.path.abspath("../txtf/input.txt")
file_output_path = os.path.abspath("../txtf/output.txt")


def merge_sort_and_count(A, n):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        inv_count = merge_sort_and_count(left, n) + merge_sort_and_count(right, n)
        # i - индекс в списке left
        # j - индекс в списке right
        # k - индекс в исходном списке A
        i = j = k = 0
        while i < len(left) and j < len(right):  # рекурсивно сравниваем элементы отсортированных массивов и добаляем их в исходныый массив А
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
                inv_count += len(left) - i  # количество инверсий
            k += 1

        while j < len(right):  # если в правом массиве остались элементы, а в левом нет
            A[k] = right[j]
            j += 1
            k += 1

        while i < len(left):  # если в левом массиве остались элементы, а в правом нет
            A[k] = left[i]
            i += 1
            k += 1

        return inv_count
    else:
        return 0


if __name__ == "__main__":
    n, A = read_file(file_input_path)
    result = str(merge_sort_and_count(A, n))
    if (1 <= n <= 10 ** 5) and all(abs(x) <= 10 ** 9 for x in A):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab2 Task2---")
    print_input(file_input_path)
    print_output(file_output_path)









