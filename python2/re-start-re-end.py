# https://www.hackerrank.com/challenges/re-start-re-end
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
k = raw_input()
import re
found = False
for i in re.finditer('(?=' + k + ')', s):
    print((i.start(), i.start() + len(k) - 1))
    found = True
if not found:
    print((-1, -1))
