'''
Author: Krushna Dike
Date: 01 Oct 2021
Pupose: Desktop Assistant
'''
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import subprocess
import random
import smtplib
from requests import get
import pywhatkit as kit
import cv2

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("Computer: Good Morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        print("Computer: Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Computer: Good Evening!")
        speak("Good Evening!")

    speak("I'm siri 2 point o. Please tell me how may I help you.")


def takeCommand():
    # It will take an microphone input and rturn the string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again please...\n")
        return "None"
    return query

def sendMail(to, content):
    server = smtplib.SMTP("smtp.@mail.com")
    server.ehlo()
    server.starttls()
    server.login("shraddhakapur35@gmail.com", "Shraddha@1234")
    server.sendmail("shraddhakapur35@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        # Siri Commands
        if "hi siri" in query:
            speak("I'm Listening sir...")

        elif "hey siri" in query:
            speak("I'm Listening sir...")

        elif "hi" in query:
            speak("I'm Listening sir...")

        elif "hai" in query:
            speak("I'm Listening sir...")

        elif "hay" in query:
            speak("I'm Listening sir...")

        elif "hey" in query:
            speak("I'm Listening sir...")

        elif "krishna dk" in query:
            speak("Krushna dk is an computer engineer and he is very very good boy...!")

        elif "who are you" in query:
            speak("I'm siri 2 point o. Your virtual desktop assistant. Please tell me how may I help you.")

        elif "wikipedia" in query:
            speak("Searching on wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open chrome" in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "open file explorer" in query:
            filePath = "C:\\Users\\dikek\\PycharmProjects\\TutorialsPy"
            os.startfile(filePath)

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif "open whatsapp" in query:
            waPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://web.whatsapp.com/"
            subprocess.Popen(waPath)

        elif "open youtube" in query:
            yoPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "www.youtube.com"
            subprocess.Popen(yoPath)

        elif "open instagram" in query:
            inPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "www.instagram.com"
            subprocess.Popen(inPath)

        elif "open mail" in query:
            maPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://mail.google.com/mail/u/1/#inbox"
            subprocess.Popen(maPath)

        elif "send message" in query:
            kit.sendwhatmsg("+919284013243", "Hi, this is msg from python",18,28)
            speak("Message has been sent succefully!")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k= cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cap.destroyAllWindows()

        elif "open classroom" in query:
            clPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://classroom.google.com/u/1/h"
            subprocess.Popen(clPath)

        elif "open attendance" in query:
            sposPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://docs.google.com//forms//d//e//1FAIpQLSfMkkkrQ2b9BPgb0RNlpXslZqKLxyzZl9IlYm1m2OzqbolbuA//viewform"
            subprocess.Popen(sposPath)

        elif "open google translator" in query:
            trPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://translate.google.co.in/"
            subprocess.Popen(trPath)

        elif "open stackoverflow" in query:
            stackPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "www.stackoverflow.com"
            subprocess.Popen(stackPath)

        elif "open code" in query:
            codePath = "C:\\Users\\dikek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open notepad" in query:
            notePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notePath)

        elif "open editing software" in query:
            softPath = "C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe"
            os.startfile(softPath)

        elif "open calculator" in query:
            os.system("calc.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "C:\\Users\\dikek\\Music\\ShareMe"
            songs = os.listdir(music_dir)
            ms = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[ms]))

        elif "the photos" in query:
            pics_dir = "E:\\pics"
            pics = os.listdir(pics_dir)
            pc = random.randint(0, len(pics))
            os.startfile(os.path.join(pics_dir, pics[pc]))

        elif "send mail to krishna" in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand().lower()
                to = "krushna.dike@mmit.edu.in"
                sendMail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                speak("Sorry Mr.Krushna. I'm not able to send that mail!")

        elif "ip address" in query:
            Ip = get("https://api.ipify.org").text
            speak(f"Your Ip address is {Ip}")

        elif "siri quit" in query:
            print("Thanks for using siri 2.0. Have a good day ahead Mr. Krushna.")
            speak("Thanks for using siri 2 point o. Have a good day ahead Mr. Krishna.")
            exit()