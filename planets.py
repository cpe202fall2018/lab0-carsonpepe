#
# Name: Carson Pepe
# Student ID: 13926584
# 9/24/2018
#
# Lab 0
# Section 13
# Purpose of Lab: To practice writing more efficient code.

def weight_on_planets():

   # Prompts user for their weight, casts input into an integer, then stored in a var
   weight = int(input("What do you weigh on earth? "))

   # Prints output and uses the variable to multiple by appropriate number
   print("\nOn Mars you would weigh", weight * 0.38, "pounds.\nOn Jupiter you would weigh", weight * 2.34, "pounds.")

if __name__ == '__main__':
   weight_on_planets()
