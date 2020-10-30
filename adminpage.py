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

# Variables
d_car_id = StringVar()
e_car_name = StringVar()
e_car_Id = StringVar()
e_car_model = StringVar()
car_fuel_type = StringVar()
car_fuel_type.set("petrol")
e_car_mileage = IntVar()
e_car_mileage.set("")
e_car_price = IntVar()
e_car_price.set("")
e_car_company = StringVar()
e_car_engine = StringVar()
e_car_transmission = StringVar()
e_car_transmission.set("manual")
e_car_seating = IntVar()
e_car_seating.set("")
e_car_colors = StringVar()
# Variables completed


def delete_car():
    try:
        if d_car_id.get() == "":
            messagebox.showerror("Error", "Please enter the Car ID", parent=root)
        else:
            Qwery = f"delete from Cars_details where Car_id='{d_car_id.get()}';"
            mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
            mycursor = mydb.cursor()
            mycursor.execute(Qwery)
            mycursor.execute("commit")
            mydb.close()
            messagebox.showerror("Info", "Car Data removed", parent=root)
    except:
        messagebox.showerror("Error", "Sorry no such car id found in our server", parent=root)



def add_car():
    try:
        if e_car_name.get() == "" or e_car_Id.get() == "" or e_car_model.get() == "" or e_car_mileage.get() == "" or e_car_price.get() == "" or e_car_company.get() == "" or e_car_engine.get() == "" or e_car_transmission.get() == "" or e_car_seating.get() == "" or e_car_colors.get() == "":
            messagebox.showerror("Error", "Fill all the boxes...", parent=root)
        else:
            Qwery_statement = f"insert into Cars_details(Car_id, Car_name, Car_model,Car_fuel_type, Car_mileage, Car_price, Car_company,Car_Engine, Car_Transmission, Car_seating_capacity,Car_color) values ('{e_car_Id.get()}', '{e_car_name.get()}', '{e_car_model.get()}', '{car_fuel_type.get()}',{e_car_mileage.get()},{e_car_price.get()}, '{e_car_company.get()}', '{e_car_engine.get()}', '{e_car_transmission.get()}',{e_car_seating.get()} ,'{e_car_colors.get()}');"
            mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
            mycursor = mydb.cursor()
            mycursor.execute(Qwery_statement)
            mycursor.execute("commit")
            messagebox.showinfo("Info", "Car Detail added.", parent=root)
            mydb.close()
    except:
        messagebox.showerror("Error", "Check car ID or Entered details are not in proper format.", parent=root)


def User_portion():
    root.destroy()
    os.system('python admin_user_portion.py')


def Car_portion():
    pass


def logout():
    root.destroy()
    os.system('python Login.py')


Label(root, text="  Welcome admin  ", font=("Goudy old style", 35, "bold", "underline"), fg="white", bg="black").place(x=10, y=5)
Button(root, padx=20, text="Logout", bg="black", fg="red", font=("times new roman", 25, "bold"), command=logout).place(x=1226, y=5)
Button(root, padx=50, text="Car Portion", bg="black", fg="yellow", font=("times new roman", 25, "bold"), command=Car_portion).place(x=510, y=5)
Button(root, padx=50, text="User Portion", bg="black", fg="blue", font=("times new roman", 25, "bold"), command=User_portion).place(x=810, y=5)

# adding a car here
Label(root, text="Add a new car here", font=("Goudy old style", 20, "bold"), fg="white", bg="black").place(x=10, y=100)
adding_new_car = Frame(root, bg="white")
adding_new_car.place(x=10, y=150, height=430, width=700)
new_car_canvas = Canvas(adding_new_car)
new_car_canvas.pack(side=LEFT, fill=BOTH, expand=1)
myscrollbar = Scrollbar(adding_new_car, orient=VERTICAL, command=new_car_canvas.yview)
myscrollbar.pack(side=RIGHT, fill=Y)
new_car_canvas.configure(yscrollcommand=myscrollbar.set)
new_car_canvas.bind('<Configure>', lambda e: new_car_canvas.configure(scrollregion=new_car_canvas.bbox("all")))
new_frame = Frame(new_car_canvas)
new_car_canvas.create_window((0, 0), window=new_frame, anchor="nw")

