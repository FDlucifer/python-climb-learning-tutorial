with open('photo.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('ffd9'))

    f.seek(offset + 2)
    print(f.read())