from sys import argv
a = len(argv) - 1
if  a == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(a))
for i in range(a):
    print("{}: {}".format(i+1, a+1)
