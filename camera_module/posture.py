import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class PostureDetector:

    def __init__(self):

        self.detector = None

        try:
            base_options = python.BaseOptions(
                model_asset_path="pose_landmarker_full.task"
            )

            options = vision.PoseLandmarkerOptions(
                base_options=base_options,
                running_mode=vision.RunningMode.IMAGE
            )

            self.detector = vision.PoseLandmarker.create_from_options(options)

        except Exception:
            print("Pose model not loaded")


    def detect_posture(self, frame):

        if self.detector is None:
            return frame, "unknown"

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.detector.detect(mp_image)

        posture = "unknown"

        if result.pose_landmarks:

            landmarks = result.pose_landmarks[0]

            shoulder = landmarks[11]
            hip = landmarks[23]
            knee = landmarks[25]

            shoulder_hip = abs(shoulder.y - hip.y)
            hip_knee = abs(hip.y - knee.y)

            # standing
            if shoulder_hip > 0.15 and hip_knee > 0.15:
                posture = "standing"

            # sitting
            elif shoulder_hip > 0.15 and hip_knee < 0.10:
                posture = "sitting"

            # lying
            elif shoulder_hip < 0.05:
                posture = "lying"

            else:
                posture = "unknown"

        return frame, posture