import cv2
from emotion_module.emotion import EmotionDetector

detector = EmotionDetector()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    emotion = detector.detect_emotion(frame)

    cv2.putText(
        frame,
        f"Emotion: {emotion}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()