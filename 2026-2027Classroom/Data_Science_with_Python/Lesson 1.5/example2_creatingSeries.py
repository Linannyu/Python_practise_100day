import pandas as pd

# Create a series and specify an index 
ingredients = pd.Series(["4 cups", "1 cup", "2 large", "1 cup"], index=["Flour", "Milk", "Eggs", "Sugar"])

print()
print("Ingredients")
print("--------------------")
print(ingredients)
print()

# Create a series using a Python dictonary. A dictionary
# stores data in key:value pairs. The key becomes the index. 
s = {"Los Angeles Dodgers": 2020, "New York Yankees": 2009, 
    "Boston Red Sox": 2018, "Chicago Cubs": 2016, "San Francisco Giants": 2014, 
    "Colorado Rockies": None}
world_series = pd.Series(s)

print()
print("World Series Winners")
print("--------------------")
print(world_series)