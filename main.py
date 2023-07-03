import vocal_assistant as va


def main():
    vocal_assistant = va.VocalAssistant()
    audio_str = vocal_assistant.listen()
    response = vocal_assistant.think(audio_str)
    print(f"User: {audio_str}")
    print(f"Vocal Assistant: {response}")

    vocal_assistant.speak(response)


if __name__ == "__main__":
    main()