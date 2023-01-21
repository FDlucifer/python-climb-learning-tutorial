from pathlib import *

my_folder = Path.cwd() / "my_folder"
print(my_folder)
print(list(my_folder.iterdir()))

file1 = list(my_folder.iterdir())[0]
print(file1)
file1.unlink()

file2 = list(my_folder.iterdir())[1]
print(file2)
file2.unlink()
print(list(my_folder.iterdir()))

