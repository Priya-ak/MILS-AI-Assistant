class ActivityClassifier:

    def classify(self, posture, objects):

        objects = [o.lower() for o in objects]

        # ORGANIZATIONAL WORK
        if "laptop" in objects:
            return "working"

        if "keyboard" in objects or "mouse" in objects:
            return "typing"

        if "book" in objects:
            return "reading"

        # PERSONAL ACTIVITIES
        if "cell phone" in objects:
            return "using_phone"

        if any(o in objects for o in ["cup", "bottle", "fork", "spoon"]):
            return "eating"

        if posture == "lying":
            return "sleeping"

        if posture == "standing":
            return "moving"

        return "idle"