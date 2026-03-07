from ultralytics import YOLO


class ObjectDetector:

    def __init__(self):

        # Load YOLO model
        self.model = YOLO("yolov8n.pt")

        # -----------------------------
        # WORK / STUDY OBJECTS
        # -----------------------------
        self.WORK_OBJECTS = [
            "laptop",
            "keyboard",
            "mouse",
            "book",
            "tv"  # used as monitor
        ]

        # -----------------------------
        # COMMUNICATION OBJECTS
        # -----------------------------
        self.COMMUNICATION_OBJECTS = [
            "phone",
            "remote"
        ]

        # -----------------------------
        # PERSONAL / BREAK OBJECTS
        # -----------------------------
        self.PERSONAL_OBJECTS = [
            "cup",
            "bottle",
            "wine glass",
            "bowl"
        ]

        # -----------------------------
        # FOOD OBJECTS
        # -----------------------------
        self.FOOD_OBJECTS = [
            "banana",
            "apple",
            "sandwich",
            "pizza",
            "cake",
            "donut"
        ]

        # -----------------------------
        # ENVIRONMENT OBJECTS
        # -----------------------------
        self.ENVIRONMENT_OBJECTS = [
            "chair",
            "backpack",
            "handbag",
            "person"
        ]

        # Combine all detectable objects
        self.ALLOWED_OBJECTS = (
            self.WORK_OBJECTS
            + self.COMMUNICATION_OBJECTS
            + self.PERSONAL_OBJECTS
            + self.FOOD_OBJECTS
            + self.ENVIRONMENT_OBJECTS
        )

    def detect(self, frame):

        results = self.model(frame, stream=True)

        objects = []

        for r in results:
            for box in r.boxes:

                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = self.model.names[cls]

                # Normalize YOLO labels
                if label == "cell phone":
                    label = "phone"

                # Confidence threshold
                if conf > 0.4:

                    if label in self.ALLOWED_OBJECTS:

                        if label not in objects:
                            objects.append(label)

        return objects