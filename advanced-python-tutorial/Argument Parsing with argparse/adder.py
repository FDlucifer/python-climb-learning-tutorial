import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument("greeting", help="the greeting message displayed")
parser.add_argument(
    "-n", "--numbers", type=float, nargs="*", help="the numbers to be added"
)
parser.add_argument(
    "-v",
    "--verbosity",
    type=int,
    choices=[0, 1, 2],
    help="determines how much info is displayed",
)
parser.add_argument("-f", "--file", type=str)
parser.add_argument("--debug", action='store_true', help="enables debug mode")


args = parser.parse_args()

if args.debug:
    start = time.perf_counter()

print(args)
print(args.numbers)

if args.verbosity is None:
    print(args.greeting)
    if args.numbers is not None:
        print(sum(args.numbers))
else:
    if args.verbosity >= 0:
        print(args.greeting)
        if args.numbers is not None:
            print(sum(args.numbers))
    if args.verbosity >= 1:
        print(args.numbers)
    if args.verbosity == 2:
        print("extra info")

if args.debug:
    end = time.perf_counter()
    print(end - start)
