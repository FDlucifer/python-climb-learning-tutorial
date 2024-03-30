import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

print(opts)
print(args)