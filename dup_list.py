#! /usr/bin/env python3

#Version 1 (First take on it)

list1=["David","Emma","Rafael","Catherine","David","Joleen","Steven",1,2,3,4,5,6,7,1,2,7]

def list_dup_finder(list1):
    base_list=[]
    dup_list=[]
    for i in list1:
        if i not in base_list:
            base_list.append(i)
        else: 
            dup_list.append(i)
    return dup_list
print(list_dup_finder(list1))

#Version 2 (Another take on it)

def find_duplicates(list1):
    dup_list=[]
    for item in list1:
        if (list1.count(item)>1) and (item not in dup_list):
            dup_list.append(item)
    return dup_list
print(find_duplicates(list1))