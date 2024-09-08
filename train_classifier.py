import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load the dataset
try:
    with open('./image_data.pickle', 'rb') as f:
        data_dict = pickle.load(f)
except FileNotFoundError:
    print("Error: 'image_data.pickle' file not found.")
    exit()
except Exception as e:
    print(f"Error loading pickle file: {e}")
    exit()

# Check the content of the pickle file
data = np.asarray(data_dict.get('data', []))
labels = np.asarray(data_dict.get('labels', []))

# Print dataset statistics
print(f"Number of samples: {len(data)}")
print(f"Number of labels: {len(labels)}")

# Ensure there is data to train on
if len(data) == 0 or len(labels) == 0:
    print("Error: The dataset is empty.")
    exit()

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Check if the split resulted in empty training or testing sets
if len(x_train) == 0 or len(x_test) == 0:
    print("Error: The resulting train or test set is empty after splitting.")
    exit()

# Initialize and train the classifier
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Make predictions and evaluate the model
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)

print(f'{score * 100:.2f}% of samples were classified correctly!')

# Save the trained model
try:
    with open('model.p', 'wb') as f:
        pickle.dump({'model': model}, f)
except Exception as e:
    print(f"Error saving model: {e}")
