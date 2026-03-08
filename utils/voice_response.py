import asyncio
import edge_tts
import pygame
import time
import uuid
import threading


class VoiceResponse:

    def __init__(self):

        self.voice = "en-IN-NeerjaNeural"

        pygame.mixer.init()

        self.last_decision = None
        self.last_time = 0

        self.speaking = False


    async def _generate_audio(self, text, filename):

        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(filename)


    def _play_audio(self, filename):

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

        self.speaking = False


    def _speak_thread(self, decision):

        filename = f"voice_{uuid.uuid4().hex}.mp3"

        asyncio.run(self._generate_audio(decision, filename))

        print("MILS:", decision)

        self._play_audio(filename)


    def speak(self, decision):

        if not decision:
            return

        now = time.time()

        if decision != self.last_decision:

            self.last_decision = decision
            self.last_time = now

            if not self.speaking:

                self.speaking = True
                threading.Thread(target=self._speak_thread, args=(decision,), daemon=True).start()


        elif now - self.last_time >= 7:

            self.last_time = now

            if not self.speaking:

                self.speaking = True
                threading.Thread(target=self._speak_thread, args=(decision,), daemon=True).start()