Label(new_frame, padx=50, text="Car Id", font=("Goudy old style", 18, "bold"), fg="black").grid(row=0, column=0)
Entry(new_frame, textvariable=e_car_Id, font=("Goudy old style", 18), fg="black", bg="white").grid(row=0, column=1)
Label(new_frame, padx=50, text="Car name", font=("Goudy old style", 18, "bold"), fg="black").grid(row=1, column=0)
Entry(new_frame, textvariable=e_car_name, font=("Goudy old style", 18), fg="black", bg="white").grid(row=1, column=1)
Label(new_frame, padx=50, text="Car model", font=("Goudy old style", 18, "bold"), fg="black").grid(row=2, column=0)
Entry(new_frame, textvariable=e_car_model, font=("Goudy old style", 18), fg="black", bg="white").grid(row=2, column=1)
Label(new_frame, padx=50, text="Car fuel type", font=("Goudy old style", 18, "bold"), fg="black").grid(row=3, column=0)
OptionMenu(new_frame, car_fuel_type, "diesel", "petrol", "diesel/petrol", "electricity", "cng").grid(row=3, column=1)
Label(new_frame, padx=50, text="Car mileage(INT)", font=("Goudy old style", 18, "bold"), fg="black").grid(row=4, column=0)
Entry(new_frame, textvariable=e_car_mileage, font=("Goudy old style", 18), fg="black", bg="white").grid(row=4, column=1)
Label(new_frame, padx=50, text="Car Price(INT)", font=("Goudy old style", 18, "bold"), fg="black").grid(row=5, column=0)
Entry(new_frame, textvariable=e_car_price, font=("Goudy old style", 18), fg="black", bg="white").grid(row=5, column=1)
Label(new_frame, padx=50, text="Car company", font=("Goudy old style", 18, "bold"), fg="black").grid(row=6, column=0)
Entry(new_frame, textvariable=e_car_company, font=("Goudy old style", 18), fg="black", bg="white").grid(row=6, column=1)
Label(new_frame, padx=50, text="Car engine", font=("Goudy old style", 18, "bold"), fg="black").grid(row=7, column=0)
Entry(new_frame, textvariable=e_car_engine, font=("Goudy old style", 18), fg="black", bg="white").grid(row=7, column=1)
Label(new_frame, padx=50, text="Car transmission", font=("Goudy old style", 18, "bold"), fg="black").grid(row=8, column=0)
OptionMenu(new_frame, e_car_transmission, "automatic", "manual").grid(row=8, column=1)
Label(new_frame, padx=50, text="Car seating capacity(INT)", font=("Goudy old style", 18, "bold"), fg="black").grid(row=9, column=0)
Entry(new_frame, textvariable=e_car_seating, font=("Goudy old style", 18), fg="black", bg="white").grid(row=9, column=1)
Label(new_frame, padx=50, text="Car colors", font=("Goudy old style", 18, "bold"), fg="black").grid(row=10, column=0)
Entry(new_frame, textvariable=e_car_colors, font=("Goudy old style", 18), fg="black", bg="white").grid(row=10, column=1)
Button(new_frame, padx=50, text="Add Car", fg="blue", font=("times new roman", 25, "bold"), command=add_car).grid(row=11,column=1)
# adding a car completed

# Deleting a Car
Label(root, text="Delete the car here", font=("Goudy old style", 25, "bold"), fg="white", bg="black").place(x=10, y=600)
Label(root, text="Enter car ID here", font=("Goudy old style", 20, "bold"), fg="white", bg="black").place(x=10, y=670)
Entry(root, textvariable=d_car_id, font=("Goudy old style", 18), fg="black", bg="white").place(x=260, y=675)
Button(root, text="Delete the car", bg="black", fg="red", font=("times new roman", 16, "bold"), command=delete_car).place(x=550, y=670)
# Deleted a Car

# Query/contact us Portion
Label(root, text="Users Query/contact us", font=("Goudy old style", 20, "bold"), fg="white", bg="black").place(x=750, y=100)
frame_list = Frame(root, bg="white")
frame_list.place(x=750, y=150, height=550, width=600)
my_canvas_list = Canvas(frame_list)
my_canvas_list.pack(side=LEFT, fill=BOTH, expand=1)
myscrollbar_list = Scrollbar(frame_list, orient=VERTICAL, command=my_canvas_list.yview)
myscrollbar_list.pack(side=RIGHT, fill=Y)
my_canvas_list.configure(yscrollcommand=myscrollbar_list.set)
my_canvas_list.bind('<Configure>',
                    lambda e: my_canvas_list.configure(scrollregion=my_canvas_list.bbox("all")))
second_frame_list = Frame(my_canvas_list)
my_canvas_list.create_window((0, 0), window=second_frame_list, anchor="nw")

mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
mycursor = mydb.cursor()
mycursor.execute(f"select * from contact_us")
res = mycursor.fetchall()
for i in res:
    email = i[0]
    name = i[1]
    phone = i[2]
    des = i[3]
    Label(second_frame_list, text=f"Name = {name}\nEmail = {email}\nPhone = {phone}\nQuery = {des[0:30]}\n{des[31:60]}\n", font=("Goudy old style", 15, "bold"), fg="black").grid()
mydb.close()
# Query/contact us completed
root.mainloop()