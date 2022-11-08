#!/usr/bin/python3

"""Python3 Optional Challenge
   Playing around with formatting output data

   RZFeeser@alta3.com"""


def main():
    """run time function"""

    # a list of strings
    animalfarm = ['cow', 'pigs', 'horse', 'ducks', 'chickens', 'dogs']

    # print our list
    print(animalfarm)


    # hardcoding the data works
    # but is subject to fail if the data changes!
    print(animalfarm[0], animalfarm[1], animalfarm[2], animalfarm[3], animalfarm[4], animalfarm[5])


    # our first example of a loop
    # for "iterator" in "iterable":
    for animal in animalfarm:
        print(animal, end=" ")



if __name__ == "__main__":
    main()
