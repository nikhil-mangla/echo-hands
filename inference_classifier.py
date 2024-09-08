

import pickle
import cv2
import mediapipe as mp
import numpy as np

# Load the trained model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# Start video capture
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Define labels dictionary
labels_dict = {0: '1', 1: '3', 2: '4', 3: '5', 4: '7', 5: '8', 6: '9', 7: 'A', 8: 'B', 9: 'Baby', 10: 'Brother',
               11: 'C', 12: 'D', 13: 'Dont_like', 14: 'E', 15: 'F', 16: 'Friend', 17: 'G', 18: 'H', 19: 'Help', 20: 'House',
               21: 'I', 22: 'J', 23: 'K', 24: 'L', 25: 'Like', 26: 'Love', 27: 'M', 28: 'Make', 29: 'More', 30: 'N', 31: 'Name',
               32: 'No', 33: 'Nothing', 34: 'O_OR_0', 35: 'P', 36: 'Pay', 37: 'Play', 38: 'Q', 39: 'R', 40: 'S', 41: 'Stop', 42: 'T',
               43: 'U', 44: 'V_OR_2', 45: 'W_OR_6', 46: 'With', 47: 'X', 48: 'Y', 49: 'Yes', 50: 'Z'}

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            data_aux = []
            x_ = []
            y_ = []

            # Draw landmarks and connections
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            # Extract and normalize landmarks for the detected hand
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) + 10
            y2 = int(max(y_) * H) - 10

            # Predict the character using the model
            if len(data_aux) == 42:  # Ensure the correct feature size
                prediction = model.predict([np.asarray(data_aux)])
               
                print(f"Prediction: {prediction}")  # Debugging: print the prediction output
                predicted_index = prediction[0]  # Prediction is usually an index
                predicted_character = labels_dict.get(predicted_index)  # Map index to character
              
                # Draw the bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()