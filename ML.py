import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Configure API
genai.configure(api_key="AIzaSyCi-whtT8ZRr06um2iyTMABRFh0xUgX6t8")

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# Speech recognition
recognizer = sr.Recognizer()

# Text-to-speech
engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening... 🎤")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""

def chatbot():
    speak("Hello! I am your Gemini voice assistant. Say exit to stop.")

    while True:
        user_input = listen()

        if not user_input:
            speak("Sorry, I didn't catch that.")
            continue

        if user_input in ["exit", "quit", "bye"]:
            speak("Goodbye!")
            break

        try:
            response = model.generate_content(user_input)
            reply = response.text
            speak(reply)

        except Exception as e:
            print("Error:", e)
            speak("Something went wrong.")

if __name__ == "__main__":
    chatbot()