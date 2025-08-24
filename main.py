import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    print(f"Command received: {command}")

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn’t understand that.")

if __name__ == "__main__":
    speak("Initializing")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes, I am listening")  # finish speaking first

                # only after speaking, start listening
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)


        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
        except Exception as e:
            print(f"Error: {e}")
