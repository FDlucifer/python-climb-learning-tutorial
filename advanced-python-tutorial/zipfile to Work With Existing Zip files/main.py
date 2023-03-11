import zipfile
import datetime

with zipfile.ZipFile("sample.zip", mode="r") as archive:
    archive.printdir()
    for line in archive.read("hello.txt", pwd=b"secret").split(b"\n"):
        print(line)

with zipfile.ZipFile("sample.zip", mode="r") as archive:
    for info in archive.infolist():
        print(f"filename: {info.filename}")
        print(f"modified: {datetime.datetime(*info.date_time)}")
        print(f"normal size: {info.file_size} bytes")
        print(f"compressed size: {info.compress_size} bytes")
        print("-" * 20)

with zipfile.ZipFile("sample_pwd.zip", mode="r") as archive:
    archive.setpassword(b"secret")
    for file in archive.namelist():
        print(file)
        print("-" * 20)
        for line in archive.read(file).split(b"\n"):
            print(line)


