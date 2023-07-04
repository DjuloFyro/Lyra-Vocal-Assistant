import vocal_assistant as va
import speech_recognition as sr

def chatting(vocal_assistant: va.VocalAssistant)-> None:
    audio_str = vocal_assistant.listen()
    if audio_str != "":
        response = vocal_assistant.think(audio_str)
        print(f"User: {audio_str}")
        print(f"Vocal Assistant: {response}")
        vocal_assistant.speak(response)

def listen_for_keyword(keyword:str, vocal_assistant: va.VocalAssistant) -> None:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=3)
        print("Listening...")
        audio = r.listen(source, timeout=3, phrase_time_limit=30)
    try:
        # Use Google Speech Recognition to convert audio to text
        text = r.recognize_google(audio)
        print("Recognized: " + text)

        # Check if the keyword is present in the recognized text
        if keyword in text.lower():
            chatting(vocal_assistant)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))



def main():
    keyword = "ok google"
    vocal_assistant = va.VocalAssistant()
    
    while True:
        listen_for_keyword(keyword=keyword, vocal_assistant=vocal_assistant)

if __name__ == "__main__":
    main()