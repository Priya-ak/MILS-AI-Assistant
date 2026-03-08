class WorkClassifier:

    def __init__(self):

        # Productive / work related
        self.ORGANIZATIONAL_WORK = [
            "coding",
            "typing",
            "reading",
            "studying",
            "researching",
            "note_taking",
            "video_call",
            "browsing",
            "writing",
            "presentation",
            "discussion"
        ]

        # Personal / break activities
        self.PERSONAL_ACTIVITY = [
            "using_phone",
            "phone_call",
            "hydrating",
            "drinking",
            "eating",
            "stretching",
            "walking",
            "relaxing",
            "watching_video",
            "gaming",
            "taking_break"
        ]

        # Neutral activities
        self.NEUTRAL_ACTIVITY = [
            "idle",
            "sitting",
            "thinking",
            "moving",
            "sleeping"
        ]

    def classify(self, activity):

        activity = (activity or "").lower()

        if activity in self.ORGANIZATIONAL_WORK:
            return "organizational_work"

        elif activity in self.PERSONAL_ACTIVITY:
            return "personal_activity"

        elif activity in self.NEUTRAL_ACTIVITY:
            return "neutral"

        return "unknown"