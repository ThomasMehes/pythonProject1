import random


# import random
# low = int(input("low: "))
# high = int(input("high: "))
# SECRET = random.randint(low, high)
# guess = int(input("? "))
# while guess != SECRET:
#     print("Guess again!")
#     guess = int(input("? "))
# print("You got it!!!")


# Importing modules:
# import math  #everything accessible, but use full name
# math pi

# from math import * # everything accessible
# pi


# import random
# length = int(input("length: "))
# random_width = random.randint(1, length)
# area = length * random_width
# print(f"the random width was: {random_width} m")
# print(f"therefore the area is: {area} m")

# import random
# low = int(input("Lower limit: "))
# high = int(input("upper limit: "))
#
# while high < low:
#     print("upper limit needs to be greater than lower limit")
#     low = int(input("Lower limit: "))
#     high = int(input("upper limit: "))
#
# random_number = random.randint(low, high)
# print('😁' * random_number)
#


# void ------- non-value returning


# def print_grid(no_of_rows, no_of_columns):
#     # version 1:
#    for i in range(no_of_rows):
#        for j in range(no_of_columns):
#            print('*', end="")
#        print()
# print_grid(3,7)

#     # version 2:
#     for i in range(no_of_rows):
#       print('*' * no_of_columns)
#
# print_grid(3, 7)

#     # version 3:
#       print(f"{'*' * no_of_columns}\n" * no_of_rows)
# print_grid(3, 7)


# FUNCTIONS - SRP - single responsibility principle
# usually don't use print or input unless thats its main purpose


# def main():
#     height = float(input("Height (m) : "))
#     weight = float(input("Weight (kg) : "))
#     bmi = calc_bmi(height, weight)
#     print(f"Your BMI is {bmi}.")

######## or
# import random
#
# def main():
#     height = random.uniform(1, 2)
#     if calc_bmi(height, 99) < 15:
#         print("Not considered overweight")

######### the function:
# def calc_bmi(height, weight):
#     return weight / (height ** 2)
#
# main()


######################## FUNCTION DEMO: ##################################
# menu:
# - get valid name
# - print greeting with line
# - print secret (random) name
#
#
# """Module 2 - functions"""
# import random
#
# def main():
#     name = ""
#     print("Menu: ")
#     print(f"(G)et name\n(P)rint greeting\n(S)ecret name\n(Q)uit")
#     choice = input("> ").upper()
#     while choice != "Q":
#         if choice == "G":
#             name = get_name()
#         elif choice == "P":
#             print_greeting(name)
#         elif choice == "S":
#             print_secret_name(name)
#         else:
#             print("invalid input")
#         print("Menu: ")
#         choice = input("> ").upper()
#
#     print("Farewell")
#
#
# def print_greeting(name):
#     """Format print with lines above and below name."""
#     length = len(name)
#     print_line(length)
#     print(name)
#     print_line(length)
#
# def get_name():
#     """ensures a valid name"""
#     name = input("Name: ")
#     while name == "":
#         print("invalid name")
#         name = input("Name: ")
#     return name
#
# def print_line(length):
#     """prints line of dashes '-' * length"""
#     print('-' * length)
#
# def print_secret_name(name):
#     letters = list(name)
#     random.shuffle(letters)
#     print( "".join(letters))
#
# main()

###########################DONT USE GLOBAL VARIBLES (for assigment partiuclarly) so don't define varibles outside main()
######unless its a constant like pi (never modifiy a constant).


########### Default parameter values
# def print_line(length=20, char="-"):
#     print(char * length)
#
########### unpack variables
def format_date(day: int, month: int, year: int) -> str:
    # ": int" & "-> str" forces an error messege if its wrong type
    return f"{day}/{month}/{year}"


date = (22, 11, 1988)  # tuple
# format_date(*date) # unpacks date tuple
print(f"{format_date(*date)}")
