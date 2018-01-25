import Tkinter
import tkMessageBox
from random import randint

secret = randint(0, 100)

def check_guess():
    user_guess = int(user_text.get())

    if user_guess == secret:
        text = "Correct!"
    elif user_guess > secret:
        text = "Higher"
    else:
        text = "Lower"

    tkMessageBox.showinfo("Info text", text)


window = Tkinter.Tk()


greeting = Tkinter.Label(window, text="Guess the secret number")
greeting.pack()

user_text = Tkinter.Entry(window)
user_text.pack()

submit = Tkinter.Button(window, text="Submit", command=check_guess)
submit.pack()

window.mainloop()