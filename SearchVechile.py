from tkinter import *
from PIL import Image, ImageTk
import os
import mysql.connector
import mysql
from tkinter import messagebox

root = Tk()
root.geometry("1400x750+60+10")
root.configure(background='black')
root.title(" Car Recommendation System(Search Vechile)")

# variables
min = IntVar
max = IntVar
Qwery_statement = StringVar()
car_name = StringVar()
clicked1 = StringVar()
clicked1.set("or")
clicked_fuel_type = StringVar()
clicked_fuel_type.set("")
clicked2 = StringVar()
clicked2.set("or")
clicked_mileage = StringVar()
clicked_mileage.set("")
clicked3 = StringVar()
clicked3.set("or")
clicked_min_price = StringVar()
clicked_min_price.set("2 lakh")
clicked_max_price = StringVar()
clicked_max_price.set("2 crore")
clicked4 = StringVar()
clicked4.set("or")
clicked_min_seat = StringVar()
clicked_min_seat.set("4")
clicked_max_seat = StringVar()
clicked_max_seat.set("7")
enter_car_id = StringVar()
# variables completed

def ContactUs():
    root.destroy()
    os.system('python ContactUs.py')


def Login():
    root.destroy()
    os.system('python Login.py')


def SearchVechile():
    pass


def About():
    root.destroy()
    os.system('python About.py')


def Home():
    root.destroy()
    os.system('python PythonOngoingProject.py')


def carfilter():
    if car_name.get() == "":
        messagebox.showerror("Error", "Car name is required", parent=root)
    else:
        Qwery_statement = f"select Car_id,Car_name,Car_company from cars_details where Car_name='{car_name.get()}'"
        mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
        mycursor = mydb.cursor()
        mycursor.execute(Qwery_statement)
        result = mycursor.fetchall()
        frame_list = Frame(root, bg="white")
        frame_list.place(x=15, y=330, height=330, width=650)
        my_canvas_list = Canvas(frame_list)
        my_canvas_list.pack(side=LEFT, fill=BOTH, expand=1)
        myscrollbar_list = Scrollbar(frame_list, orient=VERTICAL, command=my_canvas_list.yview)
        myscrollbar_list.pack(side=RIGHT, fill=Y)
        my_canvas_list.configure(yscrollcommand=myscrollbar_list.set)
        my_canvas_list.bind('<Configure>', lambda e: my_canvas_list.configure(scrollregion=my_canvas_list.bbox("all")))
        second_frame_list = Frame(my_canvas_list)
        my_canvas_list.create_window((0, 0), window=second_frame_list, anchor="nw")
        for i in result:
            id = i[0]
            name = i[1]
            company = i[2]
            detail = Label(second_frame_list, padx=120, text=f"Car id = {id}\nCar name = {name}\nCar Company = {company}",
                           font=("Goudy old style", 18, "bold"), fg="black")
            detail.grid()
            detailblank = Label(second_frame_list, text="", font=("Goudy old style", 18, "bold"), fg="black")
            detailblank.grid()
        mycursor.execute("commit")
        mydb.close()


def carID():
    if enter_car_id.get() == "":
        messagebox.showerror("Error", "Car Id is required\nDont know car id click apply filter and get your car ID.", parent=root)
    else:
        qw = StringVar()
        mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
        mycursor = mydb.cursor()
        qw = f"select * from Cars_details where Car_id='{enter_car_id.get()}'"
        mycursor.execute(qw)
        result = mycursor.fetchall()
        frame_login = Frame(root, bg="white")
        frame_login.place(x=680, y=280, height=450, width=700)

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


