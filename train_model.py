import os
import pickle

from sklearn.ensemble import RandomForestClassifier
from feature_extractor import extract_features

X = []
y = []

# load dataset
def load_dataset(folder, label):

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        try:
            features = extract_features(path)

            X.append(features)
            y.append(label)

        except Exception as e:
            print("Error reading:", path)


# benign = 0
load_dataset("dataset/benign", 0)

# malicious = 1
load_dataset("dataset/malicious", 1)

print("Total samples:", len(X))

# train model
model = RandomForestClassifier(n_estimators=100)

model.fit(X, y)

# save model
pickle.dump(model, open("model/model.pkl", "wb"))

print("Model trained and saved!")
