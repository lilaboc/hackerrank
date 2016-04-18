# https://www.hackerrank.com/challenges/validating-credit-card-number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in xrange(int(raw_input())):
    line = raw_input()
    if re.match('^[456][0-9]{15}$|^[456][0-9]{3}(-[0-9]{4}){3}$', line) and not re.search('([0-9])\\1{3}', re.sub('-', '', line)):
        print 'Valid'
    else:
        print 'Invalid'

