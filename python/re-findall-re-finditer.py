# https://www.hackerrank.com/challenges/re-findall-re-finditer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.findall('(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', raw_input())
if len(m) != 0:
    for i in m:
        print i
else:
    print '-1'
