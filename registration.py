import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random



window = tk.Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.title("REGISTRATION FORM")
window.configure(background="black")



  
  
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
policeno = tk.IntVar()
value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM admin_registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO admin_registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.askquestion("askquestion", "Are you sure?")
            ms.askokcancel("askokcancel", "Want to continue?")
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            
            from subprocess import call
            call(["python", "log.py"])
            
            
            window.destroy()

#####################################################################################################################################################

            
 
#def register():
 #    from subprocess import call
  #   call(["python", "lecture_login.py"])


# assign and define variable
# def login():

#####For background Image
image2 = Image.open('d3.jpg')
image2 = image2.resize((1800,1200), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

frame_alpr = tk.LabelFrame(text="  ", width=750, height=600, bd=5, font=('times', 14, ' bold '),bg="white")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=370, y=30)

image2 = Image.open('reg.jpg')
image2 = image2.resize((750,600), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=370, y=30)
 
logo_label=tk.Label()
logo_label.place(x=0,y=55)

# l1 = tk.Label(window, text="Create an Account",width=20, font=("Times new roman", 15, "bold"),bg="white", fg="black")
# l1.place(x=600, y=100)

# that is for label1 registration

l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="pink")
l2.place(x=550, y=150)
t1 = tk.Entry(window, textvar=Fullname,bd=2, width=20, font=('', 15),bg="pink")
t1.place(x=800, y=150)
# that is for label 2 (full name)


l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="pink")
l3.place(x=550, y=200)
t2 = tk.Entry(window, textvar=address, bd=2,width=20, font=('', 15),bg="pink")
t2.place(x=800, y=200)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="pink")
l5.place(x=550, y=250)
t4 = tk.Entry(window, textvar=Email, bd=2,width=20, font=('', 15), bg="pink")
t4.place(x=800, y=250)
# that is for email address

l6 = tk.Label(window, text="Phone No :", width=12, font=("Times new roman", 15, "bold"), bg="pink")
l6.place(x=550, y=300)
t5 = tk.Entry(window, textvar=Phoneno,bd=2, width=20, font=('', 15),bg="pink")
t5.place(x=800, y=300)
# phone number
l7 = tk.Label(window, text="Gender :", bd=2,width=12, font=("Times new roman", 15, "bold"), bg="pink")
l7.place(x=550, y=350)

# t6 = tk.Entry(window,bd=2, width=15, font=('', 20))
# t6.place(x=800, y=350)
# gender
tk.Radiobutton(window, text="Male", padx=1,  bg="pink", font=("bold", 15), variable=var, value=1).place(x=820,
                                                                                                                y=350)
tk.Radiobutton(window, text="Female", padx=1,  bg="pink", font=("bold", 15), variable=var, value=2).place(
    x=920, y=350)

l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="pink")
l8.place(x=550, y=400)
t6 = tk.Entry(window, textvar=age,bd=2, width=20, font=('', 15),bg="pink")
t6.place(x=800, y=400)

l4 = tk.Label(window, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="pink")
l4.place(x=550, y=450)
t3 = tk.Entry(window, textvar=username, bd=2,width=20, font=('', 15),bg="pink")
t3.place(x=800, y=450)


l9 = tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="pink")
l9.place(x=550, y=500)
t9 = tk.Entry(window, textvar=password,bd=2 ,width=20, font=('', 15),bg="pink", show="*")
t9.place(x=800, y=500)

l10 = tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"),bg="pink")
l10.place(x=550, y=550)

t10 = tk.Entry(window, textvar=password1, bd=2,width=20, font=('', 15), bg="pink",show="*")
t10.place(x=800, y=550)

btn = tk.Button(window, text="Register", bg="#008000",font=("",20),fg="white", width=15, height=0, command = insert)
btn.place(x=650, y=630)

#btn = tk.Button(window, text="login", bg="#192841",font=("",20),fg="white", width=9, height=0, command=login)
#btn.place(x=350, y=600)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()