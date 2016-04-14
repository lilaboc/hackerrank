# https://www.hackerrank.com/challenges/capitalize
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
result = ''
space = True
for index, value in enumerate(s):
    if space and value != ' ':
        result += value.upper()
        space = False
    else:
        if value == ' ':
            space = True
        result += value.lower()
print result
