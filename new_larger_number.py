#!/usr/bin/env python3
import sys
def main(argument):
    yourfile=open(sys.argv[1],"r")
    print(yourfile)
    yourfile=sorted(yourfile.readlines())
    print(yourfile)
    return yourfile[-1].strip()
if __name__=="__main__":
    print(main(sys.argv))
