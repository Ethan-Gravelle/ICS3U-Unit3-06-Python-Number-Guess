#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: May 6, 2020
# This program is a guessing game

import random


def main():
    # this function is a guessing game
    # this generates a number between 1-9
    some_variable = random.randint(1, 9)

    # input
    integer_as_string = input("Enter a number between 1-9: ")
    print("")
    # process & output
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number == some_variable:
            print("Correct")
        else:
            print("Incorrect, {0} is the number".format(some_variable))
    except Exception:
        print("{0} was not an integer.".format(integer_as_string))
    finally:
        print("Thanks for playing.")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
