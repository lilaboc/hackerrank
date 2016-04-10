# https://www.hackerrank.com/challenges/sets
# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
a = set([int(i) for i in raw_input().split()])
raw_input()
b = set([int(i) for i in raw_input().split()])
for i in sorted(a.difference( b).union(  b.difference(a))):
    print(i)
