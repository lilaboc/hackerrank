# https://www.hackerrank.com/challenges/python-lists
# Enter your code here. Read input from STDIN. Print output to STDOUT
l = []
for i in xrange(int(raw_input())):
    command = raw_input().split()
    if hasattr(l, command[0]):
        getattr(l, command[0])(*[int(i) for i in command[1:]])
    else:
        print(l)
