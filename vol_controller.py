

import cv2
import mediapipe as mp
from gesture_recognizer import GestureRecognizer

class VolumeControl:
    def __init__(self):
        self.recognizer = GestureRecognizer()
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

    def run(self):
        while self.cap.isOpened():
            success, img = self.cap.read()
            if not success:
                continue

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = self.hands.process(img_rgb)

            if result.multi_hand_landmarks:
                for handLms in result.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
                    landmarks = [(lm.x, lm.y, lm.z) for lm in handLms.landmark]
                    gesture = self.recognizer.recognize(landmarks)
                    cv2.putText(img, f'Gesture: {gesture}', (10, 70), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Volume Control", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    vc = VolumeControl()
    vc.run()
