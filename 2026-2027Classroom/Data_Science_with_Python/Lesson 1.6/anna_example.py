import pandas as pd

# Create and print the series
people_named_anna = pd.Series([7288, 7118, 6846, 6808, 7523, 8564,
    8565, 8337, 8378, 9098, 10588, 10588,
    10385, 9443, 9514, 9101, 8601, 7888,
    7265, 6800, 6326, 5658, 5615, 5378,
    5679, 5125, 4775, 4520], index=["1990", "1991", "1992", "1993", "1994", "1995",
    "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005",
    "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015",
    "2016", "2017"])

print("People Named Anna")
print("--------------------")
print(people_named_anna)

# Find the variance
print()
print("Variance:")
print(people_named_anna.var())

# Find the standard deviation
print()
print("Standard Deviation:")
print(people_named_anna.std())

# Find the range using the max and min values
max = people_named_anna.max()
min = people_named_anna.min()
range = max - min

print()
print("Range:")
print(range)

# Find the interquartile range using the first and third quartile values
