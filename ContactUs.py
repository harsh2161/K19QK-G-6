from tkinter import *
from tkinter import messagebox

import mysql.connector
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("1400x750+60+10")
root.configure(background='black')
bg = ImageTk.PhotoImage(file="loginimage.jpg")
img = Label(root, image=bg)
img.place(x=0, y=0)
root.title(" Car Recommendation System(Contact Us)")

# Variables defined here
email = StringVar()
Username = StringVar()
description = StringVar()
phone = StringVar()
# Variables defined


# Function Defined here
def ContactUs():
    pass


def Login():
    root.destroy()
    os.system('python Login.py')


def SearchVechile():
    root.destroy()
    os.system('python SearchVechile.py')


def About():
    root.destroy()
    os.system('python About.py')


def Home():
    root.destroy()
    os.system('python PythonOngoingProject.py')


def submit():
    if email.get() == "" or Username.get() == "" or description.get() == "" or phone.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=root)
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
        mycursor = mydb.cursor()
        mycursor.execute(f"insert into contact_us values('{email.get()}','{Username.get()}','{phone.get()}','{description.get()}')")
        mycursor.execute("commit")
        messagebox.showinfo("info", "Successfully completed", parent=root)


# Navigation Bar
Label(root, text="  Car Recommendation System  ", pady=23, fg='white', bg='black', font=("Comic Sans MS", 25, "bold")).grid(row=0, column=0, columnspan=3)
Home_button = Button(root, text="Home", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Home).grid(row=0, column=3, columnspan=1)
About_button = Button(root, text="About", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=About).grid(row=0, column=4, columnspan=1)
Search_vehicle_button = Button(root, text="(Recommendation)\nSearch vehicle", padx=20, pady=4, font=('', 20, ''), bg='black', fg='white', command=SearchVechile).grid(row=0, column=5, columnspan=1)
Login_button = Button(root, text="Login", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Login).grid(row=0, column=6, columnspan=1)
Contact_button = Button(root, text="Contact Us", padx=20, pady=20, font=('', 20, ''), bg='black', fg='blue', command=ContactUs).grid(row=0, column=7, columnspan=1)
# Navigation Bar Completed

frame_login = Frame(root, bg="black")
frame_login.place(x=50, y=150, height=500, width=600)

title = Label(frame_login, text="  Contact Us  ", font=("Impact", 35, "bold", "underline"), bg="black", fg="yellow").place(x=120, y=10)
Label(frame_login, text="Email", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=120)
Entry(frame_login, textvariable=email, font=("Goudy old style", 18), fg="black", bg="white").place(x=250, y=120)
Label(frame_login, text="Username", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=180)
Entry(frame_login, textvariable=Username, font=("Goudy old style", 18), fg="black", bg="white").place(x=250, y=180)
Label(frame_login, text="Phone number", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=240)
Entry(frame_login, textvariable=phone, font=("Goudy old style", 18), fg="black", bg="white").place(x=250, y=240)
Label(frame_login, text="Description", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=300)
Entry(frame_login, textvariable=description, font=("Goudy old style", 18), fg="black", bg="white").place(x=250, y=300)
Button(frame_login, padx=80, text="Submit", bg="light blue", fg="yellow", font=("times new roman", 25, "bold"), command=submit).place(x=140, y=370)

root.mainloop()