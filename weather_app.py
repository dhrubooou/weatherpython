import os
import pyttsx3
import requests
import json

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        imp=input("Enter (y) to Start else (n) : ")
        if imp=="n" or imp=='N':
            text_to_speech("Thank you Sir.")
            break
        else:
            text = input("Enter the City : ")
            url=f'http://api.weatherapi.com/v1/current.json?key=2fc24b69be5844fc847213927242605&q={text}'
            r=requests.get(url)
            dic=json.loads(r.text)
            ans1=dic['current']['condition']['text']
            ans2=dic['current']['temp_c']
            final=f'The current weather in {text} is {ans1} and Temperature is {ans2} degree Celcius'
            print(ans1)
            print(ans2)
            text_to_speech(final)
        