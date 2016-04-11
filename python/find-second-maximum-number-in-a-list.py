# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
arr = [int(i) for i in raw_input().split()]
largest = None
second_largest = None
for i in arr:
    if i > largest:
        second_largest, largest  = largest, i
    elif i > second_largest and i != largest:
        second_largest = i
print(second_largest)
