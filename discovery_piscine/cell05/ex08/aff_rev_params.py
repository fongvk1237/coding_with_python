import sys

if len(sys.argv) < 3:
    print("none")
else:
    for argv in reversed(sys.argv[1:]):
        print(argv)