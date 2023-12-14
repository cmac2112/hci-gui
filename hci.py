#hci program

#this program is meant to be used in the window it spawns
#do not maximize the window or it will alter the gui buttons
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import sqlite3 #not used yet
def edit_profile():
    edit_profile = tk.Toplevel()
    edit_profile.title("Edit Profile")

    edit_profile.geometry("500x500")
    edit_profile.configure(bg="black")
    curr_username = Label(edit_profile, text='(current username placeholder)', font=("Arial", 10))
    change_password = Label(edit_profile, text='Enter current password here', font=("Arial", 10))

    username_label = Label(edit_profile, text = 'Enter new username below', font = ("Arial", 10))
    get_username = Entry(edit_profile)
    get_password = Entry(edit_profile) #no variables to hold new vaules right now

    username_label.place(x=100, y=100)
    get_username.place(x=100, y=130)
    change_password.place(x=100, y=200)
    get_password.place(x=100, y=230)

    confirm = Button(edit_profile, text='Confirm', command = edit_profile.destroy)
    exit_edit = Button(edit_profile, text = 'Exit', command = edit_profile.destroy)

    confirm.place(x=100, y=260)
    exit_edit.place(x=100, y=290)
def profile_helper():
    profile_helper = tk.Toplevel()
    profile_helper.title("Help")

    profile_helper.geometry("400x400")
    helptitle = Label(profile_helper, text = "Help", font=("Arial", 20))
    helptitle.pack()
    message = 'This is your profile page, here you can view and do many different things'
    message2 = 'To search for other users, enter the username to search in the box named "search other users" and click search'
    message3 = 'To edit your profile information, click the "edit profile" button'
    message4 = 'To exit click exit'
    message1var = Message(profile_helper, text = message)
    message1var.config(bg='lightgreen')
    message2var = Message(profile_helper, text = message2)
    message2var.config(bg='lightgreen')
    message3var = Message(profile_helper, text = message3)
    message3var.config(bg='lightgreen')
    message4var =  Message(profile_helper, text = message4)
    message4var.config(bg='lightgreen')
    

    message1var.pack()
    message2var.pack()
    message3var.pack()
    message4var.pack()
def not_found(root):
    label = Label(root, text = "user not found")
    label.configure(background='red')
    label.place(x=50, y=550)
def profile():
    profile_page = tk.Tk()
    profile_page.title("Profile")
    profile_page.geometry('700x700')
    profile_label = Label(profile_page, text = 'Welcome (username)', font=("Arial", 20))
    profile_label.pack()

    profile_page.config(bg='black')

    search_label = Label(profile_page, text = 'Search other users', font=("Arial", 8))
    search_term = ''
    search_button = Button(profile_page, text = "Search", command = lambda root = profile_page: not_found(root))
    search_box = Entry(profile_page, textvariable=search_term)
    #at this point we would check if our search term to search for users would match any in the
    #database, but once again i have not made the database yet so imagine this works
    search_label.place(x=50, y=460)
    search_box.place(x=50, y=480)
    search_button.place(x=50, y=500)

    #this scroll bar will hold saved users by the user
    scrollbar = Scrollbar(profile_page)
    scrollbar.pack(side = RIGHT, fill = Y)
    saved_users = Listbox(profile_page, yscrollcommand = scrollbar.set)
    for lines in range(100):
        saved_users.insert(END, 'Saved user:' +str(lines))
    saved_users.pack(side=RIGHT, fill=BOTH)
    scrollbar.config(command=saved_users.yview)

    #make edit profile button and functionality
    edit_button = Button(profile_page, text="Edit Your Profile", command = edit_profile)
    edit_button.place(x=228, y=460)

    exit_button = Button(profile_page, text="Exit", command = profile_page.destroy)
    help_button = Button(profile_page, text="Help",command = profile_helper)
    
    exit_button.pack(side='bottom')
    help_button.pack(side='bottom')

    saved_label = Label(profile_page, text = 'Users you have saved', font=("Arial", 8))
    saved_label.place(x=575, y=15)

    placeholder = Label(profile_page, text = 'Placeholder for custom', font=("Arial", 30))
    placeholder2 = Label(profile_page, text = 'Image set by user', font=("Arial", 30))
    placeholder.place(x=65, y=100)
    placeholder2.place(x=110, y=150)

    del_saved = Button(profile_page, text='Delete Saved User') #no command currently
    del_saved.place(x=400, y=460)
    
def login_helper():
    help_menu = tk.Toplevel()
    help_menu.title("Help")

    help_menu.geometry("400x400")
    helptitle = Label(help_menu, text = "Help", font=("Arial", 20))
    helptitle.pack()
    message = 'If you do not already have an account, click exit and go to register'
    message2 = 'For returning users: Login by entering the correct information on the login screen'
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
    
def register_helper():
    help_menu = tk.Toplevel()
    help_menu.title("Help")

    help_menu.geometry("400x400")
    helptitle = Label(help_menu, text = "Help", font=("Arial", 20))
    helptitle.pack()
    message = 'Please enter the required fields located on the register page'
    message2 = 'When you are done click register to register your account'
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
    
def login():
    login_menu = tk.Toplevel()
    login_menu.title("Login")
    login_menu.geometry("700x700")
    login_menu.configure(bg="black")
    login_title = Label(login_menu, text = "Login", font=("Arial", 20))

    help_button = Button(login_menu, text="Help", command = login_helper)
    exit_button = Button(login_menu, text="Exit", command = login_menu.destroy)

    exit_button.pack(side = 'bottom')
    help_button.pack(side = 'bottom')
    login_title.pack()

    username_label = Label(login_menu, text = "Username", font=("Arial", 8))
    username_entry =''
    username = Entry(login_menu, textvariable = username_entry)
    
    username.place(x=275, y=255)
    username_label.place(x=276, y=237)
    #entry for password
    password_label = Label(login_menu, text = "Password", font=("Arial", 8))
    password_entry = ''
    password = Entry(login_menu, textvariable = password_entry, show='*')

    password_label.place(x=276, y=276)
    password.place(x=275, y=290)


    #at this point we would check if password and username are valid in the database
    #but i dont have time to do so right now for this project at least maybe later if i get bored
    #one day

    #so for now we will just have a login button that takes us to the profile screen

    login_button = Button(login_menu, text="Login", command = profile)
    login_button.place(x=276, y=350)
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

    register_button = Button(register_menu, text="Register", command = register_menu.destroy)
    register_button.place(x=275, y=370)
    
    
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

