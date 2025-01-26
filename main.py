import speech_recognition as sr
import pyttsx3
import webbrowser
import music_library
import requests
import google.generativeai as genai

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "1a59b5c5ce9f4df89ed75bd48605d994"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def AIcode(command):
    # Use Gemini API to generate a response
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(command)
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/?authuser=0")
    elif "roti banana" in c.lower():
        speak("mein nahi karsakta")
    elif c.lower().startswith("play"):
        # Split the command, remove "play", and join the rest to form the song name
        song = ' '.join(c.lower().split()[1:])  # Takes everything after "play"
        
        try:
            link = music_library.music[song]  # Fetch the link from the dictionary
            webbrowser.open(link)  # Open the link in the browser
        except KeyError:
            speak(f"Sorry, I couldn't find the song {song}. Please check the music library.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the json data
            data = r.json()
            # Extract the articles
            articles = data.get('articles',[])
            # Voicing the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Pass it to the AI
        output = AIcode(c)
        speak(output)
  

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while True:
        # Wait for the word 'Jarvis' or any command
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("Listening...")

            try:
                # Listen with a timeout of 2 seconds
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                print("Recognizing...")
                
                # Use Google's recognizer 
                word = recognizer.recognize_google(audio)  
                if(word.lower() == "jarvis"):
                    speak("At your command sir")
                    #Listen for command
                    with sr.Microphone() as source:
                        print("Jarvis Activated")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
                
            except sr.WaitTimeoutError:
                print("No speech detected, please try again.")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
