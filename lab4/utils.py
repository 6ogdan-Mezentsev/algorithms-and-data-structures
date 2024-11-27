import time
from memory_profiler import memory_usage


def read_file(file_input_path, start_line=0):
    with open(file_input_path, 'r') as file:
        n = int(file.readline().strip())
        A = [file.readline().strip() for _ in range(n)]
        return n, A


def write_result(file_output_path, result, *args):
    with open(file_output_path, 'w') as file:
        if args[0] == "task3":
            file.write("\n".join(result))
        else:
            for item in result:
                file.write(f"{item}\n")


def write_except(file_output_path):
    outfile = open(file_output_path, 'w').write("Проверьте корректность введённых данных")


def count_time_and_memory(algorithm, *args, **kwargs):
    start_time = time.perf_counter()
    mem_usage_before = memory_usage()[0] * 1024

    result = algorithm(*args, **kwargs)

    mem_usage_after = memory_usage()[0] * 1024
    elapsed_time = time.perf_counter() - start_time
    memory_used = mem_usage_after - mem_usage_before

    return result, elapsed_time, memory_used


def print_input(file_input_path):
    print("input.txt:")
    with open(file_input_path, 'r') as f:
        print(f.read())


def print_output(file_output_path):
    print("output.txt:")
    with open(file_output_path, 'r') as f:
        print(f.read())
        print()






