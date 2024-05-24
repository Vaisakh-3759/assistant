import speech_recognition as sr
import pyttsx3
import os
import datetime
#from textblob import TextBlob as TB
import psutil
from plyer import notification
import webbrowser
import random
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import time
import keyboard
import time
from camera import *
import numpy as np
import requests

tinvar=["what time is it now","what is the time now","give me the  time"]
dinvar=["what day is it today","what is the day today","give me the  date"]

def speak(aud):
       x=pyttsx3.init()
       voices=x.getProperty("voices")
       x.setProperty("voice",voices[1].id)
       x.setProperty('rate',150)
       x.setProperty('volume',0.5)
       x.say(aud)
       x.runAndWait()

def search():
       speak("what would you like me to search")
       srh=getaud2()
       url="https://google.com/search?q="+srh
       speak("here you go sir")
       webbrowser.open(url)
def search2(srh):
       url="https://"+srh
       webbrowser.open(url)
def search3(engine):
       sr=engine.split()
       if t.count('what do you know about')>0 :
              word='what do you know about'
              srch=("".join([i for i in sr if i not in  word]))
              url="https://google.com/search?q="+srch
              webbrowser.open(url)
              speak("here is what i found sir")
       elif t.count('tell me about') >0:
              word='tell me about'
              srch=("".join([i for i in sr if i not in  word]))
              url="https://google.com/search?q="+srch
              webbrowser.open(url)
              speak("here is what i found sir")

      
def youtube(vid):
       sr=vid.split()
       if vid.count("go to youtube and search"):
              word='go to youtube and search'
              srch=("".join([i for i in sr if i not in  word]))
              url="https://www.youtube.com/results?search_query="+srch
              webbrowser.open(url)
              speak("here is what i found sir")
       elif vid.count("search on youtube"):
              word='search on youtube'
              srch=("".join([i for i in sr if i not in  word]))
              url="https://www.youtube.com/results?search_query="+srch
              webbrowser.open(url)
              speak("here is what i found sir")
       elif vid.count("open youtube and search"):
              word='open youtube and search'
              srch=("".join([i for i in sr if i not in  word]))
              url="https://www.youtube.com/results?search_query="+srch
              webbrowser.open(url)
              speak("here is what i found sir")
def time():
       timed=datetime.datetime.now()
       hr=int(timed.strftime("%I"))
       mi=int(timed.strftime("%M"))
       sec=int(timed.strftime("%S"))
       ampm=datetime.datetime.now().strftime("%p").lower()
       if ampm=="am":
              tp='the time is',sec,'seconds past',hr,mi,'inthe morning'
              print(tp)
              speak(tp)
       elif ampm=='pm':
              tp='the time is',sec,'seconds past',hr,mi,'in the evening'
              print(tp)
              speak(tp)
       
def battery():     
       battery=psutil.sensors_battery()
       plugged=battery.power_plugged
       percent=int(battery.percent)
       bt=percent,"% remaining sir!!"
       speak(bt)
def typer(t):
       sr=t.split()
       word='type'
       srch=("".join([i for i in sr if i not in  word]))
       keyboard.write(srch)
       keyboard.press_and_release('enter')
def tracker(num):
       chn=phonenumbers.parse(num,'CH')
       print("The locaton is in",geocoder.description_for_number(chn,'en'))

       sn=phonenumbers.parse(num,'RO')
       print('and the service provider is',carrier.name_for_number(sn,'en'))
def battery2():
       battery=psutil.sensors_battery()
       plugged=battery.power_plugged
       percent=int(battery.percent)
       if plugged==False:
              if percent<=35:
                     notification.notify(title="Battery",message=str(percent)+"% remaining",timeout=14)
                     speak("battery is going down sir. please plug in")
       
def getaud2():
       r=sr.Recognizer()
       with sr.Microphone() as source:
              aud=r.listen(source)
              said=""       
              try:
                     said=r.recognize_google(aud,language='en-US')
                     print(said.lower())
              except Exception as ex:
                     if ex=='recognition connection failed: [Errno 11001] getaddrinfo failed':
                            speak('sorry sir! internet is not connected')
                     else:
                            print (ex)
       return said.lower()
def getaud():
       r=sr.Recognizer()
       with sr.Microphone() as source:
              aud=r.record(source,duration=5)
              said=""       
              try:
                     said=r.recognize_google(aud,language='en-US')
                     print(said.lower())
              except Exception as ex:
                     print (ex)
       return said.lower()
