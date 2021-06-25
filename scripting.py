#!/usr/bin/env python3

#.read() returns a string and is a method for files
#.readlines() returns a list and is a method for files
#.readline() returns a string and is a method for files
#.splitlines() returns a _____ and is a method for strings


import sys

#def readfile(my_file):
#    for line in my_file:
#        print(line.rstrip())
def readfile(my_file):
    for i in range(10):
        #print(my_file.read().rstrip()) #reads the whole file at once
        #print(my_file.readline().rstrip()) # reads one line at a time #maintains cursor location in file
        #print(my_file.readlines())  #splits the lines into a list #maintains cursor location in file
        print(my_file.readline().splitlines()) # removes the new line characters and makes them empty elements in the list

def main(path):
    opened=open(path,"r")
    readfile(opened)
    opened.close()

if __name__=="__main__":
    path =sys.argv[1]
    main(path)
