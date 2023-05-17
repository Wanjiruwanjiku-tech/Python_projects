#!/usr/bin/python3

import random

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Your Number of choice should be in the range 0 to 10\n")
number_of_choice = int(input("Enter a Number of choice: "))
random_num = random.choice(my_list) #returns random element

if number_of_choice == random_num:
    print("Correct Guess\n")
    print(f"Your number is: {number_of_choice}")
else:
    print("Incorrect guess\n")
    print(f"Your guess is: {number_of_choice}")
    print(f"The number is: {random_num}")

