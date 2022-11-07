#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    domain = input("Please enter a domain address: ")

    path = input("Enter the path you want to query: ")


    print("you want to query")
    print("https://", domain, path, sep="")

    uri = "https://" + domain + path

    print(uri)


# this calls main
main()

