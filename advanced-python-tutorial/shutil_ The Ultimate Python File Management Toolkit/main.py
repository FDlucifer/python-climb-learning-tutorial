import shutil

# shutil.copy('first.txt', 'second.txt')
# shutil.copytree('source_dir', 'destination_dir')


def ignore_specific_files(directory, files):
    return [f for f in files if f == "first.txt"]


shutil.copytree("source_dir", "destination_dir", ignore=ignore_specific_files)
shutil.move("third.txt", "source_dir/first.txt")
shutil.rmtree("source_dir")

total, sued, free = shutil.disk_usage("/")
print(total, sued, free)

shutil.chown("one.txt", user="root")
print(shutil.which('python3'))

shutil.make_archive('myarchive', 'zip', 'myfile')
shutil.unpack_archive('myarchive.zip', 'unpacked_dir')

print(shutil.get_archive_formats())
print(shutil.get_unpack_formats())

