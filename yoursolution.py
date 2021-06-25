#!/usr/bin/env python3 
import sys
def front_x(arguments):
    my_x_list=[]
    my_other_list=[]
    for i in arguments[1:]:
        if i[0]=="x":
            my_x_list.append(i)
        else:
            my_other_list.append(i)
    return sorted(my_x_list)+sorted(my_other_list)

arguments=sys.argv
print(front_x(arguments))
