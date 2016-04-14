# https://www.hackerrank.com/challenges/validating-named-email-addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in xrange(int(raw_input())):
    line = raw_input()
    name, email = line.split()
    if re.match('[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email[1:-1]):
        print line
