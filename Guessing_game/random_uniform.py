#!/usr/bin/python3

import random
import sys

print("INSTRUCTION")
print("Your number of choice can be a decimal point 0-5\n")
num_of_choice = input("Enter You number: ")
rand_num = random.uniform(0, 4.9) + 0.5
#returns a rand float inlusive 0 and 5

if num_of_choice == rand_num:
    print("Correct choice :>\n")
    print(f"Your Number is: {rand_num}")
elif num_of_choice == 2.5:
    sys.stdout.write("JACKPOT")
else:
    sys.stdout.write("Incorrect choice\n")
    print(f"Your choice is: {num_of_choice}")
    print(f"The Number is: {rand_num}")