def applyfilters():
    Qwery_statement = "select Car_id,Car_name,Car_company from cars_details where "
    if car_name.get() == "":
        Qwery_statement = Qwery_statement + f"Car_name ='' or "
    if car_name.get() != "":
        Qwery_statement = Qwery_statement + f"Car_name ='{car_name.get()}' {clicked1.get()} "
    if clicked_fuel_type.get() == "":
        Qwery_statement = Qwery_statement + f"Car_fuel_type='{clicked_fuel_type.get()}' {clicked2.get()} "
    if clicked_fuel_type.get() != "":
        if clicked_fuel_type.get() == "diesel":
            Qwery_statement = Qwery_statement + f"Car_fuel_type='{clicked_fuel_type.get()}' or Car_fuel_type='diesel/petrol' {clicked2.get()} "
        if clicked_fuel_type.get() == "petrol":
            Qwery_statement = Qwery_statement + f"Car_fuel_type='{clicked_fuel_type.get()}' or Car_fuel_type='diesel/petrol' {clicked2.get()} "
        if clicked_fuel_type.get() == "diesel/petrol":
            Qwery_statement = Qwery_statement + f"Car_fuel_type='{clicked_fuel_type.get()}' or Car_fuel_type='petrol' or Car_fuel_type='diesel' {clicked2.get()} "
        if clicked_fuel_type.get() == "electricity" or clicked_fuel_type.get() == "cng":
            Qwery_statement = Qwery_statement + f"Car_fuel_type='{clicked_fuel_type.get()}' {clicked2.get()} "
    if clicked_mileage.get() == "":
        Qwery_statement = Qwery_statement + f"Car_mileage >5 {clicked3.get()} "
    if clicked_mileage.get() != "":
        if clicked_mileage.get() == "More than 5":
            Qwery_statement = Qwery_statement +f"Car_mileage >5 {clicked3.get()} "
        if clicked_mileage.get() == "More than 10":
            Qwery_statement = Qwery_statement +f"Car_mileage >10 {clicked3.get()} "
        if clicked_mileage.get() == "More than 15":
            Qwery_statement = Qwery_statement +f"Car_mileage >15 {clicked3.get()} "
        if clicked_mileage.get() == "More than 25":
            Qwery_statement = Qwery_statement +f"Car_mileage >25 {clicked3.get()} "
    if clicked_min_price.get() == "2 lakh":
        Qwery_statement = Qwery_statement + f"Car_price between 200000 and "
    if clicked_min_price.get() != "2 lakh":
        if clicked_min_price.get() == "5 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 500000 and "
        if clicked_min_price.get() == "10 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 1000000 and "
        if clicked_min_price.get() == "15 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 1500000 and "
        if clicked_min_price.get() == "20 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 2000000 and "
        if clicked_min_price.get() == "30 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 3000000 and "
        if clicked_min_price.get() == "40 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 4000000 and "
        if clicked_min_price.get() == "50 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 5000000 and "
        if clicked_min_price.get() == "60 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 6000000 and "
        if clicked_min_price.get() == "70 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 7000000 and "
        if clicked_min_price.get() == "80 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 8000000 and "
        if clicked_min_price.get() == "90 lakh":
            Qwery_statement = Qwery_statement + f"Car_price between 9000000 and "
        if clicked_min_price.get() == "1 crore":
            Qwery_statement = Qwery_statement + f"Car_price between 10000000 and "
        if clicked_min_price.get() == "1.5 crore":
            Qwery_statement = Qwery_statement + f"Car_price between 15000000 and "
    if clicked_max_price.get() != "2 crore":
        if int(clicked_min_price.get()[0]) > int(clicked_max_price.get()[0])+1:
            messagebox.showerror("Error", "maximum price should be greator than minimum price", parent=root)
            clicked_max_price.set("2 crore")
        else:
            if clicked_min_price.get() == "5 lakh":
                Qwery_statement = Qwery_statement + f"500000 {clicked4.get()} "
            if clicked_min_price.get() == "10 lakh":
                Qwery_statement = Qwery_statement + f"1000000 {clicked4.get()} "
            if clicked_min_price.get() == "15 lakh":
                Qwery_statement = Qwery_statement + f"1500000 {clicked4.get()} "
            if clicked_min_price.get() == "20 lakh":
                Qwery_statement = Qwery_statement + f"2000000 {clicked4.get()} "
            if clicked_min_price.get() == "30 lakh":
                Qwery_statement = Qwery_statement + f"3000000 {clicked4.get()} "
            if clicked_min_price.get() == "40 lakh":
                Qwery_statement = Qwery_statement + f"4000000 {clicked4.get()} "
            if clicked_min_price.get() == "50 lakh":
                Qwery_statement = Qwery_statement + f"5000000 {clicked4.get()} "
            if clicked_min_price.get() == "60 lakh":
                Qwery_statement = Qwery_statement + f"6000000 {clicked4.get()} "
            if clicked_min_price.get() == "70 lakh":
                Qwery_statement = Qwery_statement + f"7000000 and {clicked4.get()} "
            if clicked_min_price.get() == "80 lakh":
                Qwery_statement = Qwery_statement + f"8000000 and {clicked4.get()} "
            if clicked_min_price.get() == "90 lakh":
                Qwery_statement = Qwery_statement + f"9000000 and {clicked4.get()} "
            if clicked_min_price.get() == "1 crore":
                Qwery_statement = Qwery_statement + f"10000000 {clicked4.get()} "
            if clicked_min_price.get() == "1.5 crore":
                Qwery_statement = Qwery_statement + f"15000000 {clicked4.get()} "
    if clicked_max_price.get() == "2 crore":
        Qwery_statement = Qwery_statement + f"20000000 {clicked4.get()} "
    if clicked_min_seat.get() == "4":
        Qwery_statement = Qwery_statement + f"Car_seating_capacity between 4 and "
    if clicked_min_seat.get() == "6":
        Qwery_statement = Qwery_statement + f"Car_seating_capacity between 4 and "
    if clicked_max_seat.get() == "6":
        Qwery_statement = Qwery_statement + f"{clicked_max_seat.get()}"
    if clicked_max_seat.get() == "7":
        Qwery_statement = Qwery_statement + f"{clicked_max_seat.get()}"
    print(Qwery_statement)

    mydb = mysql.connector.connect(host="localhost", user="root", password="harsh2161", database="python_pj1")
    mycursor = mydb.cursor()
    mycursor.execute(Qwery_statement)
    result = mycursor.fetchall()
    frame_list = Frame(root, bg="white")
    frame_list.place(x=15, y=330, height=330, width=650)
    my_canvas_list = Canvas(frame_list)
    my_canvas_list.pack(side=LEFT, fill=BOTH, expand=1)
    myscrollbar_list = Scrollbar(frame_list, orient=VERTICAL, command=my_canvas_list.yview)
    myscrollbar_list.pack(side=RIGHT, fill=Y)
    my_canvas_list.configure(yscrollcommand=myscrollbar_list.set)
    my_canvas_list.bind('<Configure>', lambda e: my_canvas_list.configure(scrollregion=my_canvas_list.bbox("all")))
    second_frame_list = Frame(my_canvas_list)
    my_canvas_list.create_window((0, 0), window=second_frame_list, anchor="nw")
    for i in result:
        id = i[0]
        name = i[1]
        company = i[2]
        detail = Label(second_frame_list, padx=120, text=f"Car id = {id}\nCar name = {name}\nCar Company = {company}", font=("Goudy old style", 18, "bold"), fg="black")
        detail.grid()
        detailblank = Label(second_frame_list, text="", font=("Goudy old style", 18, "bold"), fg="black")
        detailblank.grid()
    mycursor.execute("commit")
    mydb.close()


