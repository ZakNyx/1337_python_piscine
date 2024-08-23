import sys


n = len(sys.argv)

if n == 1:
    sys.exit()
assert n == 2, "more than one argument is provided"

try :
    value = int(sys.argv[1])
except ValueError:
    raise AssertionError("argument is not an integer")

if (value % 2) == 0:
    print ("I'm Even")
else:
    print("I'm Odd")