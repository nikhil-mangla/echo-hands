import pickle
import matplotlib.pyplot as plt
import numpy as np

# Load the existing data from the train_data file
with open('image_data.pickle', 'rb') as f:
    train_data = pickle.load(f)

data = np.array(train_data['data'])
labels = np.array(train_data['labels'])

# Example of how to visualize the data
def plot_landmarks(landmarks, label):
    x_coords = landmarks[0::2]  # Extract X coordinates
    y_coords = landmarks[1::2]  # Extract Y coordinates

    plt.figure(figsize=(6, 6))
    plt.scatter(x_coords, y_coords, marker='o')
    plt.title(f'Hand Landmarks for label: {label}')
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.grid(True)
    plt.show()

# Plot the first data sample for demonstration
if data.size > 0 and labels.size > 0:
    plot_landmarks(data[0], labels[0])
