from lab2.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def binary_search(value, lst):
    left = 0
    right = len(lst) - 1
    mid = len(lst) // 2

    while lst[mid] != value and left <= right:
        if value > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    if left > right:
        return -1
    else:
        return mid


if __name__ == "__main__":
    answer = []
    n, A = read_file(file_input_path)
    k, B = read_file(file_input_path, 2)
    for i in B:
        answer.append(binary_search(i, A))
    result = ' '.join(map(str, answer))
    if 1 <= n <= 10**5 and all(abs(x) <= 10**9 for x in A):
        if 1 <= k <= 10 ** 5 and all(abs(x) <= 10 ** 9 for x in B):
            write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab2 Task4---")
    print_input(file_input_path)
    print_output(file_output_path)





