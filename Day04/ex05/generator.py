import sys
import os
import psutil

def  read_file(path: str):
    with open(path, 'r') as fin:
        if not os.access(path, os.R_OK):
            raise OSError("Can't open file")
        tmp_line = "temporary"
        while tmp_line:
            tmp_line = fin.readline()
            yield tmp_line

def main(path: str):
    for line in read_file(path):
        pass
    
    usage = psutil.Process()
    print(f'Peak memory usage= {usage.memory_info().rss / 1073741824} GB')
    print(f'User Mode Time + System Mode Time = {usage.cpu_times().user + usage.cpu_times().system}s')
    
if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            main(sys.argv[1])
        else:
            raise Exception("Wrong quantity of args!")
    except Exception as err:
        print(err)