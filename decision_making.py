#!/usr/bin/python3

"""Making Choices with Python
   if, elif, else
   checking input"""

def main():
    """run time code"""

    ans = input("What is your favorite color? ")

    # use a string function to 'normalize' the input
    ans = ans.lower()  # everything should be lower case

    ## create lists containing colors we accept
    blue_shades = ['blue', 'slate', 'sky', 'navy', 'indigo', 'cobalt', 'teal', 'ocean', 'stone', 'spruce']

    #if ans == 'blue' or ans == 'light blue' or ans == 'dark blue':
    if ans in blue_shades:
        print("Color of the sky")
    elif ans == 'green' or ans == 'dark green' or ans == 'light green':
        print("Color of the grass")
    elif ans == 'red':
        print("Color of fire")
    else:
        print("I don't know that color")


    # collecting a second input for more complicated testing
    ans2 = input("What is your name? ")

    if ans2 != "" and ans != "":
        print("Thanks for typing in something both times")
    elif ans2 != "" and ans == "":
        print("Looks like you didn't type anything in the first time, and did the second time")
    elif ans2 == "" and ans != "":
        print("Looks like you didn't type something in the second time, and did the first time")
    else:
        print("did get to analyzing that yet...")





if __name__ == "__main__":
    main()
