import pandas as pd

# Create a series with default indexing
pies = pd.Series(["Pumpkin", "Pecan", 3.14, "Lemon Meringue", "Apple"])

print("Pies")
print("--------------------")
print(pies)
print()

# Print item based on its index
print()
print("pies[2] = " + str(pies[2]))
print()

# Change item based on its index and reprint the series
pies[2] = "Pizza"

print()
print("Pies (with pizza)")
print("--------------------")
print(pies)
print()

# Print NEW item based on its index
print()
print("pies[2] = " + str(pies[2]))
print()

# Create a series and specify an index to use
new_pies = pd.Series(["Pumpkin", "Pecan", "Pizza", "Lemon Meringue", "Apple"],
              index=["A", "B", "C", "D", "E"])

print()
print("New Pies (with specific indices)")
print("--------------------")
print(new_pies)
print()

# Print item based on its NEW index
print()
print("pies[C] = " + str(new_pies["C"]))
