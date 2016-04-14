# https://www.hackerrank.com/challenges/finding-the-percentage
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
marks = {}
for i in xrange(int(raw_input())):
    columns = raw_input().split()
    marks[columns[0]] = sum([float(i) for i in columns[1:]]) / 3
print('{0:.2f}'.format(marks[raw_input()]))

