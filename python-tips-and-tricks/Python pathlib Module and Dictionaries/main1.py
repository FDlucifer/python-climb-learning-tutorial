from pathlib import *

print(Path.cwd())

print(Path.home() / 'python' / 'scripts' / 'test.py')
print(Path.home().joinpath('python' , 'scripts' , 'test.py'))

path = Path.cwd() / 'test.md'
with open(path, mode='r', encoding="utf-8") as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]

print('\n'.join(headers))
print(Path.read_text())
print(Path.resolve())
print(Path.resolve().parent == Path.cwd())
