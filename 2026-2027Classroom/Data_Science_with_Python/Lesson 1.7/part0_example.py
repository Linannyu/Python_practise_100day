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

# print data to the console
print(mammals)