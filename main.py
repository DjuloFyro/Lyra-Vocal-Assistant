import vocal_assistant as va


def main():
    vocal_assistant = va.VocalAssistant()
    audio_str = vocal_assistant.listen()
    print(audio_str)


if __name__ == "__main__":
    main()