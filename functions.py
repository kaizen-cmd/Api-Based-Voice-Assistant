from selenium import webdriver
import time
import speech_recognition as sr
import pyttsx3
import datetime
from datetime import date
import smtplib
import wikipedia
from twilio.rest import Client
import tkinter as tk
import subprocess
from playsound import playsound
import sqlite3
from tkinter import *
import requests
import bs4


def listen():
    with sr.Microphone() as source:
        global r
        r = sr.Recognizer()
        r.energy_threshold = 400
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 0.5
        audio = r.listen(source)
    return audio


def recognize():
    playsound('sound.mp3')
    voice = listen()
    try:
        command = r.recognize_google(voice, language='en-in')
        return command
    except Exception:
        speak("Sorry i didn't catch that. Please repeat")
        return recognize()


def exit1():
    speak("Sad to see you go! Bye!")
    exit(0)


def stopmusic(browser):
    browser.quit()


def savenote(text, title):
    chromebrowser = 'chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path=chromebrowser, chrome_options=options)
    browser.get("https://accounts.google.com/AddSession?continue=https://keep.google.com/#identifier")
    time.sleep(5)
    browser.find_element_by_id('Email').send_keys("your_email")
    browser.find_element_by_id("next").click()
    time.sleep(5)

    browser.find_element_by_name("Passwd").send_keys("your_password")
    time.sleep(1)
    browser.find_element_by_id("signIn").click()
    time.sleep(10)

    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]"
                                  "/div[6]").click()
    time.sleep(3)

    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]"
                                  "/div[7]").send_keys(text)
    time.sleep(1)

    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/di"
                                  "v[1]/div[5]").send_keys(title)
    time.sleep(10)

    browser.quit()


def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\IVONA 2 Voice Emma22")
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()


def search_wiki(query):
    newQuery = query.replace("who is", "")
    result = wikipedia.summary(newQuery, sentences=2)
    speak(result)


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        w = "Good Morning"
    elif 12 <= hour < 18:
        w = "Good Afternoon"
    else:
        w = "Good Evening"
    return w


def add(query):
    new = [int(i) for i in query.split() if i.isdigit()]
    result = new[0] + new[1]
    speak("{} plus {} is {}.".format(str(new[0]), str(new[1]), str(result)))



def sub(query):
    new = [int(i) for i in query.split() if i.isdigit()]
    result = new[0] - new[1]
    speak("{} minus {} is {}.".format(str(new[0]), str(new[1]), str(result)))


def div(query):
    new = [int(i) for i in query.split() if i.isdigit()]
    result = new[0] / new[1]
    speak("{} divided by {} is {}.".format(str(new[0]), str(new[1]), str(result)))


def mul(query):
    new = [int(i) for i in query.split() if i.isdigit()]
    result = new[0] * new[1]
    speak("{} times {} is {}.".format(str(new[0]), str(new[1]), str(result)))


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your_email', 'your_password')
    server.sendmail('your_email', to, content)
    server.close()


def call(number):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    client = Client(account_sid, auth_token)

    client.calls.create(
        url='link to youe xml file',
        to='+91' + str(number),
        from_='you_twilio_number'
    )


def playmusic(song):
    chromebrowser = 'chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path=chromebrowser, chrome_options=options)
    newsong = song + " with lyrics"
    browser.get('https://www.youtube.com')
    print("Navigated to youtube")
    browser.find_element_by_id('search').send_keys(newsong)
    print("Searching..")
    browser.find_element_by_id('search-icon-legacy').click()
    time.sleep(2)
    speak("Now playing {}".format(song))
    stopWin = tk.Tk()
    stopWin.geometry("305x70+500+650")
    stopWin.title(song)
    stopWin.iconbitmap("play.ico")
    tk.Label(stopWin, text="playing "+song, font=("Comic Sans MS", 16), relief="solid", bg="black", fg="yellow").pack()
    tk.Button(stopWin, command=lambda: [stopmusic(browser), stopWin.destroy()],
              text="STOP", height=34, width=34, bg="black", font=("Comic Sans MS", 10),
              fg="yellow").pack()
    browser.find_element_by_id('description-text').click()
    stopWin.mainloop()


def WinNotepad():
    subprocess.Popen("C:\\Windows\\System32\\notepad.exe")


def WinCalc():
    subprocess.Popen("C:\\Windows\\System32\\calc.exe")


def saveTasks(task):
    f = open("reminders.txt", "a")
    date1 = date.today()
    f.write("You have {} on {}.".format(task, str(date1)))
    f.close()


def remind():
    f = open("reminders.txt", "r")
    content = f.read()
    speak(content)


def playVideo(video):
    chromebrowser = 'chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chromebrowser)
    newsong = video
    browser.get('https://www.youtube.com')
    time.sleep(1)
    browser.find_element_by_id('search').send_keys(newsong)
    print("Searching..")
    browser.find_element_by_id('search-icon-legacy').click()


def search(query):
    chromebrowser = 'chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chromebrowser)
    browser.get("https://www.google.com/search?q={}&rlz=1C1CHBF_enIN790IN790&oq=football&aqs="
                "chrome..69i57j0l5.5535j0j1&sourceid=chrome&ie=UTF-8".format(query))
    text = browser.find_element_by_xpath('//*[@id="rhs_block"]/div[1]/div[1]/div[1]/div[1]/div'
                                         '/div[2]/div/div[2]/div/div/div/div/span[1]')
    toread = text.get_attribute('Description')
    speak(toread)
    return browser


def openweb(site):
    chromebrowser = 'chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chromebrowser)
    browser.get("https://www.{}.com/".format(site))


def history(ownerName):
    string = ""
    db = sqlite3.connect("{}.db".format(ownerName))
    cursor = db.cursor()
    cursor.execute("SELECT * FROM history")
    s = "User         |      Command"
    for name, command in cursor:
        string = string + "{}         |      {}\n".format(name, command)
    cursor.close()
    db.close()
    root = tk.Toplevel()
    root.geometry("500x700+400+70")
    root.title("Previous Commands")
    c = Canvas(root, width=500, height=700)
    c.place(x=0, y=0)
    history = PhotoImage(file="history.png")
    c.create_image(0, 0, anchor=NW, image=history)
    c.create_text(250, 100, text=s, font=("Bahnschrift Condensed", 30, "bold underline"), anchor=CENTER)
    c.create_text(250, 350, text=string, font=("Bahnschrift Condensed", 20, "bold"), anchor=CENTER)
    Button(c, text="Close", font=("Bahnschrift Condensed", 15, "bold"),
           fg="white", bg="black", command=root.destroy).place(x=250, y=600, anchor=CENTER)
    root.mainloop()


def readinfo(query):

    res = requests.get("https://www.google.com/search?q={}&oq={}"
                       "&aqs=chrome.0.69i59j0l7.2286j0j7&sourceid=chrome&ie=UTF-8".format(query, query))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    lis = soup.select('div')
    des = lis[25].getText()
    stop = 0
    string = ""
    for i in des:
        if i == ".":
            stop += 1
        if stop == 2:
            break
        string += i
    speak(string + ".")
