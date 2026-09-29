countries = ["Australia", "Egypt", "Greece", "India", "Jamaica", "Mexico", "Spain", "United States"]
sugar_1980 = [152, 71.8, 73.5 ,52.2, 153, 124, 83.7, 158]
sugar_1990 = [137, 86.6, 87.3, 56, 142, 141, 76.1, 173]
sugar_2000 = [123, 82.1, 90.4, 63.7, 161, 132, 81, 189]
sugar_2010 = [126, 81.2, 77.3, 59.9, 137, 136, 83.2, 167]


# average sugar consumed in 2010
ave = sum(sugar_2010) / len(sugar_2010)
print(ave)



# range of sugar consumed in 1990
print(min(sugar_1990))
print(max(sugar_1990))



# average of sugar consumed in total for all four decades
total = sugar_1980 + sugar_1990 + sugar_2000 + sugar_2010
ave_total = sum(total) / len(total)
print(ave_total)
# Challenge: average sugar consumed by the United States 
# over the four decades

US = sugar_1980[-1] + sugar_1990[-1] + sugar_2000[-1] + sugar_2010[-1]
ave_US = sum(US) / 4
print(ave_US)

