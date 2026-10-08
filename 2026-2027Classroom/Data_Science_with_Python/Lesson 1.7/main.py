import pandas as pd

data = {"Student": ["Anayo", "Brandon", "Claudia", "Dave", "Evelyn", "Finn", "Gloria", "Hank", "Isla", "Julia"],
        "Test One": [84, 90, 50, 29, 49, 44, 30, 98, 31, 66],
        "Test Two": [68, 78, 28, 80, 45, 56, 53, 93, 31, 66],
        "Test Three": [42, 35, 30, 40, 28, 85, 80, 99, 38, 48]
    }

test = pd.DataFrame(data)
print(test)

print()
print("1) Data Types")
print("-------------")
print(test.dtypes)

print()
print("2) Shape")
print("-------------")
print("(rows, columns) = " + str(test.shape))

print()
print("3) Stats")
print("-------------")
print(round((test.describe()), 1))

print()
print("4) First Three Rows")
print("-------------")
print(test.head(3))

print()
print("5) Last Five Rows")
print("-------------")
print(test.tail(5))

print()
print("6) Rows Second to Eighth (Indicies 2 to 8)")
print("-------------")
print(test[1:8])
