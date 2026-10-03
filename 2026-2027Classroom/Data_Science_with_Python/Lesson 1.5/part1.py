import pandas as pd

list1 = pd.Series([72.0, 41.0, 70.0, 38.0, 62.0, 38.0, 61.0, 34.0, 69.0, 36.8], 
        index=["Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Miki Sudo ", "Matthew Stonie", "Miki Sudo", "Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Sonya Thomas"])

print(list1)

print("--------------------")

dictionary = {"Joey Chestnut": 72.0, "Miki Sudo": 41.0, "Joey Chestnut": 70.0, "Miki Sudo": 38.0, "Matthew Stonie": 62.0, "Miki Sudo": 38.0, "Joey Chestnut": 61.0, "Miki Sudo": 34.0, "Joey Chestnut": 69.0, "Sonya Thomas": 36.8}
dictionarys = pd.Series(dictionary)
print(dictionarys)