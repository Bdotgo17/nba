def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def make_prediction(model, features):
    return model.predict(features)

def main(model_path, features):
    model = load_model(model_path)
    prediction = make_prediction(model, features)
    return prediction

if __name__ == "__main__":
    import sys
    model_path = sys.argv[1]
    features = sys.argv[2]  # This should be parsed into the appropriate format
    prediction = main(model_path, features)
    print(prediction)