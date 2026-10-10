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

# prints the hours of sleep column
print("Hours of Sleep Column ONLY")
print("-----------------")
print(mammals[["hours_of_sleep"]])

# prints the mammal and hours of sleep columns
print()
print("Mammal and Hours of Sleep Columns")
print("-----------------")
print(mammals[["mammal", "hours_of_sleep"]])

# stores the mammals and hours of sleep columns in a variable
sleep_data = mammals[["mammal", "hours_of_sleep"]]

# prints the sleep_data for mammals who sleep exactly 8 hours
print()
print("Sleeps 8 Hours")
print("-----------------")
print(sleep_data[sleep_data["hours_of_sleep"] == 8])

# prints the sleep_data for mammals who sleep less than 4 hours
print()
print("Sleeps Less Than 4 Hours")
print("-----------------")
print(sleep_data[sleep_data["hours_of_sleep"] < 4])


# prints the sleep_data for mammals who sleep exactly 8 hours OR
# less than 4 hours
print()
print("Sleeps 8 Hours OR Less Than 4 Hours")
print("-----------------")
print(sleep_data[(sleep_data["hours_of_sleep"] == 8) |
                 (sleep_data["hours_of_sleep"] < 4)])