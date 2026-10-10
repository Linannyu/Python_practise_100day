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

# prints the mammals dataframe
print("Mammals DataFrame with Default Index")
print("-----------------")
print(mammals)

# prints the mammals dataframe using the mammal column as the index
print()
print("Mammals DataFrame with Index = Mammals Column")
print("-----------------")
print(mammals.set_index("mammal"))

# prints the mammals datafram (index didn't change)
print()
print("Didn't actually change the DataFrame...")
print("-----------------")
print(mammals)

# changes the index to the mammal column 
# prints the NEW mammals dataframe
print()
print("DOES change the DataFrame...")
print("-----------------")
mammals.set_index("mammal", inplace=True)
print(mammals)

# stores the table consisting of only the hours of sleep 
# columns in a variable
sleep_data = mammals[["hours_of_sleep"]]

# prints the sleep_data for mammals who sleep less than 4 hours
print()
print("Sleeps Less Than 4 Hours")
print("-----------------")
new_data = sleep_data[sleep_data["hours_of_sleep"] < 4]
print(new_data)

# resets the index by renumbering the rows
print()
print("Renumbers the Rows")
print("-----------------")
new_data.reset_index(inplace=True)
print(new_data)