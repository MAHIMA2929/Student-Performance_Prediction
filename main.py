import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_excel("student_data.csv")

df["Result"] = df["Result"].map({
    "Fail": 0,
    "Pass": 1
})

X = df[["Study_Hours", "Attendance", "Previous_Score"]]
y = df["Result"]

model = DecisionTreeClassifier()
model.fit(X, y)

with open("student_pass_fail_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model created successfully!")
