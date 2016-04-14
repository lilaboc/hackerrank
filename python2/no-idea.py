# https://www.hackerrank.com/challenges/no-idea
# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
l = [int(i) for i in raw_input().split()]
a = set([int(i) for i in raw_input().split()])
b = set([int(i) for i in raw_input().split()])
score = 0
for i in l:
    if i in a:
        score += 1
    if i in b:
        score -= 1
print(score)
