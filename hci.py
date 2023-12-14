#hci program
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import sqlite3

def login(window):
    login_menu = tk.Tk()
    #window.destroy()
def register():
    register_menu = tk.Tk()
    register_menu.title("Register")
    register_menu.geometry("700x700")
    title = Label(resiger_menu, text = "Register an Account", font=("Arial", 20))
    root.destroy()
    register_menu.mainloop()
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

   # dia =
    

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

    r_button = Button(main_menu, text = 'Register', command = register)
    l_button = Button(main_menu, text = 'Login', command = login)
    help_button = Button(main_menu, text = 'Help', command = helper)
    exit_button = Button(main_menu, text = 'Exit', command = main_menu.destroy)

    r_button.place(x=211, y=100)
    l_button.place(x=211, y=120)
    r_button.activebackground('yellow')
    exit_button.pack(side = 'bottom')
    help_button.pack(side = 'bottom')
    
    main_menu.mainloop()
main()

