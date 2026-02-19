import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

X = []
y = []

for file in os.listdir("dataset"):
    gesture = file.split(".")[0]
    data = pd.read_csv(f"dataset/{file}", header=None)

    for row in data.values:
        X.append(row)
        y.append(gesture)

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved as model.pkl")
