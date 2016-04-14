# https://www.hackerrank.com/challenges/py-the-captains-room
# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(raw_input())
room_list = [int(i) for i in raw_input().split()]
seen = set()
first = set()
for i in room_list:
    if not i in seen and i not in first:
        first.add(i)
    elif i in first:
        first.remove(i)
        seen.add(i)
print first.pop()    
