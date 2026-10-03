import pandas as pd

hotdog = pd.Series([72.0, 41.0, 70.0, 38.0, 62.0, 38.0, 61.0, 34.0, 69.0, 36.8], 
        index=["Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Miki Sudo ", "Matthew Stonie", "Miki Sudo", "Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Sonya Thomas"])

print(hotdog.mean())
print(hotdog.median())

print(hotdog.mode())