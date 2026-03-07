from ultralytics import YOLO

class ObjectDetector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):

        results = self.model(frame)

        objects = []

        for r in results:
            for box in r.boxes:

                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = self.model.names[cls]

                if conf > 0.6:

                    allowed = [
                        "cell phone",
                        "laptop",
                        "keyboard",
                        "mouse",
                        "book",
                        "cup",
                        "bottle",
                        "fork",
                        "spoon"
                    ]

                    if label in allowed:
                        objects.append(label)

        return objects