#!/usr/bin/env python3
import sys
def main(user_file):
    your_file=open(sys.argv[1],"r")
    for line in your_file:
        if int(line)%2==0:
            line=line.strip()
            print(line,"True")
        else:
            line=line.strip()
            print(line,"False")
    your_file.close()
if __name__=="__main__":
    main(sys.argv)
