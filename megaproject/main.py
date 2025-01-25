import speech_recognition as sr
import webbrowser
import pyttsx3



recognizer = sr.Recognizer()
ttsx = pyttsx3.init()


def speak(text):
    
    ttsx.say(text)
    ttsx.runAndWait()

def processcomand(c):
    print(f"Processing command: {c}")
   
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        print("Opening Google...")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        print("Opening YouTube...")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        print("Opening Facebook...")
    
        
if __name__ == "__main__":
    speak("Initializing Nova....")
    while True:

        print("Listening to the wake word...")
        try:    
            with sr.Microphone() as source:
                audio = recognizer.listen(source,timeout=5 , phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                print(f"You say :{word}")
            


                if(word.lower() == "nova"):
                    speak("Yes,how can i help you")
                    print("Nova active...")
        #    listening for command 
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(f"Command Received:{command}")
                    processcomand(command)

        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except Exception as e:
            print(f"Error: {e}")
                
       

        

