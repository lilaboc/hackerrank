# https://www.hackerrank.com/challenges/string-validators
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
r = [getattr(y, x)()  for x in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'] for y in s]
for i in [r[i:i+len(s)] for i in xrange(0, len(r), len(s))]:
    print any(i)
    
