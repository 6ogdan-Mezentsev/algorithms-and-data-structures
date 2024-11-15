import random
from lab1.utils import read_file
from lab1.utils import write_result
from lab1.utils import write_except

file_input_path = '../txtf/input.txt'
file_output_path = '../txtf/output.txt'


def selection_sort(S, n):
    for i in range(0, len(S) - 1):
        M = S[i]
        p = i
        for j in range(i+1, len(S)):
            if M > S[j]:
                M = S[j]
                p = j

        if p != i:
            k = S[i]
            S[i] = S[p]
            S[p] = k
    return S


if __name__ == "__main__":
    # generate test array and writing it to input.txt
    random_numbers = [random.randint(0, 1000000000) for _ in range(1000)]
    lines = [f'{len(random_numbers)}\n', ' '.join(map(str, random_numbers))]
    file = open('../txtf/input.txt', 'w')
    file.writelines(lines)

    n, S = read_file(file_input_path)
    result = ' '.join(map(str, selection_sort(S, n)))
    if (1 <= n <= 10**3) and all(abs(int(x)) <= 10**9 for x in S):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

