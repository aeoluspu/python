#*************************************************************************
#     File Name: test_dir.py
#     Author: zhaohongpu
#     Mail: idbalife@gmail.com 
#     Created Time: 10/29 11:58:58 2017
# ************************************************************************
#coding=utf-8

from __future__ import print_function
import os
import sys

def main():
    if sys.version_info.major >=3:  # if the interpreter version is 3.x,use input
        input_func=input             #otherwise use 'raw_input'
    else:
        input_func=raw_input

    CheckDir = input_func("Enter the name of the directory to check:")
    print()

    if os.path.exists(CheckDir):  #Checks if the dir exists
        print("The directory exists")
    else:
        print("No directory found for " + CheckDir) #output if no directory 
        print()
        os.makedirs(CheckDir) #creates a new dir for the given name
        print("Directory created for " + CheckDir)


if __name__ == '__main__':
    main()
