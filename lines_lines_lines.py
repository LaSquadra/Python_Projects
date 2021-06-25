#!/usr/bin/env python3
import sys
def main(the_file):
    yourfile=open(sys.argv[1],"r")
    corrected_file=""
    for line in yourfile:
        if line!="\n":
            corrected_file+=line.strip()+" "
    print(corrected_file)
    yourfile.close()
if __name__=="__main__":
    main(sys.argv)
            
