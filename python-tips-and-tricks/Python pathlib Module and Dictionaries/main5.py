from pathlib import *
import shutil

my_folder = Path.cwd() / "my_folder"
print(my_folder)
print(list(my_folder.iterdir()))
print(list(my_folder.rglob("*")))

shutil.rmtree(my_folder)
print(my_folder.exists())

