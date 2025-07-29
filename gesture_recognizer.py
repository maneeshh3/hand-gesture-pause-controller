
class GestureRecognizer:
    def __init__(self):
        pass

    def get_finger_state(self, landmarks):
        # Dummy logic — replace with actual MediaPipe-based finger state calc
        return [1, 1, 1, 1, 1]  # Simulated open palm for testing

    def recognize(self, landmarks):
        fingers = self.get_finger_state(landmarks)

        if fingers == [0, 1, 1, 0, 0]:
            return "Peace"
        elif fingers == [1, 1, 1, 1, 1]:
            return "Pause"
        return "Unknown"
