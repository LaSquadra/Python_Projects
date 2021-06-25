#!/usr/bin/env python3
import sys
def main(my_input):
    yourfile=open(sys.argv[1],"r")
    line_count=0
    message=""
    for line in yourfile:
        line_count+=1
        if line_count==int(sys.argv[2]):
            print(line.strip())
            for word in line.split(" "):
                message=message+word[0]
            print("Here is your hidden message: "+message)
    yourfile.close()

if __name__=="__main__":
    main(sys.argv)
