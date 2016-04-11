# https://www.hackerrank.com/challenges/text-wrap
# Enter your code here. Read input from STDIN. Print output to STDOUT
import textwrap
s = raw_input()
width = int(raw_input())
print(textwrap.fill(s, width))
