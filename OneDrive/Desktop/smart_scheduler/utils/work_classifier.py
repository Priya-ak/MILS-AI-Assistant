class WorkClassifier:

    def classify(self, activity):

        organizational = [
            "working",
            "typing",
            "reading",
            "studying",
            "writing"
        ]

        personal = [
            "using_phone",
            "sleeping",
            "eating",
            "moving",
            "idle"
        ]

        if activity in organizational:
            return "organizational_work"

        if activity in personal:
            return "personal_activity"

        return "unknown"