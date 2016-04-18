# https://www.hackerrank.com/challenges/validating-uid
# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
import re
for _ in xrange(int(raw_input())):
    line = raw_input()
    upper = 0
    digits = 0
    fault = False
    seen = set()
    if len(line) != 10:
        print 'Invalid'
    else:
        for i in line:
            if i in seen:
                fault = True
                break
            seen.add(i)
            if i in string.uppercase:
                upper += 1
            elif i in string.digits:
                digits += 1
            elif i not in string.lowercase:
                fault = True
                break
        if fault or upper < 2 or digits < 3:
            print 'Invalid'
        else:
            print 'Valid'

