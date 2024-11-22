from lab3.utils import read_file, write_result, write_except, print_input, print_output
import os

file_input_path = os.path.abspath("../txtf/input.txt")
file_output_path = os.path.abspath("../txtf/output.txt")


def hirsch_index_search(citations):
    n = len(citations)  # количество статей
    count = [0] * (n + 1)  # массив для подсчёта процетированных статей


    for citation in citations:
        if citation >= n:
            count[n] += 1  # если статья цитируется >= n раз,
                           # то добаляем её в последнюю ячейку списка count
        else:
            count[citation] += 1

    h = 0
    t = 0
    for i in range(n, -1, -1):
        t += count[i]
        if t >= i:
            h = i
            break

    return h


if __name__ == "__main__":
    citations = read_file(file_input_path, 0, 'task4')
    result = str(hirsch_index_search(citations))
    if (1 <= len(citations) <= 5000) and all(abs(x) <= 10**3 for x in citations):
        write_result(file_output_path, result)
    else:
        write_except(file_output_path)

    print("---Lab3 Task4---")
    print_input(file_input_path)
    print_output(file_output_path)
