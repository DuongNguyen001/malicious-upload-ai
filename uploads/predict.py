import pickle
from feature_extractor import extract_features

# load model
model = pickle.load(open("model/model.pkl", "rb"))

def predict_file(path):

    features = extract_features(path)

    result = model.predict([features])[0]

    if result == 1:
        prediction = "MALICIOUS"
    else:
        prediction = "SAFE"

    return prediction, details
