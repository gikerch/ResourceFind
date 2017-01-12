# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:28:57 2016

@author: acer-zhou
"""

newfile = open('allurl.txt','w+')
for i in range(1,31):
    filename = str(i)+'.txt'
    f = open(filename)
    contents = f.read()
    newfile.write(contents)
    
    