import cv2
from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

mp_hands = hands
mp_draw = drawing_utils

cap = cv2.VideoCapture(0)
hand_detector = mp_hands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hand_detector.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking Test", img)

    if cv2.waitKey(1) == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
