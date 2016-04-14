# https://www.hackerrank.com/challenges/python-mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
pos, c = raw_input().split()
print(s[:int(pos)] + c + s[int(pos) + 1:])
