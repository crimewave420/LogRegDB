from tkinter import *
from tkinter import messagebox

import domain

class MainScreen():
    
    def __init__(self):
        self.screen=Tk()
        self.screen.geometry("300x250")
        self.screen.title("Notes")
    
        Label(text = "Notes",bg="grey",height="2",width="300",font = ("Calibri",12)).pack()
        Label(text="").pack()
        Button(text = "Login",width=30,height=2).pack()
        Label(text="").pack()
        Button(text = "Register",height="2",width="30",command=self.regButton).pack()
        self.screen.mainloop()

    def regButton(self):
        self.screen.withdraw()
        reg = RegisterScreen(self.screen)
       
        
        


class RegisterScreen():
    
    def __init__(self, mainscreen):
        self.screenreg = Toplevel(mainscreen)
        self.username = StringVar()
        self.password =StringVar()

    
        self.screenreg.geometry("300x250")
        self.screenreg.title("Register")
        Label(self.screenreg,text="username").pack()
        Label(text="").pack
        Entry(self.screenreg,textvariable=self.username).pack()
        Label(text="").pack()
        Label(self.screenreg,text="password").pack()
        Label(text="").pack()
        Entry(self.screenreg,textvariable=self.password).pack()
        Label(text="").pack()
        Button(self.screenreg,text = "Submit",height="1",width="5",command=self.register_user).pack()

    def register_user(self):
        user = domain.User(self.username.get(),self.password.get())
        
        
        
        

MainScreen()