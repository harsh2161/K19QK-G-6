from tkinter import *
from PIL import Image, ImageTk
import os
import mysql.connector
import mysql
from tkinter import messagebox

root = Tk()
root.geometry("1400x750+60+10")
bg = ImageTk.PhotoImage(file="loginimage.jpg")
img = Label(root, image=bg)
img.place(x=0, y=0)
root.title(" Car Recommendation System(Login)")

# Declaring Variables
email = StringVar()
password = StringVar()
d_user_id = StringVar()
int_car = StringVar()
# Declared Variables

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


def registrationuser():
    root.destroy()
    os.system('python Registration.py')


def login_user():
    if email.get() == "" or password.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=root)
    if email.get() == "admin2161" and password.get() == "puma100crore":
        root.destroy()
        os.system('python adminpage.py')
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
        mycursor = mydb.cursor()
        mycursor.execute(f"select user_id from User_details where User_email_id = '{email.get()}' and User_password='{password.get()}'")
        res = mycursor.fetchone()
        print(res)
        if res == None:
            messagebox.showerror("Error", "Invalid Username & password", parent=root)
        else:
            messagebox.showinfo("Success", "Welcome", parent=root)
        try:
            d_user_id.set(res[0])
            if d_user_id.get() == "":
                messagebox.showerror("Error", "Please enter the User ID", parent=root)
            else:
                Qwery1 = f"select * from User_details where User_id={d_user_id.get()};"
                mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
                mycursor = mydb.cursor()
                mycursor.execute(Qwery1)
                result = mycursor.fetchall()

                frame_list = Frame(root, bg="white")
                frame_list.place(x=700, y=150, height=370, width=600)
                my_canvas_list = Canvas(frame_list)
                my_canvas_list.pack(side=LEFT, fill=BOTH, expand=1)
                myscrollbar_list = Scrollbar(frame_list, orient=VERTICAL, command=my_canvas_list.yview)
                myscrollbar_list.pack(side=RIGHT, fill=Y)
                my_canvas_list.configure(yscrollcommand=myscrollbar_list.set)
                my_canvas_list.bind('<Configure>',
                                    lambda e: my_canvas_list.configure(scrollregion=my_canvas_list.bbox("all")))
                second_frame_list = Frame(my_canvas_list)
                my_canvas_list.create_window((0, 0), window=second_frame_list, anchor="nw")
                if result == None:
                    messagebox.showerror("Error", "Sorry no such User id found in our server", parent=root)
                else:
                    for i in result:
                        id = i[0]
                        name = i[1]
                        email1 = i[2]
                        phone = i[6]
                        Label(second_frame_list,
                              text=f"User id = '{id}'\nname = '{name}'\nemail = '{email1}'\nphone= '{phone}'",
                              font=("Goudy old style", 18, "bold"), fg="black").grid()
                mydb.close()
        except:
            messagebox.showerror("Error", "Sorry no such User id found in our server", parent=root)
        Label(root, text="  Are You interested in any car  ", font=("Impact", 35, "bold", "underline"), bg="black", fg="yellow").place(x=700, y=500)
        Label(root, text="Car ID", font=("Goudy old style", 25, "bold"), fg="white", bg="black").place(x=700, y=600)
        Entry(root, textvariable=int_car, font=("Goudy old style", 25), fg="black", bg="white").place(x=850, y=600)
        Button(root, padx=80, text="Submit", bg="light blue", fg="yellow", font=("times new roman", 25, "bold"), command=submit).place(x=850, y=670)
        mydb.close()


def submit():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
        mycursor = mydb.cursor()
        mycursor.execute(f"insert into interest_user_car values('{int_car.get()}', {d_user_id.get()});")
        mycursor.execute("commit")
        mydb.close()
        messagebox.showinfo("Info", "Record submit", parent=root)
    except:
        messagebox.showerror("error", "Record already submit", parent=root)


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
frame_login.place(x=50, y=150, height=500, width=500)

title = Label(frame_login, text="  User   Login  ", font=("Impact", 35, "bold", "underline"), bg="black", fg="yellow").place(x=120, y=30)
lbl_username = Label(frame_login, text="Email", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=140)
txt_username = Entry(frame_login, textvariable=email, font=("Goudy old style", 18), fg="black", bg="white").place(x=200, y=140)
lbl_password = Label(frame_login, text="Password", font=("Goudy old style", 18, "bold"), fg="white", bg="black").place(x=50, y=200)
txt_password = Entry(frame_login, textvariable=password, font=("Goudy old style", 18), fg="black", bg="white").place(x=200, y=200)
login_button = Button(frame_login, padx=80, text="Login", bg="light blue", fg="yellow", font=("times new roman", 25, "bold"), command=login_user).place(x=120, y=260)
register_button = Button(frame_login, padx=20, text="New User? Register here", bg="black", fg="blue", font=("times new roman", 25, "bold"), command=registrationuser).place(x=50, y=380)
# Created Frame

root.mainloop()