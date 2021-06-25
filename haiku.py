#!/usr/bin/env python3
import sys
from ast import literal_eval
def haiku_builder():
    my_file=open(sys.argv[1],"r")
    for line in my_file: #converting the file to a dict
        chunk=literal_eval(line)
    my_file.close()
    haiku_file={}
    for number in chunk: #converting key from str to int
        number_int=int(number)
        haiku_file[number_int]=chunk[number] #putting the updated key:value pair in the new dict
    sorted_haiku_file=sorted(haiku_file.keys())
    final_out=""
    for key in sorted_haiku_file: #creating proper output
        if chunk[str(key)]!="\n": #if the key is not the line-break
            final_out+=chunk[str(key)]+" " #add key to final output and put a space at the end
        else: #if key is a line-break
            final_out=final_out.rstrip() #remove extra characters from end only
            final_out+=chunk[str(key)] #add key to final output
    print(final_out) #final product

haiku_builder()