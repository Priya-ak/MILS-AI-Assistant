from deepface import DeepFace

class EmotionDetector:

    def __init__(self):
        pass

    def detect_emotion(self, frame):

        emotion = "unknown"

        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )

            emotion = result[0]['dominant_emotion']

        except:
            emotion = "unknown"

        return emotion