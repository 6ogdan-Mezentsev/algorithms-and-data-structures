import time
from memory_profiler import memory_usage


def read_file(FILE_INPUT_PATH, start_line=0):
    with open(FILE_INPUT_PATH, 'r') as file:
            lines = file.readlines()
            n = int(lines[start_line].strip())
            A = [int(num) for num in lines[start_line + 1].strip().split()]
            return n, A


def write_result(FILE_OUTPUT_PATH, result):
    outfile = open(FILE_OUTPUT_PATH, 'w').write(result)


def write_except(FILE_OUTPUT_PATH):
    outfile = open(FILE_OUTPUT_PATH, 'w').write("Проверьте корректность введённых данных")


def count_time_and_memory(algorithm, *args, **kwargs):
    start_time = time.perf_counter()
    mem_usage_before = memory_usage()[0] * 1024

    result = algorithm(*args, **kwargs)

    mem_usage_after = memory_usage()[0] * 1024
    elapsed_time = time.perf_counter() - start_time
    memory_used = mem_usage_after - mem_usage_before

    return result, elapsed_time, memory_used


def print_input(FILE_INPUT_PATH):
    print("input.txt:")
    with open(FILE_INPUT_PATH, 'r') as f:
        print(f.read())


def print_output(FILE_OUTPUT_PATH):
    print("output.txt:")
    with open(FILE_OUTPUT_PATH, 'r') as f:
        print(f.read())
        print()
