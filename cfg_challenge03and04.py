#!/usr/bin/env python3
"""Alta3 Research RZFeeser@alta3.com
   CHALLNEGE 04 - At the top of the program, write code to prompt the user for the name of file
   to load. Replace vlanconfig.cfg with that value, so the user may control the name of the file
   that is read into the script."""


def main():

    ## create file object in "r"ead mode
    with open(input("What file are we opening? "), "r") as configfile:
        ## readlines() creates a list by reading target
        ## file line by line
        configlist = configfile.readlines()

    ## file was just auto closed (no more indenting)

    ## each item of the list now has the "\n" characters back
    print(configlist)


    # CUSTOMIZATION 03 - Add as few lines as possible to display how many lines are in the
    # file vlanconfig.cfg. Display the number of lines on the screen at the end of the script.
    print("The number of lines is", len(configlist))

main()
