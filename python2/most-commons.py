# https://www.hackerrank.com/challenges/most-commons
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
import operator
for i in sorted(Counter(raw_input()).most_common(), key=lambda element: (-int(element[1]), element[0]))[:3]:
    print ' '.join([str(o) for o in i])
