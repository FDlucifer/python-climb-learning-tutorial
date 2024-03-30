class FileStream:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.filestream = open(self.path, self.mode)
        return self.filestream

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.filestream.close()

with FileStream("file.txt", "w") as f:
    f.write("other text")

print(f.closed)