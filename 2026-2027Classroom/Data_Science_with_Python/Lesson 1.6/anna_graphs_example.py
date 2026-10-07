# Dataset: People Names Anna
# This item may take a bit to load in the editor the first time the code is run.

# The data used in this example lists the number of people named Anna in the US that were born in each year from 1990 to 2017.

# Read through the comments and take note of the different functions used to find out more about this dataset.

import pandas as pd
import matplotlib.pyplot as plt

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

# Plot a box plot
plt.boxplot(people_named_anna)
plt.show()

# Change boxplot to hist in the function above to see a histogram of the data!