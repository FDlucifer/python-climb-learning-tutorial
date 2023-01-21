from pathlib import *

my_folder = Path.cwd() / "my_folder"
print(my_folder)

images_dir = my_folder / "images"
images_dir.mkdir()

image1 = my_folder / "image1.png"
print(image1.exists())

destination = images_dir / "image1.png"
image1.replace(destination)
print(destination.exists())


