from pathlib import *

home = Path.home()
print(home)

my_folder = Path.cwd() / "my_folder"
print(my_folder)
my_folder.mkdir()
print(my_folder.exists())

file1 = my_folder / "file1.txt"
file1.touch()
(my_folder / "file2.txt").touch()
my_folder.joinpath("image1.png").touch()