def wishme():
       hr=datetime.datetime.now().hour
       if hr>6 and hr<=12:
              speak("good morning sir")
              speak('i am always here for your servese sir!!! ')
       elif hr>12 and hr<=16:
              speak("good after noon sir")
              speak('i am always here for your servese sir!!! ')
       elif hr>16 and hr<22:
              speak("good evening sir")
              speak('i am always here for your servese sir!!! ')
       else :
              speak("good night sir. it's time to sleep ")
              speak("but still you can acess me sir. do you wish to acess me")
              yn=getaud2()
              print(yn)
              if yn.count("yes"):
                     t=getaud()
                     speak('i am always here for your servese sir!!! ')
              elif yn.count("no"):
                     quit()
def get_weather():
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("Please tell the city name.")
    city_name = getaud2()
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

def alarm():
       timed=datetime.datetime.now()
       hr=int(timed.strftime('%I'))
       mi=int(timed.strftime('%M'))
       ap=datetime.datetime.now().strftime("%p").lower()
       tp=hr,':',mi,',',ap
       print(tp)
       speak('sir, give me the title of the alarm please')
       title=input('enter title')
       speak('sir, type the hour please')
       h=int(input('enter the hour'))
       speak('and the minute ')
       m=input('enter the minute')
       speak('finally wether a,m or p,m please')
       amp=input('enter am or pm')
       amp=amp.lower()

       speak('alarm is set sir')
       
       if ap=='pm':
              h=h+12
       while (1==1):
              if (h==datetime.datetime.now().hour and
                  m==datetime.datetime.now().minute):
                     speak('sir its an alarm. the title is  '+ title)
                     break


def date():
       dt=datetime
       dat=dt.datetime.now()
       yer=int(dat.strftime('%y'))+2000
       mon=int(dat.strftime('%m'))
       day=dat.strftime('%A')
       mont=["januery",'february','march','april','may','june','july','august','september','october','november','december']
       month=mont[mon-1]
       dat=int(dat.strftime('%d'))
       datez='today is',dat,month,yer,day
       print(datez)
       speak(datez)
       
def cmd(t):
       if t.count("calculator"):
              os.system("calc")
       elif t.count("command prompt"):
              os.system("start")
       elif t.count(" controle panal"):   
              os.system("C:\\Windows\\system32\\control")
       elif t.count(" task manager"):
              os.system("taskmgr.exe")
       elif t.count(" controle panal"):
              os.system("C:\\Windows\\system32\\control")
       elif t.count(" this pc") or t.count("my computer"):
              os.system("explorer.exe")
       elif t.count("chrome"):
              os.system("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
       elif t.count("youtube") or t.count("you tube") :
              search2('www.youtube.com')
       elif t.count("whatsapp") or t.count("whatsapp") :
              search2('web.whatsapp.com/')
       elif t.count("facebook") or t.count("fb") or t.count("face book"):
              search2('www.facebook.com/')
       elif t.count("python"):
              os.startfile("D:\\vrn\\python")
       elif t.count("movie section") or t.count("telegram desktop") or t.count("movie"):
              os.startfile('C:\\Users\\vaisa\\Downloads\\Telegram Desktop')
       elif t.count("watched movie section") or t.count("watched folder")or t.count("watched movie"):
              os.startfile("D:\\VRN\\APPS\\Telegram Desktop\\Telegram Desktop\\WATCHED")
       elif t.count("premiere") or t.count("adobe premiere pro"):
              os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Premiere Pro 2020.lnk")
       elif t.count("photoshop") or t.count("adobe photoshop"):
              os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Photoshop CC 2019.lnk")
       elif t.count("meet") or t.count("googlemeet") or t.count("google meet"):
              search2('meet.google.com/')
       

              
print('ready')
battery2()
while True:
    ww=getaud2()
    if ww.count("friday") >0 or ww.count("wake up ") >0:
        speak("hello sir")
        while True:
            t=getaud2()
            if t.count("open") or t.count("start") or t.count("play") or t.count("run") >0:
                cmd(t)
            elif t.count("today") or t.count("date") or t.count("day") >0 or t in dinvar:
                date()
            elif t.count("go to youtube and search") or t.count("search on youtube")or t.count("open youtube and search")>0:
                youtube(t)
            elif t.count("search") or t.count("google") or t.count("browser") >0:
                search()
            elif  t.count("what do you know about") or t.count("tell me about")>0:
                search3(t)
            elif t.count('alarm')>0:
                alarm()
            elif t.count("type") or t.count("text to")  >0:
                typer(t)
            elif t.count("time") >0  or t in tinvar:
                time()
            elif t.count("hello")>0:
                speak("hello. how do you do sir!")

            elif t.count("battery")>0:
                battery()
            elif t.count("track") or t.count("phone number") or t.count("number") >0:
                tracker()
            elif  t.count("cam") or t.count("camera") or t.count("video") >0:
                camera()
                
            elif t.count('quit') or t.count('close the programme') >0:
                
                quit() 

#future update()
'''elif  t.count("you are") or t.count("good") or t.count("bad") or t.count("best")>0:
getphrase(t)
 '''











