from functions import savenote, speak, add, sub, mul, div, search_wiki, exit1, remind, playVideo, history
from functions import wish, sendEmail, call, WinCalc, WinNotepad, recognize, saveTasks, search, openweb
import datetime
import tkinter as tk
from tkinter import *
from functions import playmusic
import sqlite3


def button_function():
    # speak("Hey ! {}, How may I help you?".format(ownerName))
    query = recognize().lower()
    print(query)
    db = sqlite3.connect("{}.db".format(ownerName))
    db.execute("CREATE TABLE IF NOT EXISTS history(user, command)")
    c = db.cursor()
    c.execute("INSERT INTO history(user, command) VALUES('{}', '{}')".format(ownerName, query))
    db.commit()
    c.close()
    db.close()



    if 'created' in query:
        speak("I was made by Tejas and Vedank.")

    elif 'owns' in query:
        speak("I am currently being owned by {}".format(ownerName))

    elif 'exit' in query:
        mainWindow.destroy()
        exit1()
    elif 'quit' in query:
        mainWindow.destroy()
        exit1()

    elif 'plus' in query:
        add(query)
    elif 'add' in query:
        add(query)
    elif '+' in query:
        add(query)

    elif 'minus' in query:
        sub(query)
    elif 'subtract' in query:
        sub(query)
    elif '-' in query:
        sub(query)

    elif 'multiplied by' in query:
        mul(query)
    elif 'times' in query:
        mul(query)
    elif ' x ' in query:
        mul(query)
    elif ' into ' in query:
        mul(query)

    elif 'divided by' in query:
        div(query)
    elif '/' in query:
        div(query)

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("The time is {}.".format(strTime))
    elif 'time is it' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("The time is {}.".format(strTime))

    elif 'email' in query:
        try:
            speak("What is the receiver's email address?")
            # to = recognize()
            # newTo = to.replace(" ", "")
            # print(newTo)
            newTo = "tmandre3@gmail.com"
            speak("What should i say ?")
            content = recognize()
            message = (content + "\n\n\nThis email has been sent by {}'s virtual assistant.".format(ownerName))
            sendEmail(newTo, message)
            speak("Email has been sent.")
        except Exception:
            speak("I'm sorry, failed to send the email.")

    elif 'who is' in query:
        search_wiki(query)

    elif 'call' in query:
        # new = [int(i) for i in query.split() if i.isdigit()]
        # call(new[0])
        # speak("calling" + str(new[0]))
        speak("Calling Tejas.")
        call('9021343679')

    elif query == "take a note":
        speak("What should i note ?")
        text = recognize()
        speak("What is the title of the note ?")
        title = recognize()
        speak("Your note will be saved in a minute")
        savenote(text, title)

    elif "play" in query:
        query = query.replace("play", "")
        playmusic(query)
    elif query == "play music":
        speak("Let me know the name of the song you want to play")
        song = recognize()
        playmusic(song)

    elif "calculator" in query:
        WinCalc()

    elif "notepad" in query:
        WinNotepad()

    elif "remind me" in query or "add a task" in query:
        newq = query.replace("remind me to", "")
        saveTasks(newq)

    elif "reminders" in query:
        remind()

    elif "on youtube" in query:
        newq = query.replace("play", "")
        newq1 = newq.replace("on youtube", "")
        playVideo(newq1)

    elif "go to" in query:
        newq = query.replace("go to", "")
        new1 = newq.replace("dot com", "")
        openweb(new1)

    elif "history" in query:
        history(ownerName)

    else:
        browser = search(query)



def voice():

    speak("Hey! I am Lisa. I can help you with various tasks. Before that, I'd like to know your name."
          " What is your name?")

    global ownerName
    ownerName1 = recognize()
    ownerName = ownerName1.replace("my name is ", "")
    wishme = wish()
    speak("{} {}. Click the microphone button if you need any help.".format(wishme, ownerName))
    introtext = "Hey! {} I am Lisa. Click the\nmicrophone" \
                " button if you need\nany assistance.".format(ownerName)
    global db

    global mainWindow
    mainWindow = tk.Tk()
    mainWindow.title("LISA - virtual assistant.")
    mainWindow.geometry("305x417+500+200")
    mainWindow.iconbitmap("Mic_icon.ico")
    mainWindow.resizable(False, False)

    lisaLabel = tk.Label(mainWindow, text=introtext, font=("Comic Sans MS", 14), relief="solid", bg="black",
                         fg="yellow", padx=18)
    lisaLabel.place(x=0, y=0)

    buttonImagePath = PhotoImage(file="1.png")
    micButton = tk.Button(mainWindow, height=300, width=300, command=button_function, image=buttonImagePath, bg='black')
    micButton.place(x=0, y=80)

    exitButton = tk.Button(mainWindow, text="EXIT", fg="yellow", bg="black", command=exit1, height=1,
                           width=27, font=("Arial", 14))
    exitButton.place(y=385, x=0)

    mainWindow.mainloop()
