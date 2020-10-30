from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("1400x750+60+10")
root.configure(background='black')
root.title(" Car Recommendation System(About)")

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
    pass


def Home():
    root.destroy()
    os.system('python PythonOngoingProject.py')


# Navigation Bar
Label(root, text="  Car Recommendation System  ", fg='white', bg='black', font=("Comic Sans MS", 25, "bold")).grid(row=0, column=0, columnspan=3)
Home_button = Button(root, text="Home", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Home).grid(row=0, column=3, columnspan=1)
About_button = Button(root, text="About", padx=20, pady=20, font=('', 20, ''), bg='black', fg='blue', command=About).grid(row=0, column=4, columnspan=1)
Search_vehicle_button = Button(root, text="(Recommendation)\nSearch vehicle", padx=20, pady=4, font=('', 20, ''), bg='black', fg='white', command=SearchVechile).grid(row=0, column=5, columnspan=1)
Login_button = Button(root, text="Login", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=Login).grid(row=0, column=6, columnspan=1)
Contact_button = Button(root, text="Contact Us", padx=20, pady=20, font=('', 20, ''), bg='black', fg='white', command=ContactUs).grid(row=0, column=7, columnspan=1)
# Navigation Bar Completed

Label(root, text="  What is a car Recommendation System  ?", fg='yellow', bg='black', font=("Comic Sans MS", 25, "bold", 'underline')).place(x=15, y=100)
Label(root, text="Recommendation systems are taking more importance in online businesses, where the ability to propose a new item or product that a user", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=150)
Label(root, text="will like can increase sales substantially. In this project, we propose to implement a web page where users can view certain types of", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=183)
Label(root, text="items, for example cars, and give their feedback about them, either explicitly (thumbs up / down, likes, ratings...) or implicitly ", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=216)
Label(root, text="items, for example cars, and give their feedback about them, either explicitly (thumbs up / down, likes, ratings...) or implicitly ", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=216)
Label(root, text="(clicking on item, spending time reading its description, sharing it..) Then, the system will run algorithms to come up with similar ", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=249)
Label(root, text="items to show to the user, and optionally collect feedback about the quality of the recommendation. Algorithms can range from simple ", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=282)
Label(root, text="similarity measures, to more complex machine learning models such as the SVM. Different topics of Data Science were applied, such as ", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=315)
Label(root, text="retrieving information, cleaning it for processing and storing it, evaluating algorithms for recommendation, and implementing big ", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=348)
Label(root, text="data processing pipelines. In other words, the system will study the user input throughout time, and recommend cars based on machine", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=381)
Label(root, text="data processing pipelines. In other words, the system will study the user input throughout time, and recommend cars based on machine ", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=414)
Label(root, text="learning algorithms. This way the user can look into prospective cars that meet his or her expectations..", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=447)

Label(root, text="  Why Choose Us  ", fg='yellow', bg='black', font=("Comic Sans MS", 25, "bold", 'underline')).place(x=15, y=480)
Label(root, text="We offer challenging degree programs at bachelors, Masters and Ph.D. level that offer high-quality teaching by outstanding and", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=530)
Label(root, text="experienced faculty. Our programs prepare students for either continued graduate education or for careers in business, industry,", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=563)
Label(root, text="or government. Further, our programs include a mix and balance of application-oriented course work and study of the underlying", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=596)
Label(root, text="theory and principles.", fg='white', bg='black', font=("Comic Sans MS", 15, "bold")).place(x=15, y=629)


root.mainloop()