import win32com.client
import speech_recognition as sr
import os
import webbrowser
from together import Together
import datetime
import random
import requests

chatStr = ""


def chat(query):
    global chatStr
    print(chatStr)

    client = Together(api_key="")
    chatStr += f"Shreyas: {query}\nChikki: "

    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3-70b-chat-hf",  # Valid Together AI model
            messages=[{"role": "user", "content": chatStr}],
            max_tokens=500,
            temperature=0.7,
            stream=False
        )

        reply = response.choices[0].message.content
        say(reply)

        chatStr += f"{reply}\n"
        return reply

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."


def ai(prompt):
    text = f"Ai response for prompt: {prompt} \n *******************************\n\n"
    client = Together(api_key="")

    response = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",  # Valid Together AI model
        messages=[{"role": "user", "content": prompt }],
        max_tokens=500,
        temperature=0.7,
        stream=False
    )

    print(response.choices[0].message.content)
    text += response.choices[0].message.content
    if not os.path.exists("Ai files"):
        os.mkdir("Ai files")

    with open(f"Ai files/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def get_weather(city):
    API_KEY = "1970e8a3ec16456db5f221406251403"
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"  # Disable air quality data for faster response
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            return f"Error: {data['error']['message']}"

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        feels_like = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]

        weather_report = (f"The weather in {location}, {country} is {condition}. "
                          f"The temperature is {temp_c}°C, but it feels like {feels_like}°C. "
                          f"Humidity is at {humidity}%.")

        return weather_report

    except Exception as e:
        return f"Error fetching weather data: {e}"


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry bout that"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Chikki A.I.")
    while True:
        print("Listening..")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["instagram","https://www.instagram.com"],["Udemy","https://www.udemy.com"],["facebook","https://www.facebook.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}..")
                webbrowser.open(site[1])
        if "open spotify" in query or "open music" in query:
            spotify_path = os.path.join(os.getenv("APPDATA"), "Spotify", "Spotify.exe")
            if os.path.exists(spotify_path):
                say("Opening Spotify...")
                os.startfile(spotify_path)


        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        elif "open camera" in query:
            say("Opening camera...")
            os.system("start microsoft.windows.camera:")

        elif "using Artificial Intelligence".lower() in query.lower():
            ai(prompt = query)

        elif "Chikki Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr=""

        elif "weather" in query.lower():
            city = query.split("weather in")[-1].strip()
            if city:
                weather_info = get_weather(city)
                say(weather_info)
                print(weather_info)
            else:
                say("Please specify a city.")



        else:
            print("Chatting...")
            chat(query)

        # say(query)
