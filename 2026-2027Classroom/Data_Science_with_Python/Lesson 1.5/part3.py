import pandas as pd

hotdog = pd.Series([72.0, 41.0, 70.0, 38.0, 62.0, 38.0, 61.0, 34.0, 69.0, 36.8], 
        index=["Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Miki Sudo ", "Matthew Stonie", "Miki Sudo", "Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Sonya Thomas"])

print(f"1) {"Jonathan Johnson" in hotdog.index}")
print(f"2) {"Miki Sudo" in hotdog.index}")
print(f"3) Mean: {hotdog.mean()}")
print(f"4) Median: {hotdog.median()}")
print(f"5) Mode: {hotdog.mode()}")
print(f"6) Summary: \n{hotdog.describe()}")

