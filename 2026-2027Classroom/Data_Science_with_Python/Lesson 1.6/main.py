import pandas as pd
import matplotlib.pyplot as plt

hotdog = pd.Series([72.0, 41.0, 70.0, 38.0, 62.0, 38.0, 61.0, 34.0, 69.0, 36.8], 
        index=["Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Miki Sudo ", "Matthew Stonie", "Miki Sudo", "Joey Chestnut", "Miki Sudo", "Joey Chestnut", "Sonya Thomas"])

print()
print("1) Variance:")
print(hotdog.var())

print()
print("2) Standard Deviation:")
print(hotdog.std())

max = hotdog.max()
min = hotdog.min()
range = max - min

print()
print("3) Range:")
print(range)

Q1 = hotdog.quantile(0.25)
Q3 = hotdog.quantile(0.75)
IQR = Q3 - Q1

print()
print("4) IQR:")
print(IQR)


print("---------Part 2-----------")

# Plot a box plot

plt.boxplot(hotdog)
plt.show()

print("median is 51\nmin is 34\nmax is 72\nfirst quantile is 38\nthird quantile is 67.25")

plt.figure()
plt.hist(hotdog)
plt.show()
