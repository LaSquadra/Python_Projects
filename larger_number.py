#!/usr/bin/env python3
import sys
def main(list_o_nums):
    largest_num=0
    yourfile=open(sys.argv[1],"r")
    for i in yourfile:
        if int(i)>int(largest_num):
            largest_num=i
    return largest_num.strip()
if __name__=="__main__":
    print(main(sys.argv))


