from lab6.utils import read_file, write_result, write_except, print_input, print_output
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/input.txt")
FILE_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../txtf/output.txt")


def count_votes(A):
    """Подсчитывает количество голосов для каждого кандидата"""
    votes = {}

    for entry in A:
        candidate, votes_count = entry.rsplit(maxsplit=1)
        votes_count = int(votes_count)

        # Добавляем голоса к уже существующему кандидату или создаем новую запись
        if candidate in votes:
            votes[candidate] += votes_count
        else:
            votes[candidate] = votes_count

    return votes


if __name__ == "__main__":
    n, A = read_file(FILE_INPUT_PATH, 0, 'task3')
    if 1 <= n <= 10 ** 5:
        votes = count_votes(A)
        result = [f"{candidate} {count}" for candidate, count in sorted(votes.items())]
        write_result(FILE_OUTPUT_PATH, result)
    else:
        write_except(FILE_OUTPUT_PATH)

    print("---Lab6 Task3---")
    print_input(FILE_INPUT_PATH)
    print_output(FILE_OUTPUT_PATH)
