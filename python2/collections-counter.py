# https://www.hackerrank.com/challenges/collections-counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
raw_input()
c = Counter([int(i) for i in raw_input().split()])
total = 0
for _ in xrange(int(raw_input())):
    size, money = [int(i) for i in raw_input().split()]
    if c[size] > 0:
        c[size] -= 1
        total += money
print(total)
