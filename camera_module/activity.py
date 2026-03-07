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

        elif "book" in objects and ("pen" in objects or "pencil" in objects or "cell phone" not in objects):
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
        # COMMUNICATION
        # -------------------------

        elif "phone" in objects:
            if posture == "standing" or motion:
                activity = "phone_call"
            else:
                activity = "using_phone"

        # -------------------------
        # PERSONAL / BREAK
        # -------------------------

        elif any(o in objects for o in ["cup", "bottle", "wine glass", "coffee"]):
            activity = "hydrating"

        elif any(o in objects for o in ["banana", "apple", "pizza", "sandwich", "cake", "donut", "orange"]):
            activity = "eating"

        elif posture == "sitting" and motion and not any(o in objects for o in ["laptop", "keyboard", "book"]):
            activity = "stretching"

        elif posture == "standing" and motion and not any(o in objects for o in ["laptop", "phone"]):
            activity = "walking"

        elif posture == "sitting" and not motion and not any(o in objects for o in ["laptop", "keyboard", "book", "phone"]):
            activity = "relaxing"

        # -------------------------
        # DISTRACTION
        # -------------------------

        elif "remote" in objects:
            activity = "watching_video"

        elif "tv" in objects or "monitor" in objects:
            if "laptop" not in objects and "keyboard" not in objects:
                activity = "watching_video"

        elif any(o in objects for o in ["game controller", "controller", "remote"]):
            activity = "gaming"

        elif "phone" in objects and posture == "sitting":
            activity = "using_phone"

        # -------------------------
        # MOVEMENT / POSTURE
        # -------------------------

        elif posture == "standing" and motion:
            activity = "walking"

        elif posture == "standing":
            activity = "taking_break"

        elif posture == "lying":
            activity = "sleeping"

        elif posture == "sitting" and motion:
            if any(o in objects for o in ["laptop", "keyboard", "book"]):
                activity = "researching"
            else:
                activity = "stretching"

        elif posture == "sitting":
            activity = "sitting"

        # -------------------------
        # TIME STABILITY
        # -------------------------

        if activity != self.last_activity:
            self.activity_start = time.time()
            self.last_activity = activity

        duration = time.time() - self.activity_start

        if duration > 60 and activity == "thinking":
            activity = "idle"

        return activity
