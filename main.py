from tkinter import *
from Voice import voice
from tkinter import messagebox


class Placeholder_State(object):
    __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color',\
                'placeholder_font', 'with_placeholder'


def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color = normal_color
    state.normal_font = normal_font
    state.placeholder_color = color
    state.placeholder_font = font
    state.placeholder_text = placeholder
    state.with_placeholder = True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg=state.normal_color, font=state.normal_font)

            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg=state.placeholder_color, font=state.placeholder_font)

            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg=color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state


def sub_func():
    global usernam
    usernam = username.get()
    global passwor
    passwor = password.get()

def exec():
    sub_func()
    if usernam == "admin" and passwor == "admin":
        root.destroy()
        voice()
    else:
        messagebox.showinfo("Error", "Wrong Credentials")

if __name__ == '__main__':

    root = Tk()
    root.geometry("960x641+310+110")
    root.resizable(False, False)
    root.title("Lisa - Login")
    root.iconbitmap("Mic_icon.ico")

    rootc = Canvas(root, height=641, width=960, highlightthickness=1, highlightbackground="black")
    rootc.pack()
    photo = PhotoImage(file="back.png")

    rootc.create_image(0, 0, anchor=NW, image=photo)

    username = Entry(rootc, font=("Bahnschrift Condensed", 20, "bold"), relief="raised", bd=7, fg="green")
    username.place(x=90, y=230)
    add_placeholder_to(username, "Username")

    password = Entry(rootc, font=("Bahnschrift Condensed", 20, "bold"), relief="raised", bd=7, fg="green")
    password.place(x=90, y=310)
    add_placeholder_to(password, "Password")

    submit = Button(rootc, text="Submit", font=("Comic Sans Ms", 10, "bold"),
           relief="raised", bg="black", bd=5, fg="white", command=exec)
    submit.place(x=190, y=380)

    new = Button(rootc, text="New User? Register here", font=("Comic Sans Ms", 10, "bold"),
                 bg="black", fg="white")
    new.place(x=135, y=440)

    rootc.create_line(200, 130, 800, 130, width=3, fill="purple")
    rootc.create_text(740, 110, text="About", fill="black", font=("Times", 30, "bold"))
    desc = "Hello I'm Lisa.\n\nI can make your\n\neverday tasks easier\n\nand quicker."
    rootc.create_text(700, 350, text=desc, font=("Bahnschrift Condensed", 25, "bold"))

    mainloop()

