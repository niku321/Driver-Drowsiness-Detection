import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re

root = tk.Tk()
root.configure(background="#BFEFFF")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")

username = tk.StringVar()
password = tk.StringVar()

# ++++++++++++++++++++++++++++++++++++++++++++
# For background Image
image2 = Image.open('d4.jpg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

def registration():
    from subprocess import call
    call(["python", "registration.py"])
    root.destroy()

def login():
    # Establish Connection
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        
        # Ensure the table exists (if not, create it)
        c.execute("""
            CREATE TABLE IF NOT EXISTS admin_registration
            (Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT, Gender TEXT, age TEXT, password TEXT)
        """)
        db.commit()
        
        # Find user if there is any matching record
        find_entry = 'SELECT * FROM admin_registration WHERE username = ? and password = ?'
        c.execute(find_entry, (username.get(), password.get()))
        result = c.fetchall()

        if result:
            ms.showinfo("Message", "Login successfully")
            root.destroy()

            # Call the next script after login
            from subprocess import Popen
            Popen(['python', 'Drowsiness_Detection1.py'])
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

frame_alpr = tk.LabelFrame(root, text=" ", width=500, height=350, bd=5, font=('times', 14, ' bold '), bg="pink")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=550, y=200)

title = tk.Label(frame_alpr, text="Login Here", font=("Times New Roman", 25), bd=5, bg="pink", fg="black")
title.place(x=130, y=0, width=230)

l2 = tk.Label(frame_alpr, text="username :", width=10, font=("Times new roman", 20, "bold"), bg="pink", fg="black")
l2.place(x=0, y=100)
t1 = tk.Entry(frame_alpr, textvar=username, width=14, font=('', 20), bg="pink")
t1.place(x=200, y=100)

l5 = tk.Label(frame_alpr, text="password :", width=10, font=("Times new roman", 20, "bold"), bg="pink", fg="black")
l5.place(x=0, y=150)
t4 = tk.Entry(frame_alpr, textvar=password, show='*', width=14, font=('', 20), bg="pink")
t4.place(x=200, y=150)

def window():
    root.destroy()

button1 = tk.Button(frame_alpr, text="Login", command=login, width=13, height=1, font=('times', 18, ' bold '), bg="#336699", fg="white")
button1.place(x=150, y=250)

root.mainloop()
