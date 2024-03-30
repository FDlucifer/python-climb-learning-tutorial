import filelock

lock = filelock.FileLock('counter.lock')

for _ in range(100):
    with lock:
        with open('counter.txt', 'r') as f:
            current = int(f.read())

        current += 1

        with open('counter.txt', 'w') as f:
            f.write(str(current))

