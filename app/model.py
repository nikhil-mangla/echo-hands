import pickle

# Load the trained model
with open('models/model.pickle', 'rb') as f:
    model = pickle.load(f)

def predict(data):
    # Preprocess and convert data to the appropriate format
    # Example: Convert to float or other necessary transformations
    data = [float(data)]
    
    # Make prediction
    prediction = model.predict([data])[0]
    return prediction
    