import pandas as pd

data = {"Student": ["Anayo", "Brandon", "Claudia", "Dave", "Evelyn", "Finn", "Gloria", "Hank", "Isla", "Julia"],
        "Test One": [84, 90, 50, 29, 49, 44, 30, 98, 31, 66],
        "Test Two": [68, 78, 28, 80, 45, 56, 53, 93, 31, 66],
        "Test Three": [42, 35, 30, 40, 28, 85, 80, 99, 38, 48]
    }
test = pd.DataFrame(data)
print("-------Part 1--------")
print(f"Test One mean is {test["Test One"].mean()}")
print(f"Test Two max is {test["Test Two"].max()}")
print(f"Test Three min is {test["Test Three"].min()}")



print("-------Part 3--------")
test.set_index("Student", inplace = True)
print(test)

print("2) Print the students and test_two columns for those who scored higher than 50 on test two.")
test_two = test[["Test Two"]]
print(test_two[test_two["Test Two"] > 50])


print("3) Print the students and test_three columns for those who scored lower than 50 on test three.")
test_three = test[["Test Three"]]
print(test_three[test_three["Test Three"] < 50])

print("4) Print the students , test_two, and test_three columns for those who scored higher than 50 on test two AND lower than 50 on test three")
test_scores = test[["Test Two", "Test Three"]]
print(test_scores[
    (test_scores["Test Two"] > 50) &
    (test_scores["Test Three"] < 50)]
    )
