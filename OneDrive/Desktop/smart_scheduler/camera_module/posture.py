import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class PostureDetector:
    def __init__(self):
        base_options = python.BaseOptions(
            model_asset_path="pose_landmarker_full.task"
        )

        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE
        )

        self.detector = vision.PoseLandmarker.create_from_options(options)

    def detect_posture(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.detector.detect(mp_image)

        posture_label = "Unknown"

        if result.pose_landmarks:
            landmarks = result.pose_landmarks[0]

            left_shoulder = landmarks[11]
            left_hip = landmarks[23]
            left_knee = landmarks[25]

            # Calculate vertical distances
            shoulder_hip_dist = abs(left_shoulder.y - left_hip.y)
            hip_knee_dist = abs(left_hip.y - left_knee.y)

            # Improved logic
            if shoulder_hip_dist > 0.15 and hip_knee_dist > 0.15:
                posture_label = "Standing"
            elif shoulder_hip_dist > 0.15 and hip_knee_dist < 0.1:
                posture_label = "Sitting"
            else:
                posture_label = "Unknown"

        return frame, posture_label