# https://www.hackerrank.com/challenges/nested-list
# Enter your code here. Read input from STDIN. Print output to STDOUT
lowest_names = []
result = []
lowest = None
second_lowest = None
for i in xrange(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    if not lowest:
        lowest = score
        lowest_names = [name]
    elif score < lowest:
        second_lowest, lowest = lowest, score 
        result = lowest_names[:]
        lowest_naems = [name]
    elif score == lowest:
        lowest_names.append(name)
    elif score == second_lowest:
        result.append(name)
    elif score < second_lowest or len(result) == 0 :
        second_lowest = score
        result = [name]
    #print lowest
    #print lowest_names
    #print second_lowest
    #print result
for i in sorted(result):
    print(i)
