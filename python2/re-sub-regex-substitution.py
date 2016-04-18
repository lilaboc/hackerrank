# https://www.hackerrank.com/challenges/re-sub-regex-substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def replace(match):
    if match.group(0) == ' &&':
        return ' and'
    else:
        return ' or'

for _ in xrange(int(raw_input())):
    print re.sub(' (&&|\|\|)(?= )', replace, raw_input())

