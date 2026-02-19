import cv2
import mediapipe as mp
import csv
import os

# ==============================
# AVAILABLE GESTURES
# ==============================
GESTURES = [
    "thumbs_up",
    "thumbs_down",
    "love_you",
    "stop",
    "ok",
    "rock_on",
    "pointing_up",
    "call_me",
    "strength",
    "heart"
]

print("\nAvailable Gestures:")
for g in GESTURES:
    print(" -", g)

gesture_name = input("\nEnter gesture name exactly as above: ").lower()

if gesture_name not in GESTURES:
    print("❌ Invalid gesture name!")
    exit()

# ==============================
# Dataset folder
# ==============================
folder_path = "dataset"
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, f"{gesture_name}.csv")

# ==============================
# Mediapipe Setup
# ==============================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hand_detector = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)

# ==============================
# Camera
# ==============================
cap = cv2.VideoCapture(0)

sample_count = 0
max_samples = 300   # 🔥 more samples = better accuracy

print(f"\n📸 Collecting data for: {gesture_name}")
print("Press ESC to stop early.\n")

while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hand_detector.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            landmarks = []

            for lm in handLms.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)

            # save landmarks
            with open(file_path, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(landmarks)

            sample_count += 1

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # display info
    cv2.putText(img, f"Gesture: {gesture_name}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.putText(img, f"Samples: {sample_count}/{max_samples}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Data Collection", img)

    if cv2.waitKey(1) == 27 or sample_count >= max_samples:
        break

cap.release()
cv2.destroyAllWindows()

print(f"\n✅ Collected {sample_count} samples for '{gesture_name}'")
