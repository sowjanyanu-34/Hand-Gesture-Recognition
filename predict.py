import cv2
from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

mp_hands = hands
mp_draw = drawing_utils
hand_detector = mp_hands.Hands()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hand_detector.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            landmarks = []
            for lm in handLms.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)

            prediction = model.predict([landmarks])
            cv2.putText(img, prediction[0], (10,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0,255,0), 2)

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Sign Language Recognition", img)

    if cv2.waitKey(1) == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
