import cv2
import numpy as np


class MotionDetector:

    def __init__(self):
        self.prev_frame = None

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_frame is None:
            self.prev_frame = gray
            return "idle"

        frame_delta = cv2.absdiff(self.prev_frame, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

        motion_score = np.sum(thresh)

        self.prev_frame = gray

        if motion_score > 500000:
            return "moving"
        else:
            return "idle"

    def detect_motion(self, frame):
        return self.detect(frame)