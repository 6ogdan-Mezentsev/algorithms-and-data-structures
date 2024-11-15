import psutil
import os
import time


def read_file(file_input_path, start_line=0):
    with open(file_input_path, 'r') as file:
            lines = file.readlines()
            n = int(lines[start_line].strip())
            A = [int(num) for num in lines[start_line + 1].strip().split()]
            return n, A


def write_result(file_output_path, result):
    outfile = open(file_output_path, 'w').write(result)


def write_except(file_output_path):
    outfile = open(file_output_path, 'w').write("Проверьте корректность введённых данных")


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024
    # Возвращает использование памяти в мегабайтах


def count_time_and_memory(algorithm, *args, **kwargs):
    start_time = time.perf_counter()
    start_memory = get_memory_usage()

    result = algorithm(*args, **kwargs)

    end_time = time.perf_counter()
    end_memory = get_memory_usage()
    elapsed_time = end_time - start_time
    memory_used = end_memory - start_memory

    return result, elapsed_time, memory_used






