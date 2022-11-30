from contextlib import contextmanager

@contextmanager
def filestream(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with filestream("file.txt", "w") as file:
    file.write("again another text")

print(file.closed)