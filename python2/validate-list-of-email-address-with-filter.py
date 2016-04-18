# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def valid(email):
    if re.match('[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\..{1,3}$', email):
        return True
    else:
        return False

s = [raw_input() for _ in xrange(int(raw_input()))]
print(sorted(filter(valid, s)))

