import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)  # speed of speech
engine.setProperty("volume", 1.0)  # volume 0.0 - 1.0

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    except Exception as e:
        print(f"Mic error: {e}")
        return input("Type your command: ").lower()

    try:
        command = r.recognize_google(audio, language="en-US")
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

# 🎵 Play random music from a folder
def play_music():
    song_path = "C:/Users/Jevie/OneDrive/Music/Your.mp3"
    if os.path.exists(song_path):
        os.startfile(song_path)
        return "Playing Your Song"
    else:
        return "Song not found. Please check the file path."


def main():
    speak("Hello, Erl Princess baho kag lubot")
    
    # Website dictionary
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "github": "https://github.com",
        "spotify": "https://open.spotify.com"
    }
    
    while True:
        command = listen()

        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")

        elif "open" in command:
            found = False
            for site in sites:
                if site in command:
                    speak(f"Opening {site}")
                    webbrowser.open(sites[site])
                    found = True
                    break
            if not found:
                speak("Sorry, I don't know that site. Please add it to my list.")

        elif "play music" in command:
            speak("Playing music")
            result = play_music()
            speak(result)

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
