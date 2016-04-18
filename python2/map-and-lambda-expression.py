# https://www.hackerrank.com/challenges/map-and-lambda-expression
# Enter your code here. Read input from STDIN. Print output to STDOUT
fib = [0, 1] + [0] * 13
for i in xrange(2, 15):
    fib[i] = fib[i - 1] + fib[i - 2]
print(map(lambda a: pow(a, 3), fib[: int(raw_input())]))

