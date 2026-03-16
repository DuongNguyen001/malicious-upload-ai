import os
import pickle
from feature_extractor import extract_features
from sklearn.ensemble import RandomForestClassifier

X = []
y = []

dataset_path = "dataset"

for label in ["benign","malicious"]:

    folder = os.path.join(dataset_path,label)

    for file in os.listdir(folder):

        path = os.path.join(folder,file)

        try:
            features,_ = extract_features(path)

            X.append(features)

            if label == "malicious":
                y.append(1)
            else:
                y.append(0)

        except:
            pass


model = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    random_state=42
)

model.fit(X,y)

os.makedirs("model",exist_ok=True)

pickle.dump(model,open("model/model.pkl","wb"))

print("Model trained successfully")
