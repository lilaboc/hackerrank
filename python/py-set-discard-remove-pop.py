# https://www.hackerrank.com/challenges/py-set-discard-remove-pop
# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
s = set([int(i) for i in raw_input().split()])
for i in xrange(int(raw_input())):
    cmd = raw_input().split()
    if len(cmd) == 1:
        getattr(s, cmd[0])()
    else:
        getattr(s, cmd[0])(int(cmd[1]))
print(sum(s))
