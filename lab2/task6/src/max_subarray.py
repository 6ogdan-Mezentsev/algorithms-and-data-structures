import random
from lab2.utils import read_file, write_result, write_except, print_input, print_output
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_input_path = os.path.join(script_dir, "../txtf/input.txt")
file_output_path = os.path.join(script_dir, "../txtf/output.txt")


def search_max_subarray(A):
    max_current = max_global = A[0]

    for i in range(1, len(A)):
        max_current = max(A[i], max_current + A[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


if __name__ == "__main__":
    n, A = read_file(file_input_path)
    write_result(file_output_path, str(search_max_subarray(A)))

    print("---Lab2 Task6---")
    print_input(file_input_path)
    print_output(file_output_path)
