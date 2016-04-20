#!/usr/bin/env python
import sys
import os
import os.path

url = sys.argv[1]
ext = {'python2': '.py', 'ruby' : '.rb', 'algorithm' : '.rb'}[os.path.basename(os.getcwd())]

filename = url.split('/')[-1] + ext
with open(filename, 'w') as f:
    f.write('# ' + url + '\n')
    f.write('# Enter your code here. Read input from STDIN. Print output to STDOUT\n')
os.system('"${EDITOR:-vi}" ' + filename)
