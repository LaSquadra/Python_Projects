#!/usr/bin/env python3
import sys
def six_arguments(arguments):
    if len(sys.argv[1:])<6:
        print("Sorry, no!")
    else:
        print("FS{here_is_your_flag!}")
six_arguments(sys.argv)

