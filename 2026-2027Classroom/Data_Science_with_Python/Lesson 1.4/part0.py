"""Part 0: Library Examples"""
"""Example A: Random Library Example"""
#This example demonstrates the use of the random module in Python. Read through the comments to understand how it all works.
# imports the library
import random

# prints a random float between 0 and 1
print(random.random())

# prints a random integer between 1 and 10
print(random.randint(1,10))

my_list = [2, 109, False, 10, "Lorem", 482, "Ipsum"]

# prints a random element from my_list
print(random.choice(my_list))


"""Example B: Math and Statistics Library Example"""
#This example demonstrates the use of the math and statistics modules in Python. Read through the comments to understand how it all works. 
# imports the statistics and math libraries
import statistics
import math

# prints pi = 3.14...
print(math.pi)

# prints 2 to the third power (2^3) = 2 * 2 * 2
print()
print(math.pow(2,3))

cousins_ages = [8, 12, 14, 14, 15, 19, 22]

# prints the mean of the elements in cousins_ages
print()
print("Mean: " + str(statistics.mean(cousins_ages)))

# prints the median of the elements in cousins_ages
print("Median: " + str(statistics.median(cousins_ages)))

# prints the mode of the elements in cousins_ages
print("Mode: " + str(statistics.mode(cousins_ages)))

# prints the standard deviation of the elements in cousins_ages
std = statistics.stdev(cousins_ages)
print("Standard Deviation: " + str(std))

# drops the decimal (this is different than rounding)
print()
print("Using 'floor': " + str(math.floor(std)))

# round is built-in to python without using the math module
print("Using 'round': " + str(round(std, 2)))

"""Example C: Emoji Library"""
#This example demonstrates the use of the emojis library in Python. Read through the comments to understand how it all works.
# <-- Check out the requirement.txt file to see the libraries

# imports a SPECIFIC function from the emoji library 
from emoji import emojize 

# imports the whole emojis library
import emojis

print()
print(emojize(":thumbs_up:")) 

print()
print("There is a " + emojize(":snake:") + " in my boot!") 

print()
print(emojis.encode("This is a message with two emojis :stuck_out_tongue_winking_eye: :collision:"))

print()
print(emojis.decode("😄"))