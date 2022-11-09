#!/usr/bin/env python3
"""Alta3 Research - RZFeeser@alta3.com
   Learning to read files with Python"""

def main():
    ######## EXPLORE READ ##########
    ## create file object in "r"ead mode
    configfile = open("vlanconfig.cfg", "r") # open the file vlanconfig.cfg

    ## display file to the screen - .read()
    print(configfile.read())

    ## close file
    configfile.close()

    ######## EXPLORE READLINES ##########
    ## re-create file object to explore new method
    configfile = open("vlanconfig.cfg", "r")

    ## make a list of file lines - .readlines()
    configlist = configfile.readlines()
    print(configlist)

    ## Iterate through configlist
    for x in configlist:
        print(x.strip())

    ## Always close your file
    configfile.close()


if __name__ == "__main__":
    main()
