#Part 2: 
"""
Paste your data table from the Gathering Data activity into data2.csv
"""
import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv (r"data2.csv")

print(df)


# Create a list for the columns of your dataset.
item_name = ["Caffe Latte", "Cold Brew", "Blueberry Muffin", "Green Tea", "Caramel Macchiato", "Iced Matcha Latte", "Croissant", "Americano", "Chai Latte", "Cappuccino", "Chocolate Chip Cookie", "Nitro Cold Brew", "Hot Chocolate", "Bagel with Cream Cheese", "Iced Americano"]
category = ["Espresso Drink", "Cold Coffee", "Bakery", "Tea", "Espresso Drink", "Tea", "Bakery", "Espresso Drink", "Tea", "Espresso Drink", "Bakery", "Cold Coffee", "Specialty Drink", "Bakery", "Espresso Drink"]
price = [4.50, 4.25, 3.25, 3.00, 5.25, 5.00, 3.50, 3.25, 4.25, 4.00, 2.75, 4.75, 3.75, 3.95, 3.75]
quantity_sold = [38, 52, 21, 17, 44, 29, 19, 33, 25, 31, 40, 22, 16, 27, 36]


# Print the data types of the elements in the lists. 
print(type(item_name[0]))
print(type(category[0]))
print(type(price[0]))
print(type(quantity_sold[0]))





# Print the length, the max value, the min value and the 
# sum of the other lists. Note: The sum function will not 
# work on a string.
print()
print(f"The length of the item_name list is {len(item_name)}\nThe minimum item_name is {min(item_name)}\nThe maximum item_name is {max(item_name)}\nThe sum of all Weight is Null")
print()
print(f"The length of the category list is {len(category)}\nThe minimum category is {min(category)}\nThe maximum category is {max(category)}\nThe sum of all Weight is NULL")
print()
print(f"The length of the price list is {len(price)}\nThe minimum price is {min(price)}\nThe maximum price is {max(price)}\nThe sum of all Weight is {sum(price)}")
print()
print(f"The length of the quantity_sold list is {len(quantity_sold)}\nThe minimum quantity_sold is {min(quantity_sold)}\nThe maximum quantity_sold is {max(quantity_sold)}\nThe sum of all Weight is {sum(quantity_sold)}")