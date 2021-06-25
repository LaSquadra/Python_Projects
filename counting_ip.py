#!/usr/bin/env python3
import sys
def ip_counter():
    my_file=open(sys.argv[1],"r")
    sorted_file=sorted(my_file)
    ip_address={}
    for line in sorted_file:
        line=line.split(" ")
        if line[0] not in ip_address:
            ip_address[line[0]]=1
        else:
            ip_address[line[0]]+=1
    my_file.close()
    for item in ip_address:
        print(str(item)+" - "+str(ip_address[item]))

ip_counter()
