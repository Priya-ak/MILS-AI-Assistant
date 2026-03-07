from gtts import gTTS
import pygame
import os
import time


class VoiceResponse:

    def __init__(self):

        pygame.mixer.init()

        self.last_message = None
        self.last_speak_time = 0
        self.cooldown = 15
        self.audio_file = "assistant_voice.mp3"

    def speak(self, text):

        current_time = time.time()

        if text != self.last_message and (current_time - self.last_speak_time) > self.cooldown:

            print("Assistant:", text)

            tts = gTTS(text=text, lang="en")
            tts.save(self.audio_file)

            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

            if os.path.exists(self.audio_file):
                os.remove(self.audio_file)

            self.last_message = text
            self.last_speak_time = current_time