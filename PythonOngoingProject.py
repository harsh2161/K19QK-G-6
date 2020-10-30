from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("1400x750+60+10")
root.configure(background='black')
root.title(" Car Recommendation System")

# Function Defined here
def ContactUs():
    root.destroy()
    os.system('python ContactUs.py')


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
    pass


# Navigation Bar
Label(root, text="  Car Recommendation System  ", fg='white', bg='black', font=("Comic Sans MS", 25, "bold")).grid(row=0, column=0, columnspan=3)
Home_button = Button(root, text="Home", padx=20, pady=20, font=('', 20, ''), bg='black', fg='blue', command=Home).grid(row=0, column=3, columnspan=1)
About_button = Button(root, text="About", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=About).grid(row=0, column=4, columnspan=1)
Search_vehicle_button = Button(root, text="(Recommendation)\nSearch vehicle", padx=20, pady=4, font=('', 20, ''), bg='black', fg='white', command=SearchVechile).grid(row=0, column=5, columnspan=1)
Login_button = Button(root, text="Login", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Login).grid(row=0, column=6, columnspan=1)
Contact_button = Button(root, text="Contact Us", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=ContactUs).grid(row=0, column=7, columnspan=1)
# Navigation Bar Completed

# Creating Car Recommendation System Logo
image = Image.open("fortuner.jpg")
photo = ImageTk.PhotoImage(image)
img = Label(image=photo)
img.grid(row=1, columnspan=8)
# Car Recommendation System Logo Completed

# Creating Name logo
Label(root, text="  Welcome To Our Car Recommendation System  ", fg='yellow', bg='black', font=("Comic Sans MS", 25, "bold", 'underline')).grid(row=2, column=0, columnspan=9)
# Created Name Logo

# Creating base 3 Photos
# --------------------------------------------
# Creating First Image
image_jaguar = Image.open("jg.jpg")
photo_jaguar = ImageTk.PhotoImage(image_jaguar)
img_jaguar = Label(image=photo_jaguar)
img_jaguar.grid(row=3, column=0, columnspan=2)
# Created First Image

# Creating Second Image
image_jaguar1 = Image.open("ad.jpg")
photo_jaguar1 = ImageTk.PhotoImage(image_jaguar1)
img_jaguar1 = Label(image=photo_jaguar1)
img_jaguar1.grid(row=3, column=3, columnspan=2)
# Created Second Image

# Creating Third Image
image_jaguar2 = Image.open("md.jpg")
photo_jaguar2 = ImageTk.PhotoImage(image_jaguar2)
img_jaguar2 = Label(image=photo_jaguar2)
img_jaguar2.grid(row=3, column=5, columnspan=4)
# Created Third Image
# --------------------------------------
# Created base 3 Photos

# Creating 3 heading lines
Label(root, text="Search Your Car", fg='yellow', bg='black', font=("Comic Sans MS", 15, "bold")).grid(row=4, column=0, columnspan=2)
Label(root, text="Search Car By Category", fg='yellow', bg='black', font=("Comic Sans MS", 15, "bold")).grid(row=4, column=3, columnspan=2)
Label(root, text="Get all the details of your fav car", fg='yellow', bg='black', font=("Comic Sans MS", 15, "bold")).grid(row=4, column=5, columnspan=3)
# Created 3 lines

# Adding Description to Line
Label(root, text="CRS is a great place to start planning your\nnew car purchase Tell us a few things about\nyou and your preferences, and we'llsuggest the\ncars that suit youthe best.Our Advance Search\nfilters will get you the best car.", fg='white', bg='black', font=("Comic Sans MS", 10, "bold")).grid(row=5, column=0, columnspan=2)
Label(root, text="\t\t  With our advance filters you can easily \n\t\t  search brand new cars. which suits your\n\t\t   budget.", fg='white', bg='black', font=("Comic Sans MS", 10, "bold")).grid(row=5, column=2, columnspan=3)
Label(root, text="Not able to find all the details at one    \nplace. Dont worry we have a solution for    \nthat try our (Recommendation)Search vehicle to get all  \nthe details of your favorite car in just one click.", fg='white', bg='black', font=("Comic Sans MS", 10, "bold")).grid(row=5, column=5, columnspan=4)
# Added Description to line

root.mainloop()
