# https://www.hackerrank.com/challenges/introduction-to-regex
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in xrange(int(raw_input())):
    print re.match('[+-]?\d*\.\d+$', raw_input()) != None

