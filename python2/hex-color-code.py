# https://www.hackerrank.com/challenges/hex-color-code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = ''
for i in xrange(int(raw_input())):
    s += raw_input()

for i in re.finditer('{.*?}', s):
    for o in re.finditer('#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})' ,i.group(0)):
        print o.group(0)
