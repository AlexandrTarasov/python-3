#!/usr/bin/python

import os, sys

# Open a file
path = "."
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print (file)




from os import listdir
from os.path import isfile
from os.path import join as joinpath

mypath = "content"
for i in listdir(mypath):
    if isfile(joinpath(mypath,i)): #only files
        print i
      
      
mytxt = filter(lambda x: x.endswith('.txt'), files) #only text files
