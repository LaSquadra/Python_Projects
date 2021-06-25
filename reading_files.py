#!/usr/bin/env python
import sys
filepath=sys.argv[1]
my_file=open(filepath,"r")
for line in my_file:
    #print(line,)
    # or #
    line=line.strip()
    print(line)
my_file.close()
