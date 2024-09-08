import os
import pickle
import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)

DATA_DIR = '/Users/nikhilmangla/Downloads/test proj/ASL[]'  # Path to your raw images
OUTPUT_FILE = 'image_data.pickle'

data = []
labels = []

# Ensure the directory exists
if not os.path.exists(DATA_DIR):
    print(f"Error: Directory '{DATA_DIR}' does not exist.")
    exit()

# Process each directory and image
for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    
    if not os.path.isdir(dir_path):
        print(f"Skipping non-directory {dir_path}.")
        continue
    
    print(f"Processing directory: {dir_path}")

    for img_path in os.listdir(dir_path):
        img_full_path = os.path.join(dir_path, img_path)
        
        # Read image
        img = cv2.imread(img_full_path)
        if img is None:
            print(f"Warning: Unable to read image '{img_full_path}'. Skipping.")
            continue
        
        # Convert image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        
        # Check for detected hand landmarks
        if results.multi_hand_landmarks:
            print(f"Hand landmarks detected in '{img_full_path}'")
            for hand_landmarks in results.multi_hand_landmarks:
                data_aux = []
                x_ = []
                y_ = []
                
                # Extract hand landmark positions
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)
                
                # Normalize coordinates
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))
                
                # Append data and labels
                data.append(data_aux)
                labels.append(dir_)
        else:
            print(f"Warning: No hand landmarks detected in image '{img_full_path}'.")

# Save data to pickle file
try:
    with open(OUTPUT_FILE, 'wb') as f:
        pickle.dump({'data': data, 'labels': labels}, f)
    print(f"Data successfully saved to '{OUTPUT_FILE}'.")
except Exception as e:
    print(f"Error: Failed to save data - {e}")
