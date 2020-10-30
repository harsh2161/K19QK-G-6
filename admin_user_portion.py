from tkinter import *
from PIL import Image, ImageTk
import os
import mysql.connector
import mysql
from tkinter import messagebox

root = Tk()
root.geometry("1400x750+60+10")
root.configure(background='black')
root.title(" Admin Page")

# variables
d_car_id = StringVar()
d_user_id = StringVar()
# variables completed


def car_detail():
    if d_car_id.get() == "":
        messagebox.showerror("Error", "Car Id is required\nDont know car id click apply filter and get your car ID.", parent=root)
    else:
        qw = StringVar()
        mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
        mycursor = mydb.cursor()
        qw = f"select * from Cars_details where Car_id='{d_car_id.get()}'"
        mycursor.execute(qw)
        result = mycursor.fetchall()
        frame_login = Frame(root, bg="white")
        frame_login.place(x=760, y=150, height=270, width=600)

        my_canvas = Canvas(frame_login)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        myscrollbar = Scrollbar(frame_login, orient=VERTICAL, command=my_canvas.yview)
        myscrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=myscrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)

        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        for i in result:
            id = i[0]
            name = i[1]
            model = i[2]
            fuel = i[3]
            mileage = i[4]
            price = i[5]
            company = i[6]
            engine = i[7]
            transmission = i[8]
            seating = i[9]
            color = i[10]
            Label(second_frame, text=f"Car id = {id}\n\nCar name = {name}\n\nCar Company = {company}\n\nCar model = {model}\n\nCar fuel type = {fuel}\n\nCar mileage = {mileage}\n\nCar price = {price}\n\nCar engine = {engine}\n\n Car transmission = {transmission}\n\nCar seating = {seating}\n\nCar color = {color[0:29]} and many\nmore colors avaliable", font=("Goudy old style", 18, "bold"), fg="black").grid()
        mycursor.execute("commit")
        mydb.close()


def user_detail():
    try:
        if d_user_id.get() == "":
            messagebox.showerror("Error", "Please enter the User ID", parent=root)
        else:
            Qwery1 = f"select * from User_details where User_id={d_user_id.get()};"
            mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
            mycursor = mydb.cursor()
            mycursor.execute(Qwery1)
            result = mycursor.fetchall()

            frame_list = Frame(root, bg="white")
            frame_list.place(x=760, y=470, height=270, width=600)
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
                    email = i[2]
                    phone = i[6]
                    Label(second_frame_list, text=f"User id = '{id}'\nname = '{name}'\nemail = '{email}'\nphone= '{phone}'", font=("Goudy old style", 18, "bold"), fg="black").grid()
            mydb.close()
    except:
        messagebox.showerror("Error", "Sorry no such User id found in our server", parent=root)


def delete_user():
    try:
        if d_user_id.get() == "":
            messagebox.showerror("Error", "Please enter the User ID", parent=root)
        else:
            Qwery = f"delete from User_details where User_id='{d_user_id.get()}';"
            mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
            mycursor = mydb.cursor()
            mycursor.execute(Qwery)
            mycursor.execute("commit")
            mydb.close()
            messagebox.showerror("Info", "User Data removed", parent=root)
    except:
        messagebox.showerror("Error", "Sorry no such User id found in our server", parent=root)


def User_portion():
    pass


def Car_portion():
    root.destroy()
    os.system('python adminpage.py')


def logout():
    root.destroy()
    os.system('python Login.py')


Label(root, text="  Welcome admin  ", font=("Goudy old style", 35, "bold", "underline"), fg="white", bg="black").place(x=10, y=5)
Button(root, padx=20, text="Logout", bg="black", fg="red", font=("times new roman", 25, "bold"), command=logout).place(x=1226, y=5)
Button(root, padx=50, text="Car Portion", bg="black", fg="blue", font=("times new roman", 25, "bold"), command=Car_portion).place(x=510, y=5)
Button(root, padx=50, text="User Portion", bg="black", fg="yellow", font=("times new roman", 25, "bold"), command=User_portion).place(x=810, y=5)

mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
mycursor = mydb.cursor()
mycursor.execute(f"select * from interest_user_car;")
result = mycursor.fetchall()
Label(root, text="Interested Car Users in Car ID", font=("Goudy old style", 20, "bold"), fg="white", bg="black").place(x=10, y=100)
interested_car = Frame(root, bg="white")
interested_car.place(x=10, y=150, height=330, width=700)
interested_car_canvas = Canvas(interested_car)
interested_car_canvas.pack(side=LEFT, fill=BOTH, expand=1)
myscrollbar = Scrollbar(interested_car, orient=VERTICAL, command=interested_car_canvas.yview)
myscrollbar.pack(side=RIGHT, fill=Y)
interested_car_canvas.configure(yscrollcommand=myscrollbar.set)
interested_car_canvas.bind('<Configure>', lambda e: interested_car_canvas.configure(scrollregion=interested_car_canvas.bbox("all")))
new_frame = Frame(interested_car_canvas)
interested_car_canvas.create_window((0, 0), window=new_frame, anchor="nw")
j = 1
for i in result:
    car_id = i[0]
    user_id = i[1]
    Label(new_frame, text=f"{j})This User id = '{user_id}' is looking for the Car id = '{car_id}'", font=("Goudy old style", 18, "bold"), fg="black").grid()
    j = j+1

Label(root, text="Interest of a particular car or user", font=("Goudy old style", 20, "bold"), fg="white", bg="black").place(x=10, y=490)
Label(root, text="User ID", font=("Goudy old style", 15, "bold"), fg="white", bg="black").place(x=10, y=552)
Entry(root, textvariable=d_user_id, font=("Goudy old style", 18), fg="black", bg="white").place(x=130, y=552)
Button(root, text="Delete the particular User", bg="black", fg="red", font=("times new roman", 15, "bold"), command=delete_user).place(x=450, y=548)
Button(root, text="Get User Detail", bg="black", fg="blue", font=("times new roman", 15, "bold"), command=user_detail).place(x=450, y=610)
Label(root, text="User detail", font=("Goudy old style", 20, "bold"), fg="white", bg="black").place(x=760, y=420)
Label(root, text="Car detail", font=("Goudy old style", 20, "bold"), fg="white", bg="black").place(x=760, y=100)
Label(root, text="Car ID", font=("Goudy old style", 15, "bold"), fg="white", bg="black").place(x=10, y=682)
Entry(root, textvariable=d_car_id, font=("Goudy old style", 18), fg="black", bg="white").place(x=130, y=682)
Button(root, text="Get Car detail", bg="black", fg="red", font=("times new roman", 15, "bold"), command=car_detail).place(x=450, y=680)

root.mainloop()