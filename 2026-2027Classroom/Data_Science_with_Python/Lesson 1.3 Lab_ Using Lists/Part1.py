import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv (r"data.csv")

print(df)
#Part 1

"""
Creates a list for the height_in_inches column that consists of all 
#of the values in that column.
"""
heights = [71, 69, 70, 71, 68, 70, 70]

# Your Turn: Create a list for the name, weight, and 
# net_worth columns.

name = ['Jin', 'Suga', 'J-Hope', 'RM', 'Jimin', 'V', 'Jungkook']
weight = [136, 138, 132, 145, 143, 137, 145]
net_worthq = [8, 8, 12, 8, 8, 8, 8]





"""
Print the data type of the elements in the height list. 
What data type is it?
"""

print(heights)
print("Height elements are stored as " + str(type(heights[0])))

# Your Turn: Print the data types of the elements in the other lists. 
print(name)
print("Height elements are stored as " + str(type(name[0])))
print(weight)
print("Height elements are stored as " + str(type(weight[0])))
print(net_worthq)
print("Height elements are stored as " + str(type(net_worthq[0])))




# Your Turn: Print the data type of one of the lists. 
# What data type is it?
print(type(name))




"""
Print the length of the heights list, the max value, the min value 
and the sum of the heights list.
"""

print()
print("The length of the heights list is " + str(len(heights)))
print("The minimum height is " + str(min(heights)))
print("The maximum height is " + str(max(heights)))
print("The sum of all heights is " + str(sum(heights)))

# Your Turn: Print the length, the max value, the min value and the 
# sum of the other lists. Note: The sum function will not work on a string.
# How do you suppose the min and max work with strings based on what
# is printed?
print()
print("The length of the name list is " + str(len(name)))
print("The minimum name is " + str(min(name)))
print("The maximum name is " + str(max(name)))
# print("The sum of all heights is " + str(sum(name)))
print()
print("The length of the weight list is " + str(len(weight)))
print("The minimum weight is " + str(min(weight)))
print("The maximum weight is " + str(max(weight)))
print("The sum of all Weight is " + str(sum(weight)))
print()
print("The length of the net_worthq list is " + str(len(net_worthq)))
print("The minimum net_worthq is " + str(min(net_worthq)))
print("The maximum net_worthq is " + str(max(net_worthq)))
print("The sum of all net_worthq is " + str(sum(net_worthq)))


print(len(name))
# In the string, the letter 'a' is the smallest and 'z' is the largest; values ​​are taken in this order.