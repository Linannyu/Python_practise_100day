import pandas as pd

students = pd.DataFrame({
"Name": ["Alex", "Sam", "Jordan"],
"Grade": [95, 88, 92],
"Sport": ["Soccer", "Basketball", "Track"]
})
print(students["Grade"])


