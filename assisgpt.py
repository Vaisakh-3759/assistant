import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import webbrowser
import random
import requests
import json

engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to audio and return text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

# Function to send email
def send_email():
    speak("Who is the recipient?")
    recipient = listen()
    speak("What should I say?")
    content = listen()

    # Your email credentials
    email = "your_email@gmail.com"
    password = "your_password"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, recipient, content)
    server.quit()
    speak("Email has been sent.")

# Function to get weather updates
def get_weather():
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("Please tell the city name.")
    city_name = listen()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather = data["weather"]
        weather_description = weather[0]["description"]
        speak(f"The temperature in {city_name} is {temperature} Kelvin, with humidity at {humidity}% and {weather_description}.")
    else:
        speak("City not found.")

# Main loop
speak("Hi! How can I assist you?")
while True:
    text = listen()
    if "send email" in text:
        send_email()
    elif "weather" in text:
        get_weather()
    elif "exit" in text:
        speak("Goodbye!")
        break
