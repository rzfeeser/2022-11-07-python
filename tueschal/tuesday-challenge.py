#!/usr/bin/python3
"""Tuesday morning challenge
   
   Store data in a structure (such as a list)

   RZFeeser@alta3.com"""


def main():
    """run-time code"""

    mylist = []

    # name = input("What is your name? ")
    # mylist.append(name)
    mylist.append(input("What is your name? "))

    mylist.append(input("What is your favorite color? "))

    mylist.append(input("is the air-speed velocity of an unladen swallow? "))

    # display answers to questions
    print(mylist)

# call our program
if __name__ == "__main__":
    main()
