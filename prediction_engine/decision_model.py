class DecisionModel:

    def decide(
        self,
        activity,
        emotion,
        work_type,
        habits=None,
        posture=None,
        productivity_score=None,
        focus_time=0,
        break_time=0,
        distraction_time=0
    ):

        activity = (activity or "").lower()
        emotion = (emotion or "neutral").lower()
        posture = (posture or "").lower()
        score = productivity_score if productivity_score is not None else 0

        # -------------------------
        # HIGH PRODUCTIVITY
        # -------------------------

        if score >= 85 and work_type == "organizational_work":
            return "Excellent productivity. Keep focusing on your task."

        # -------------------------
        # PRODUCTIVE WORK
        # -------------------------

        if work_type == "organizational_work":

            if activity == "coding":
                return "You are coding. Stay in deep focus mode."

            if activity == "typing":
                return "Keep typing and maintain your workflow."

            if activity == "reading":
                return "Continue reading and capture key ideas."

            if activity == "studying":
                return "Stay focused on your study session."

            if activity == "researching":
                return "Good research session. Note important points."

            if activity == "note_taking":
                return "Great—note taking improves retention."

            if activity == "video_call":
                return "Stay engaged in the conversation."

            return "Continue your productive work."

        # -------------------------
        # PERSONAL ACTIVITIES
        # -------------------------

        if work_type == "personal_activity":

            if activity == "hydrating":
                return "Good—stay hydrated to maintain energy."

            if activity == "eating":
                return "Enjoy your meal and recharge."

            if activity == "stretching":
                return "Stretching helps prevent fatigue."

            if activity == "walking":
                return "A short walk can refresh your focus."

            if activity == "relaxing":
                return "Short rest is fine. Return to work soon."

            if activity == "using_phone":
                return "Phone distraction detected. Try returning to work."

            if activity == "gaming":
                return "Gaming detected. Consider focusing on your tasks."

            return "Enjoy your short break."

        # -------------------------
        # NEUTRAL ACTIVITIES
        # -------------------------

        if work_type == "neutral":

            if activity == "idle":
                return "You appear idle. Start your next task."

            if activity == "sitting":
                return "You are sitting. Consider starting a task."

            if activity == "sleeping":
                return "Rest is important. Recharge for the next session."

            return "Choose one task and focus on it."

        # -------------------------
        # POSTURE BASED
        # -------------------------

        if posture == "lying" and activity != "sleeping":
            return "Sit upright to stay focused."

        if posture == "sitting" and emotion == "tired":
            return "Stand up and stretch for a minute."

        # -------------------------
        # DISTRACTION CHECK
        # -------------------------

        if activity in ["using_phone", "gaming", "watching_video"]:
            return "Avoid distractions and return to work."

        # -------------------------
        # DEFAULT RESPONSE
        # -------------------------

        return "Choose one task and give it your full focus."