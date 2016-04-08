#!/usr/bin/env python
import sys
import os
url = sys.argv[1]
filename = url.split('/')[-1] + '.py'
with open(filename, 'w') as f:
    f.write('# ' + url + '\n')
    f.write('# Enter your code here. Read input from STDIN. Print output to STDOUT\n')
os.system('"${EDITOR:-vi}" ' + filename)