# Navigation Bar
Label(root, text="  Car Recommendation System  ", fg='white', bg='black', font=("Comic Sans MS", 25, "bold")).grid(row=0, column=0, columnspan=3)
Home_button = Button(root, text="Home", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Home).grid(row=0, column=3, columnspan=1)
About_button = Button(root, text="About", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=About).grid(row=0, column=4, columnspan=1)
Search_vehicle_button = Button(root, text="(Recommendation)\nSearch vehicle", padx=20, pady=4, font=('', 20, ''), bg='black', fg='blue', command=SearchVechile).grid(row=0, column=5, columnspan=1)
Login_button = Button(root, text="Login", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Login).grid(row=0, column=6, columnspan=1)
Contact_button = Button(root, text="Contact Us", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=ContactUs).grid(row=0, column=7, columnspan=1)
# Navigation Bar Completed


# started upper frame
frame_filter = Frame(root, bg="black")
frame_filter.place(x=10, y=100, height=130, width=1370)
Label(frame_filter, text="Car name", font=("Goudy old style", 18, "bold"), fg="Yellow", bg="black").place(x=15, y=10)
txt_car_name = Entry(frame_filter, textvariable=car_name, font=("Goudy old style", 18), fg="black", bg="white").place(x=150, y=13)
drop1 = OptionMenu(frame_filter, clicked1, "or", "and").place(x=430, y=13)
Label(frame_filter, text="Select Car fuel type", font=("Goudy old style", 18, "bold"), fg="Yellow", bg="black").place(x=520, y=10)
drop_car_fuel_type = OptionMenu(frame_filter, clicked_fuel_type, "", "diesel", "petrol", "diesel/petrol", "electricity","cng").place(x=760, y=13)
drop2 = OptionMenu(frame_filter, clicked2, "or", "and").place(x=890, y=13)
Label(frame_filter, text="Select Mileage", font=("Goudy old style", 18, "bold"), fg="Yellow", bg="black").place(x=980, y=10)
drop_car_mileage= OptionMenu(frame_filter, clicked_mileage, "", "More than 5", "More than 10", "More than 15", "More than 25").place(x=1180, y=13)
drop3 = OptionMenu(frame_filter, clicked3, "or", "and").place(x=1300, y=13)
Label(frame_filter, text="Select minimum price", font=("Goudy old style", 18, "bold"), fg="Yellow", bg="black").place(x=15, y=60)
drop_car_min_price = OptionMenu(frame_filter, clicked_min_price, "1)2 lakh", "2)5 lakh", "3)10 lakh", "4)15 lakh", "5)20 lakh", "6)30 lakh", "7)40 lakh", "8)50 lakh", "9)60 lakh", "10)70 lakh", "11)80 lakh", "12)90 lakh", "13)1 crore", "14)1.5 crore").place(x=290, y=63)
Label(frame_filter, text="Select maximum price", font=("Goudy old style", 18, "bold"), fg="Yellow", bg="black").place(x=400, y=60)
drop_car_max_price = OptionMenu(frame_filter, clicked_max_price, "1)5 lakh", "2)10 lakh", "3)15 lakh", "4)20 lakh", "5)30 lakh", "6)40 lakh", "7)50 lakh", "8)60 lakh", "9)70 lakh", "10)80 lakh", "11)90 lakh", "12)1 crore", "13)1.5 crore", "14)2 crore").place(x=680, y=63)
drop4 = OptionMenu(frame_filter, clicked4, "or", "and").place(x=780, y=63)
Label(frame_filter, text="Select minimum/maximum seat", font=("Goudy old style", 18, "bold"), fg="Yellow", bg="black").place(x=850, y=60)
drop_car_min_seat = OptionMenu(frame_filter, clicked_min_seat, "4", "6").place(x=1230, y=63)
drop_car_max_seat = OptionMenu(frame_filter, clicked_max_seat, "6", "7").place(x=1300, y=63)
# Completed upper frame

Label(root, text="  List of cars after applying filters  ", fg='blue', bg='black', font=("Comic Sans MS", 25, "bold", "underline")).place(x=15, y=270)
Label(root, text="Get your car details by entering Car ID", fg='blue', bg='black', font=("Comic Sans MS", 25, "bold", "underline")).place(x=700, y=210)

Button(root, padx=10, text="Apply All Filters", bg="light blue", fg="yellow", font=("times new roman", 25, "bold"), command=applyfilters).place(x=15, y=210)
Button(root, padx=10, text="Search By Car name", bg="light blue", fg="yellow", font=("times new roman", 25, "bold"), command=carfilter).place(x=330, y=210)


Label(root, text="Car ID", font=("Goudy old style", 18, "bold"), fg="Yellow", bg="black").place(x=15, y=685)
enter_car_id1 = Entry(root, textvariable=enter_car_id, font=("Goudy old style", 18), fg="black", bg="white").place(x=110, y=685)
Button(root, text="Search", bg="light blue", fg="yellow", font=("times new roman", 25, "bold"), command=carID).place(x=390, y=670)
Label(root, text="Enter car id \nand get details \nof cars", font=("Goudy old style", 10, "bold"), fg="red", bg="black").place(x=540, y=680)

root.mainloop()