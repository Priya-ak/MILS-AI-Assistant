class DecisionModel:

    def decide(self, activity, emotion, work_type, habits=None, posture=None,
               productivity_score=None, focus_time=0, break_time=0, distraction_time=0):
        habits = habits or {}
        posture = (posture or "").lower()
        score = productivity_score if productivity_score is not None else 0
        # Align work_type with classifier output
        is_productive = work_type in ("organizational_work", "productive")
        is_break = work_type in ("personal_activity", "break")
        is_neutral = work_type in ("neutral", "unknown")

        # -----------------------------
        # PRODUCTIVITY-SCORE-BASED (when stats available)
        # -----------------------------
        if score < 30 and activity == "idle":
            return "Your focus time is low—try one 25-minute block on your main task"
        if score < 40 and distraction_time > focus_time and distraction_time > 1:
            return "Distraction time is building—put the phone away and focus for 20 min"
        if score >= 85 and is_productive:
            return "You're in a great flow—keep going"

        # -----------------------------
        # DISTRACTION DETECTION
        # -----------------------------
        if activity in ["using_phone", "gaming", "watching_video", "browsing_social_media"]:
            return "Avoid phone distraction and return to work"

        # -----------------------------
        # POSTURE-BASED
        # -----------------------------
        if posture in ["slouching", "bad_posture", "hunched"]:
            return "Straighten your back and adjust your screen height to avoid strain"
        if posture == "lying" and activity != "sleeping":
            return "Sit up at your desk to stay focused and productive"
        if posture == "sitting" and emotion == "tired":
            return "Stand up for a minute or take a short walk to refresh"

        # -----------------------------
        # PRODUCTIVE WORK
        # -----------------------------
        if is_productive:
            if activity in ["typing", "coding", "writing"]:
                return "Continue your deep focus work"
            if activity == "meeting":
                return "Focus on the meeting"
            if activity == "presentation":
                return "Deliver your presentation confidently"
            if activity == "reading":
                return "Keep taking notes or summarize key points to retain more"
            if activity == "researching":
                return "Stay in research mode—note key sources and one next action"
            if activity == "studying":
                return "Stick to one topic for 25 minutes, then recap"
            if activity == "note_taking":
                return "Good—capture main ideas and one action item per section"
            if activity == "browsing":
                return "Use this for focused research; avoid unrelated tabs"
            if activity == "video_call":
                return "Keep the conversation focused and productive"
            if activity == "taking_break" and "taking_break" in habits:
                return "You take smart breaks—drink some water and get back stronger"

        # -----------------------------
        # COMMUNICATION
        # -----------------------------
        if activity in ["talking", "discussion", "video_call", "phone_call"]:
            return "Keep the conversation focused and productive"

        # -----------------------------
        # PERSONAL BREAK ACTIVITIES (hydration, movement, rest)
        # -----------------------------
        if activity in ["drinking", "hydrating"]:
            return "Good—stay hydrated, water helps focus and energy"
        if activity == "eating":
            return "Good time to recharge—hydrate after eating too"
        if activity == "taking_break":
            return "Good time to drink some water and stretch—you'll focus better"
        if activity == "walking":
            return "A short walk helps—grab water on the way back"
        if activity == "stretching":
            return "Great—stretching and hydration keep you sharp"
        if activity == "relaxing":
            return "Short rest is fine—drink some water, set a 5-min timer, then return"

        # -----------------------------
        # IDLE / SITTING / THINKING
        # -----------------------------
        if activity == "idle":
            if emotion in ["sad", "tired"]:
                return "Take a short break—drink some water and stretch"
            if emotion == "neutral":
                return "Quick tip: drink some water, then pick one small task"
            return "Start with one task—you've got this"

        if activity == "sitting":
            if emotion == "tired":
                return "You are sitting—sit upright, drink some water, then start one small task"
            if is_productive:
                return "You are seated and ready—focus on your current task for the next 20 minutes"
            return "You are just sitting—choose one task and begin, even for 5 minutes"

        if activity in ["thinking", "looking_around"]:
            return "Drink some water, then plan your next task—small steps add up"

        # -----------------------------
        # SLEEPING
        # -----------------------------
        if activity == "sleeping":
            return "Rest well so you can be productive tomorrow"

        # -----------------------------
        # HABIT-AWARE FALLBACKS
        # -----------------------------
        if habits:
            frequent_break = any(
                "break" in str(k).lower() or "idle" in str(k).lower()
                for k in habits
            )
            if frequent_break and not is_productive:
                return "Try a 25-minute focus block, then a 5-minute break"
            if "typing" in habits or "coding" in habits:
                return "Your usual focus activity is nearby—get into flow"
            if "reading" in habits:
                return "You read often—finish this block then take a short break"

        # -----------------------------
        # DEFAULTS
        # -----------------------------
        if is_productive:
            return "Keep up the productive work"
        if is_break:
            return "Enjoy your break—return when you are ready"
        if is_neutral:
            return "Choose one task and give it your focus for the next 20 minutes"
        if emotion == "tired":
            return "Consider a short break or a glass of water"
        if emotion == "sad":
            return "Take a moment for yourself; small steps still count"
        return "Choose one task and give it your focus for the next 20 minutes"
