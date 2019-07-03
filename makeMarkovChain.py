
# -*- coding: utf-8 -*-
import os.path
import getPoems as gP
import pandas as pd

'''
First, we need to clean up the file and separate each word into a list
'''
poet_name = "walt-whitman"
file_name = poet_name+"-poems.txt"

if os.path.exists(file_name):
    poems_file = open(file_name)
else:
    gP.get_poems(poet_name)
    poems_file = open(file_name)

line_list = poems_file.readlines()
line_dict = {}
for line in line_list:
    temp_line = line.split()
    if len(temp_line) > 0:
        line_dict[temp_line[0]] = temp_line[1:]

print(line_dict)

#print(word_list)
poems_file.close()

'''
Now comes the analysis part
'''
