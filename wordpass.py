import string
from random import *
from tkinter import *

def on_close():
    gui.destroy()

def generate():
    try:
        # punctuation = string.punctuation
        characters = string.ascii_letters + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        return password
    except:
        print("generate error")

def main():
    try:
        x = list(generate() + special_var.get())
        password = "".join(sample(x, len(x)))
        f = open("pass.txt", "a")
        f.write(password + "\n")
        f.close()
        print("password generated")
    except:
        print("main error")

gui = Tk()

Label(gui, text="Hello World! This is a password generator.", 
font=('arial',12,'bold')).pack()
Label(gui, text="password generated will be stored in a txt file created on the root dir of this script.", 
font=('arial',11,'italic')).pack()

special_var = StringVar()
special_label = Label(gui, text="Input punctuation/s to be added:", font=('arial',11,'normal')).pack(side = LEFT, fill = BOTH)
special_entry = Entry(gui, textvariable=special_var, font=('arial',11,'normal')).pack(side = LEFT, fill = BOTH)
special_button = Button(gui, text="Submit", font=('arial',11,'bold'), bg="cyan", command=main).pack(fill = BOTH)

gui.protocol("WM_DELETE_WINDOW", on_close)
gui.resizable(False, False)
gui.mainloop()