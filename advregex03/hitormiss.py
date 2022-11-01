#!/usr/bin/env python3
import re
mytxt = open('grimm.txt') # open file object

allLines = mytxt.readlines() # read out of buffer into list

mytxt.close() # close file

lookingfor = re.compile(r'wol[vf][es]?\w+') # compile
                               ## a search expression

for oneline in allLines:   # search through the lines
    mymatchobj = lookingfor.search(oneline) # call
                      ## search() and pass oneline 
    if mymatchobj: # if mymatchobj has a value (if a match, then...)
            print(mymatchobj.group(), '***', oneline, end='') # Print
                 ## what was matched on, ***, then the string matched

print("+-+-+")

jasonlookingfor = re.compile(r'[Ee]Book[s]?\w+') # compile
                               ## a search expression

for oneline in allLines:   # search through the lines
    jasonmatchobj = jasonlookingfor.search(oneline) # call
                      ## search() and pass oneline
    if jasonmatchobj: # if mymatchobj has a value (if a match, then...)
            print(jasonmatchobj.group(), '***', oneline, end='') # Print
                 ## what was matched on, ***, then the string matched
