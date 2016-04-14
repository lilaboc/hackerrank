# https://www.hackerrank.com/challenges/python-string-formatting
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
width = len("{0:b}".format(N))
for i in xrange(1, N + 1):
    line = "{0}".format(i).rjust(width) 
    line += " " + "{0:o}".format(i).upper().rjust(width)
    line += " " + "{0:x}".format(i).upper().rjust(width)
    line += " " + "{0:b}".format(i).upper().rjust(width)
    print line
