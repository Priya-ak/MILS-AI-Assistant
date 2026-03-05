import cv2

from camera_module.posture import PostureDetector
from camera_module.object_detector import ObjectDetector
from camera_module.activity import ActivityClassifier

from emotion_module.emotion import EmotionDetector
from prediction_engine.decision_model import DecisionModel

from utils.work_classifier import WorkClassifier
from utils.voice_response import VoiceResponse

from planner.day_planner import DayPlanner


# Initialize modules
posture_detector = PostureDetector()
object_detector = ObjectDetector()
activity_classifier = ActivityClassifier()

emotion_detector = EmotionDetector()
decision_model = DecisionModel()

work_classifier = WorkClassifier()
voice = VoiceResponse()

planner = DayPlanner()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # Emotion Detection
    emotion = emotion_detector.detect_emotion(frame)

    # Posture Detection
    try:
        posture = posture_detector.detect_posture(frame)
    except:
        posture = "unknown"

    # Object Detection
    try:
        objects = object_detector.detect(frame)
    except:
        objects = []

    # Activity Detection
    activity = activity_classifier.classify(posture, objects)

    print("Detected Objects:", objects)
    print("Activity:", activity)

    # Work Classification
    work_type = work_classifier.classify(activity)

    # AI Decision
    decision = decision_model.decide(activity, emotion, work_type)

    planner.plan(decision)
    voice.speak(decision)

    # Display
    cv2.putText(frame, f"Emotion: {emotion}", (30,50),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.putText(frame, f"Activity: {activity}", (30,90),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.putText(frame, f"Work: {work_type}", (30,130),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)

    cv2.putText(frame, f"Decision: {decision}", (30,170),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("MILS AI Assistant", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()