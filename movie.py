#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


def main():

    message = 'The movie is about to begin, we recommend '

    # wrap connection in a float() to accept decimals as number
    # the following line would ERROR if someone typed in a non-number
    # connection = float(input("What is your connection speed in Mbps? "))

    connection = input("What is your conneciton speed in Mbps? ")
    connection2 = connection

    if not connection2.replace(".", "").isdigit():
        print("I am unsure what you mean by:", connection, "Exiting...")
        return  # if you "return" from the only function
                # the program will end without an error
    
    # we are now safe to "transform" our connection into a float
    connection = float(connection)

    # if input value was higher or equal to 25
    if connection >= 25:
        message = message + 'setting video to 4k.'
    elif connection >= 5:
        message = message + 'setting video to 1080p.'
    elif connection >= 2:
        message = message + 'setting video to 720p.'
    else:
        message = message + 'finding another access network.'
    
    # this is outside of the if, elif, else logic block
    # so it always runs
    print(message) # display the message created


if __name__ == "__main__":
    main()
