import speech_recognition as sr


class SpeechListener:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):

        text = ""

        try:
            with self.microphone as source:

                print("Adjusting for noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                print("Listening now...")
                audio = self.recognizer.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=4
                )

            text = self.recognizer.recognize_google(audio)

        except:
            pass

        return text


def extract_intent(text):

    text = text.lower()

    intent = "general"
    urgency = "normal"

    if "study" in text:
        intent = "study"

    if "work" in text:
        intent = "work"

    if "sleep" in text:
        intent = "sleep"

    if "gym" in text or "exercise" in text:
        intent = "fitness"

    if "urgent" in text or "tomorrow" in text:
        urgency = "high"

    return intent, urgency