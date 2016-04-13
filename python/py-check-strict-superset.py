# https://www.hackerrank.com/challenges/py-check-strict-superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set([int(i) for i in raw_input().split()])
result = True
for _ in xrange(int(raw_input())):
    tmp = set([int(i) for i in raw_input().split()])
    if not tmp.issubset(A) or len(tmp) == len(A):
        result = False
        break
print result
    

