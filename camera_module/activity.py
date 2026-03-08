import time


class ActivityClassifier:

    def __init__(self):
        self.last_activity = None
        self.activity_start = time.time()

    def classify(self, posture, objects, motion):

        objects = [o.lower() for o in objects]
        motion = motion == "moving" if isinstance(motion, str) else bool(motion)

        activity = "idle"

        # -------------------------
        # PRODUCTIVE WORK
        # -------------------------

        if "laptop" in objects and ("keyboard" in objects or "mouse" in objects):
            activity = "coding"

        elif "keyboard" in objects:
            activity = "typing"

        elif "book" in objects and ("pen" in objects or "pencil" in objects):
            activity = "studying"

        elif "book" in objects:
            activity = "reading"

        elif "laptop" in objects and "person" in objects:
            activity = "video_call"

        elif "laptop" in objects:
            activity = "researching"

        elif any(o in objects for o in ["notebook", "pad", "clipboard"]) and any(o in objects for o in ["pen", "pencil"]):
            activity = "note_taking"

        elif "laptop" in objects and posture == "sitting":
            activity = "browsing"

        # -------------------------
        # PHONE USAGE
        # -------------------------

        elif "cell phone" in objects or "phone" in objects:

            if posture == "standing" or motion:
                activity = "phone_call"
            else:
                activity = "using_phone"

        # -------------------------
        # FOOD / DRINK
        # -------------------------

        elif any(o in objects for o in ["cup", "bottle", "wine glass", "coffee"]):
            activity = "hydrating"

        elif any(o in objects for o in ["banana", "apple", "pizza", "sandwich", "cake", "donut", "orange"]):
            activity = "eating"

        # -------------------------
        # BODY MOVEMENT
        # -------------------------

        elif posture == "standing" and motion:
            activity = "walking"

        elif posture == "sitting" and motion and not any(o in objects for o in ["laptop", "keyboard", "book"]):
            activity = "stretching"

        # -------------------------
        # ENTERTAINMENT
        # -------------------------

        elif "remote" in objects:
            activity = "watching_video"

        elif "tv" in objects or "monitor" in objects:
            if "laptop" not in objects and "keyboard" not in objects:
                activity = "watching_video"

        elif any(o in objects for o in ["game controller", "controller"]):
            activity = "gaming"

        # -------------------------
        # REST
        # -------------------------

        elif posture == "lying":
            activity = "sleeping"

        elif posture == "standing":
            activity = "taking_break"

        elif posture == "sitting" and not motion:
            activity = "relaxing"

        elif posture == "sitting":
            activity = "sitting"

        # -------------------------
        # STABILITY FILTER
        # -------------------------

        if activity != self.last_activity:
            self.activity_start = time.time()
            self.last_activity = activity

        duration = time.time() - self.activity_start

        # prevent flickering predictions
        if duration < 2:
            activity = self.last_activity

        return activity