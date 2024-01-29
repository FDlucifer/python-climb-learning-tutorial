# pip install memory-profiler

from memory_profiler import profile, memory_usage

log_file = open("memory.log", "w+")


@profile(stream=log_file)
def myfunction(list_size):
    mylist = ["hello"] * list_size
    mylist2 = ["world"] * list_size
    del mylist2
    return mylist


myfunction(1000000)
# mem_usage = memory_usage((myfunction, (), {'list_size': 1000000}), max_usage=True)
# print(mem_usage)
