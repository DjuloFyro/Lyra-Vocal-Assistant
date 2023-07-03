import openai
import speech_recognition as sr
import os


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

class VocalAssistant():
    def __init__(self):
        return

    def listen(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            audio_str = r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)
        except sr.RequestError as e:
            print("Could not request results from Whisper API")
        return audio_str

    def speak(self) -> None:
        pass

    def think(self) -> None:
        pass

