import pandas as pd

# data using a dictionary
data = {"mammal": ["African Elephant", "Bottlenose Dolphin", "Cheetah", "Domestic Cat", "Giraffe", "Ground Squirrel", "Horse", "House Mouse", "Human", "Killer Whale", "Lion", "Pig", "Rabbit"],
        "life_span": [70, 25, 14, 16, 25, 9, 25, 3, 80, 50, 15, 10, 5],
        "hours_of_sleep": [3, 5, 12, 12, 2, 15, 3, 12, 8, 3, 20, 8, 11],
        "speed": [40, 37, 110, 50, 50, 19, 69, 13, 45, 48, 80, 18, 56],
        "diet": ["plants", "meat", "meat", "meat", "plants", "both", "plants", "both", "both", "meat", "meat", "both", "plants"]
    }

# format data into a DataFrame
mammals = pd.DataFrame(data)

# prints the data type of each columns
print("Data Types")
print("-------------")
print(mammals.dtypes)

# prints the number of rows and columns as (rows, columns)
print()
print("Shape")
print("-------------")
print("(rows, columns) = " + str(mammals.shape))

# prints statistics about each column rounding to one decimal
print()
print("Stats")
print("-------------")
print(round((mammals.describe()), 1))

# prints the first five rows
print()
print("First Five Rows")
print("-------------")
print(mammals.head())

#prints the last three rows
print()
print("Last Three Rows")
print("-------------")
print(mammals.tail(3))

# print rows three to five
print()
print("Rows Three to Five (Indicies 2 to 4)")
print("-------------")
print(mammals[2:5])