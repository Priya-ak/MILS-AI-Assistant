class FatigueDetector:

    def detect(self, emotion, activity):

        if emotion in ["sad", "tired"]:
            return True

        if activity == "Active / Break":
            return False

        return False