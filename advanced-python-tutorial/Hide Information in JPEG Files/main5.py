with open('photo.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    with open('file_from_photo.exe', 'wb') as e:
        e.write(f.read())