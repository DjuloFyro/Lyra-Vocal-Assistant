import openai
import speech_recognition as sr
import os
import pyttsx3



class VocalAssistant():
    def __init__(self):
        self.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        self.activated = False

    def listen(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            audio_str = r.recognize_whisper_api(audio, api_key=self.OPENAI_API_KEY)
        except sr.RequestError as e:
            print("Could not request results from Whisper API")

        print(audio_str)
        if "salut lyra" in audio_str.lower() or "salut lyra" in audio_str.lower():
            print("Lyra is activated")
            self.activated = True

        return audio_str
    
    def think(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.6
        )
        return dict(response.choices[0])["message"]["content"]

    def speak(self, audio: str) -> None:
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()
