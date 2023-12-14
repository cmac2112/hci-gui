#hci program

#this program is meant to be used in the window it spawns
#do not maximize the window or it will alter the gui buttons

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import sqlite3 #not used yet
def register_helper():
    print('wip')
    
def login(window):
    login_menu = tk.Tk()
    #window.destroy()
    
def register():
    #initialize window and other utilities
    register_menu = tk.Toplevel()
    register_menu.title("Register")
    register_menu.geometry("700x700")
    register_menu.configure(bg='black')
    registertitle = Label(register_menu, text = "Register an Account", font=("Arial", 20))

    exit_button = Button(register_menu, text = 'Exit', command = register_menu.destroy)
    help_button = Button(register_menu, text = 'Help', command = register_helper)
    exit_button.pack(side = 'bottom')
    help_button.pack(side = 'bottom')

    #get info from user

    #radio gender selection
    #use get to create text box

    
    #entry for username
    username_label = Label(register_menu, text = "Username", font=("Arial", 8))
    username_entry =''
    username = Entry(register_menu, textvariable = username_entry)
    username.place(x=275, y=255)
    username_label.place(x=276, y=237)
    #entry for password
    password_label = Label(register_menu, text = "Password", font=("Arial", 8))
    password_entry = ''
    password = Entry(register_menu, textvariable = password_entry, show='*')

    password_label.place(x=276, y=276)
    password.place(x=275, y=290)
    #gather some information to store into database for later
    gender = ''
    gender_button = Radiobutton(register_menu, text='Male', variable = gender, value=1)
    gender_button2 = Radiobutton(register_menu, text='Female', variable = gender, value=2)
    #value 1 = male, value = 2 female

    gender_button.place(x=275, y=325)
    gender_button2.place(x=275, y=345)
    
    
    registertitle.pack()
def helper():
    help_menu = tk.Toplevel()
    help_menu.title("Help")

    help_menu.geometry("400x400")
    helptitle = Label(help_menu, text = "Help", font=("Arial", 20))
    helptitle.pack()
    message = 'For new users: register an account by selecting the register button'
    message2 = 'For returning users: login by selecting the register button'
    message3 = 'Exit by selecting the exit button'

    message1var = Message(help_menu, text = message)
    message1var.config(bg='lightgreen')
    message2var = Message(help_menu, text = message2)
    message2var.config(bg='lightgreen')
    message3var = Message(help_menu, text = message3)
    message3var.config(bg='lightgreen')

    message1var.pack()
    message2var.pack()
    message3var.pack()

    

def main():
    #enter main menu
    #have two options plus help button

    #create window object named main menu
    main_menu = tk.Tk()

    #gives window a title at top
    main_menu.title("Main Menu")

    #defines the size of the window
    main_menu.geometry('500x500')
    main_menu.configure(bg = 'black')

    #label puts text on the window
    title1 = Label(main_menu, text = "Simple User Database", font=("Arial", 30)).pack()
    version = Label(main_menu, text = "Version 1.0.0", font=("Arial",10))

    version.place(x=0, y=480)

    r_button = Button(main_menu, text = 'Register', command = register)
    l_button = Button(main_menu, text = 'Login', command = login)
    help_button = Button(main_menu, text = 'Help', command = helper)
    exit_button = Button(main_menu, text = 'Exit', command = main_menu.destroy)

    r_button.place(x=211, y=225)
    l_button.place(x=211, y=250)
    exit_button.pack(side = 'bottom')
    help_button.pack(side = 'bottom')
    
    main_menu.mainloop()
main()

