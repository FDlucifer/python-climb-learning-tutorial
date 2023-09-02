import sys

print("hello world\n", end="")
sys.stdout.write("hello world\n")
sys.stderr.write("this is an error\n")

print(input())
print(sys.stdin.read())
