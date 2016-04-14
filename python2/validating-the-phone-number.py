# https://www.hackerrank.com/challenges/validating-the-phone-number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in xrange(int(raw_input())):
    if re.match('[789]\d{9}$', raw_input()):
        print 'YES'
    else:
        print 'NO'
