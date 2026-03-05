from speech_module.speech import SpeechListener, extract_intent

listener = SpeechListener()

while True:

    text = listener.listen()

    if text != "":

        intent, urgency = extract_intent(text)

        print("You said:", text)
        print("Intent:", intent)
        print("Urgency:", urgency)
        print("----------------------")