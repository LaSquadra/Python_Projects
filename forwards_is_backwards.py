#!/usr/bin/env python3
import sys
def main(the_file):
    yourfile=open(sys.argv[1],"r")
    for line in yourfile:
        reverse_line=line[::-1]
        if line.strip()==reverse_line.strip():
            print("True")
        else:
            print("False")
    yourfile.close()
if __name__=="__main__":
    main(sys.argv)
