#!/usr/bin/env python3
## create file object in "r"ead mode


configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
configblob = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblob.splitlines()

## display list with no "\n"
print(configlist)

## Always close your file
configfile.close()

