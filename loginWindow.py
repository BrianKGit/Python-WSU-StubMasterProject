# login window
import functionsModule as tm
from tkinter import messagebox as mb
import tkinter as tk
# from PIL import ImageTk, Image
import eventGUI as eg
# import sys
# print(sys.path)
# print(sys.version)
root = tk.Tk()
XWIDTH = 500
YHEIGHT = 300

COLOR = '#4e83c9'
COLOR2 = '#8a00ad'
COLOR3 = '#ffaa00'
canvas = tk.Frame(root, height=YHEIGHT, width=XWIDTH, bg=COLOR3)
cCanvas = tk.Frame(root, height=YHEIGHT, width=XWIDTH, bg=COLOR3)


def createUserCommand():
    print('create pressed')
    canvas.pack_forget()
    createUserWindow()


def samePass(password, confirmPassword):
    if password == confirmPassword:
        print('         same')
        return True
    else:
        print('Passwords didnt match')
        return False
# =================================================================================================


def createUserWindow():
    def goBack():
        cCanvas.pack_forget()
        loginWindow()

    def tryCreate():
        print('attempt create, assume success')
        user = cUsernameField.get()
        name = cNameField.get()
        password = cPassField.get()
        confirmPassword = cConfirmField.get()
        # first see if name is taken
        if tm.notTaken(user):
            # then check passwords
            if samePass(password, confirmPassword):
                tm.createNewUser(user, name, password)
                # mb.showinfo('Oops', 'Successful creation bro!')
                cCanvas.pack_forget()
                loginWindow()
            else:
                cUsernameField.delete(0, tk.END)
                cNameField.delete(0, tk.END)
                cPassField.delete(0, tk.END)
                cConfirmField.delete(0, tk.END)
                mb.showinfo('Oops', 'Passwords do not match')
                print('Failed to create new user')
        else:
            mb.showinfo('Oops', 'User already exists')
    print('quitting login window')
    # switches into create user window
    root.title('Login')

    cCanvas.pack()
    cLeftArea = tk.Frame(cCanvas, bg=COLOR3)
    cLeftArea.place(rely=0, relx=0.05, relwidth=.43, relheight=.7)
    cRightArea = tk.Frame(cCanvas, bg=COLOR3)
    cRightArea.place(rely=0, relx=.52, relwidth=.43, relheight=.7)
    cBottomArea = tk.Frame(cCanvas, bg=COLOR3)
    cBottomArea.place(relx=.3, rely=.75, relwidth=.4, relheight=.2)
    # labels
    cUsername = tk.Label(cLeftArea, font=80, text='Enter Username:', bg=COLOR)
    cUsername.place(rely=.05, relwidth=1, relheight=.2)
    cName = tk.Label(cLeftArea, font=80, text='Name:', bg=COLOR)
    cName.place(rely=.3, relwidth=1, relheight=.2)
    cPass = tk.Label(cLeftArea, font=80, text='Enter Password:', bg=COLOR)
    cPass.place(rely=.55, relwidth=1, relheight=.2)
    cConfirmPass = tk.Label(cLeftArea, font=80, text='Confirm Password:', bg=COLOR)
    cConfirmPass.place(rely=.8, relwidth=1, relheight=.2)
    # fields
    cUsernameField = tk.Entry(cRightArea, font=80)
    cUsernameField.place(rely=.05, relwidth=1, relheight=.2)
    cNameField = tk.Entry(cRightArea, font=80)
    cNameField.place(rely=.3, relwidth=1, relheight=.2)
    cPassField = tk.Entry(cRightArea, font=80)
    cPassField.place(rely=.55, relwidth=1, relheight=.2)
    cConfirmField = tk.Entry(cRightArea, font=80)
    cConfirmField.place(rely=.8, relwidth=1, relheight=.2)
    # buttons
    goBackButton = tk.Button(cBottomArea, font=30, text='Back', padx=5, command=goBack)
    goBackButton.place(relx=0, relwidth=.4, relheight=1)
    tryCreateButton = tk.Button(cBottomArea, font=30, text='Create', padx=5, command=tryCreate)
    tryCreateButton.place(relx=.6, relwidth=.4, relheight=1)

    root.mainloop()
# ================================================================================================


def loginWindow():
    def loginCommand():
        print('--------------------------')
        print('login presssed')
        pullUser = nameField.get()
        pullPass = passField.get()
        print('name entered: ' + pullUser)
        print('pass entered: ' + pullPass)
        print('--------------------------')
        verified = tm.verifyUser(pullUser, pullPass)
        # with successful login
        if verified:
            root.quit()
            root.destroy()
            print('Starting event GUI')
            eg.runEventGUI(str(pullUser))
        else:
            nameField.delete(0, tk.END)
            passField.delete(0, tk.END)
            mb.showinfo('Oops', 'Login failed :(')

    # switches into login window
    root.title('Login')

    canvas.pack()
    leftArea = tk.Frame(canvas, bg=COLOR3)
    leftArea.place(rely=0, relx=0.05, relwidth=.43, relheight=.6)
    rightArea = tk.Frame(canvas, bg=COLOR3)
    rightArea.place(rely=0, relx=.52, relwidth=.43, relheight=.6)
    bottomArea = tk.Frame(canvas, bg=COLOR3)
    bottomArea.place(relx=.1, rely=.7, relwidth=.8, relheight=.2)
    # labels
    name = tk.Label(leftArea, font=80, text='Username:', bg=COLOR)
    name.place(rely=.4, relwidth=1, relheight=.2)
    password = tk.Label(leftArea, font=80, text='Password:', bg=COLOR)
    password.place(rely=.7, relwidth=1, relheight=.2)
    # fields
    nameField = tk.Entry(rightArea, font=80)
    nameField.place(rely=.4, relwidth=1, relheight=.2)
    passField = tk.Entry(rightArea, font=80)
    passField.place(rely=.7, relwidth=1, relheight=.2)
    # buttons
    loginButton = tk.Button(bottomArea, font=30, text='Login', padx=5, command=loginCommand)
    loginButton.place(rely=0, relx=0, relwidth=.4, relheight=1)

    createUserButton = tk.Button(bottomArea, font=30, text='Create User',
                                 padx=1, command=createUserCommand)
    createUserButton.place(rely=0, relx=.6, relwidth=.4, relheight=1)

    root.mainloop()


# createUserWindow()
loginWindow()
