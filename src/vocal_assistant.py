import speech_recognition as sr
import os
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

import pyttsx3


GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

class VocalAssistant():
    def __init__(self):
        self.OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        self.template = """Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
        
        Assistant is aware that human input is being transcribed from audio and as such there may be some errors in the transcription. It will attempt to account for some words being swapped with similar-sounding words or phrases. Assistant will also keep responses concise, because human attention spans are more limited over the audio channel since it takes time to listen to a response.
        
        Human: {input}

        Information from internet, you can use it if you think it's necessary: {internet_search}
        Assistant:"""

    def listen(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print("TING TING")
            audio = r.listen(source, timeout=5, phrase_time_limit=30)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Whisper API")

        return ""
    
    def think(self, input_text: str) -> str:
        prompt = PromptTemplate(input_variables=['input', 'internet_search'], template=self.template)

        # Search on the internet
        search = GoogleSearchAPIWrapper(k=2)
        tool = Tool(
            name="Google Search",
            description="Search Google for recent results.",
            func=search.run,
        )
        internet_response = tool.run(input_text)

        chat_chain = LLMChain(
            llm=OpenAI(temperature=0),
            prompt=prompt,
            verbose=True,
        )
        response = chat_chain.predict(input=input_text, internet_search=internet_response)
        return response
    
    def speak(self, audio: str) -> None:
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()
