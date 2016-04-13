# https://www.hackerrank.com/challenges/re-split
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in re.split('[\.,]', raw_input()):
    if re.match('\d+$', i):
        print i
