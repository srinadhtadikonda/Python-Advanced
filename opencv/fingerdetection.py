import cv2
import mediapipe as mp

# Initialize Mediapipe Hands and Drawing Utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Define indices for finger tips (Mediapipe's hand landmarks)
tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky finger tips

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()  # Capture frame-by-frame
    img = cv2.flip(img, 1)  # Flip the frame horizontally for a mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB
    results = hands.process(img_rgb)  # Process the RGB frame to detect hands

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []  # List to hold landmarks positions (x, y)
            for id, lm in enumerate(hand_landmarks.landmark):
                # Get image dimensions and scale landmarks to pixel values
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            # Check which fingers are up
            fingers = []

            # Thumb (special case: compare x-coordinates instead of y)
            if lm_list[tip_ids[0]][0] < lm_list[tip_ids[0] - 1][0]:
                fingers.append(1)  # Thumb is up
            else:
                fingers.append(0)  # Thumb is down

            # Other fingers
            for id in range(1, 5):
                if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id] - 2][1]:
                    fingers.append(1)  # Finger is up
                else:
                    fingers.append(0)  # Finger is down

            # Count the number of fingers up
            total_fingers = fingers.count(1)

            # Display the count on the image
            cv2.putText(img, f'Fingers: {total_fingers}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Draw landmarks and connections
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show the image with the finger count
    cv2.imshow("Finger Counter", img)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
