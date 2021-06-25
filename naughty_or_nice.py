#!/usr/bin/env python3
import sys
def main():
    my_file=open(sys.argv[1], "r")
    the_list={"good_list":0,"bad_list":0}
    for line in my_file:
        line=line.strip()
        if line[-4:]=="good":
            the_list["good_list"]+=1
        elif line[-3:]=="bad":
            the_list["bad_list"]+=1
    my_file.close()
    print("Naughty list has "+str(the_list["bad_list"])+" people!\nNice list has "+str(the_list["good_list"])+" people!")
if __name__=="__main__":
    main()
