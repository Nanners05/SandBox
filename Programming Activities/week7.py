"""
Programming Activity 1

Write a program, and have the user enter their name and their favorite 
color, as two separate variables. Write the sentence to a file using the 
with command "<name>'s favorite color is <color>"
- get two variables from user
- use the with command to open the file
- use the write function to write to the file
"""

name = input("Please enter your name >")
color = input("Enter your favorite color >")

with open("week7.txt", "w") as file:
    file.write(name + "'s favorite color is " + color)
    

"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. Then, change the 
array from 0s to random numbers.
"""

import random, numpy as np

array1 = np.zeros(100)
array1 = np.random.rand(100)

print(array1)