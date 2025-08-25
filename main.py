import speech_recognition as sr 
import webbrowser
import pyttsx3 
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    pass

if __name__ == "__main__" :
    speak("Initializing")
    while True:
        #listen the wake word
        # obtain audio from the microphone
        r = sr.Recognizer()
       
            
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand()
        except Exception as e:
            print("Error; {0}".format(e))
