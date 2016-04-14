# https://www.hackerrank.com/challenges/py-set-mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
a = set([int(i) for i in raw_input().split()])
for _ in xrange(int(raw_input())):
    cmd = raw_input().split()[0]
    b = set([int(i) for i in raw_input().split()])
    getattr(a, cmd)(b)
print(sum(a))
