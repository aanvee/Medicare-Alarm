import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening... Please speak your command.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print(" Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        print(" Could not connect to the speech recognition service.")
        return None
