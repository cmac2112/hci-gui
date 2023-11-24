#hci program
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import sqlite3


def main():
    #enter main menu
    #have two options plus help button

    #create window object named main menu
    main_menu = tk.Tk()

    #gives window a title at top
    main_menu.title("Main Menu")

    #defines the size of the window
    main_menu.geometry('1920x1080')

    #label puts text on the window
    title1 = Label(main_menu, text = "Simple User Database", font=("Arial", 30)).pack()

    r_button = Button(main_menu, text = 'Register', command = main_menu.destroy)
    l_button = Button(main_menu, text = 'Login', command = main_menu.destroy)
    help_button = Button(main_menu, text = 'Help', command = main_menu.destroy)

    r_button.pack(side = 'right')
    l_button.pack(side = 'left')
    help_button.pack(side = 'bottom')
    main_menu.mainloop()
main()

