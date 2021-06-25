#!/usr/bin/env python3
import sys
def name_counter(names_list):
    frequency={}
    for name in names_list:
        if name in frequency:
            frequency[name]+=1
        else:
            frequency[name]=1
    return frequency

def main():
    file_path=sys.argv[1]
    my_file=open(file_path, "r")
    names_list=[]
    for line in my_file:
        name=line.rstrip()
        names_list.append(name)    
    my_file.close()
    frequency=name_counter(names_list)
    sorted_keys=sorted(frequency.keys())
    for name in sorted_keys:
        print(name+ " - " + str(frequency[name]))
if __name__=="__main__":
    main()
