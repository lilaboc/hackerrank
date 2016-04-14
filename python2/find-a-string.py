# https://www.hackerrank.com/challenges/find-a-string
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
o = raw_input()
count = 0
for i in xrange(len(s) - len(o) + 1):
    if s[i: i + len(o)] == o:
        count += 1
print count
