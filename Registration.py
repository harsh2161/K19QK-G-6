from tkinter import *
import mysql
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("1400x750+60+10")
# background image started
bg = ImageTk.PhotoImage(file="loginimage.jpg")
img = Label(root, image=bg)
img.place(x=0, y=0)
# background image completed
root.title(" Car Recommendation System(Login)")


# Function Defined here
def ContactUs():
    root.destroy()
    os.system('python ContactUs.py')


def Login():
    pass


def SearchVechile():
    root.destroy()
    os.system('python SearchVechile.py')


def About():
    root.destroy()
    os.system('python About.py')


def Home():
    root.destroy()
    os.system('python PythonOngoingProject.py')


def loginuser():
    root.destroy()
    os.system('python Login.py')


def register_user():
    if email.get() == "" or password.get() == "" or name.get() == "" or phone_no.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=root)
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
        mycursor = mydb.cursor()
        mycursor.execute("select id from ID")
        result = mycursor.fetchone()
        for i in result:
            curr_id = i
        curr_id1 = curr_id + 1
        strcur = str(curr_id)
        mycursor.execute(f"UPDATE ID set id={curr_id1} where id={curr_id}")
        mycursor.execute("commit")
        mycursor.execute("insert into User_details(User_id, User_name,User_email_id,User_password,User_phone_number) Values("+strcur+",'"+name.get()+"','"+email.get()+"','"+password.get()+"','"+phone_no.get()+"')")
        mycursor.execute("commit")
        messagebox.showinfo("Success", "Successfully Registered")
        mydb.close()


# Giving Variables name
email = StringVar()
password = StringVar()
phone_no = StringVar()
name = StringVar()
# Given the name


# Navigation Bar
Label(root, text="  Car Recommendation System  ", pady=23, fg='white', bg='black', font=("Comic Sans MS", 25, "bold")).grid(row=0, column=0, columnspan=3)
Home_button = Button(root, text="Home", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Home).grid(row=0, column=3, columnspan=1)
About_button = Button(root, text="About", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=About).grid(row=0, column=4, columnspan=1)
Search_vehicle_button = Button(root, text="(Recommendation)\nSearch vehicle", padx=20, pady=4, font=('', 20, ''), bg='black', fg='white', command=SearchVechile).grid(row=0, column=5, columnspan=1)
Login_button = Button(root, text="Login", padx=20, pady=20, font=('', 20, ''), bg='black', fg='blue', command=Login).grid(row=0, column=6, columnspan=1)
Contact_button = Button(root, text="Contact Us", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=ContactUs).grid(row=0, column=7, columnspan=1)
# Navigation Bar Completed

# Creating Frame
frame_login = Frame(root, bg="black")
frame_login.place(x=50, y=120, height=550, width=500)

title = Label(frame_login, text="  User   Registration  ", font=("Impact", 35, "bold", "underline"), bg="black", fg="yellow").place(x=50, y=30)
lbl_email = Label(frame_login, text="Email", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=140)
txt_email = Entry(frame_login, textvariable=email, font=("Goudy old style", 18), fg="black", bg="white").place(x=200, y=140)
lbl_password = Label(frame_login, text="Password", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=200)
txt_password = Entry(frame_login, textvariable=password, font=("Goudy old style", 18), fg="black", bg="white").place(x=200, y=200)
lbl_name = Label(frame_login, text="Name", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=260)
txt_name = Entry(frame_login, textvariable=name, font=("Goudy old style", 18), fg="black", bg="white").place(x=200, y=260)
lbl_phone_number = Label(frame_login, text="Phone Number", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=10, y=320)
txt_phone_number = Entry(frame_login, textvariable=phone_no, font=("Goudy old style", 18), fg="black", bg="white").place(x=200, y=320)
register_button = Button(frame_login, padx=80, text="Register", bg="light blue", fg="yellow", font=("times new roman", 25, "bold"), command=register_user).place(x=100, y=380)
login_button = Button(frame_login, padx=20, text="Already have account\nLogin here", bg="black", fg="white", bd=0, font=("times new roman", 15, "bold"), command=loginuser).place(x=130, y=460)
# Created Frame

root.mainloop()