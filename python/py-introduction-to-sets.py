# https://www.hackerrank.com/challenges/py-introduction-to-sets
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
raw_input()
s = set([int(i) for i in raw_input().split()])
print sum(s) / len(s)
