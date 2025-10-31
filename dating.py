#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 10 30, 2025
# This program asks the user to input their age and tells them if they can date the grandchild


def main():
    try:
        # have the user enter their age
        Age = input(" Please enter your age")
        Age_int = int(Age)

        # if the age is > 25 and < 40 then display :You can date my grandchild
        if Age_int > 25 and Age_int < 40:
            print("You Can Date my grandchild! :)")
        else:
            print(f"You cannot date my grandchild ")
        # if the integer is not valid, display ("this is not valid")
    except ValueError:
        print("This is not a valid integer.")
        # display thank you for playing at the end of the program
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
