class WorkClassifier:

    def __init__(self):

        # Organizational / productive work
        self.ORGANIZATIONAL_WORK = [
            "coding",
            "typing",
            "writing",
            "meeting",
            "researching",
            "reading",
            "studying",
            "presentation",
            "discussion",
            "note_taking",
            "browsing",
            "video_call",
        ]

        # Personal / break / distraction
        self.PERSONAL_ACTIVITY = [
            "using_phone",
            "phone_call",
            "drinking",
            "hydrating",
            "eating",
            "stretching",
            "relaxing",
            "watching_video",
            "gaming",
            "walking",
        ]

        # Neutral / passive
        self.NEUTRAL_ACTIVITY = [
            "idle",
            "thinking",
            "taking_break",
            "sitting",
            "moving",
            "sleeping",
        ]

    def classify(self, activity):

        activity = (activity or "").lower()

        if activity in self.ORGANIZATIONAL_WORK:
            return "organizational_work"

        if activity in self.PERSONAL_ACTIVITY:
            return "personal_activity"

        if activity in self.NEUTRAL_ACTIVITY:
            return "neutral"

        return "unknown"
