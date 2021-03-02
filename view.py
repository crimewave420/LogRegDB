from tkinter import *
from tkinter import messagebox
from controller import Controller
import domain

class MainScreen():
    
    def __init__(self):
        self.screen=Tk()
        self.screen.geometry("300x250")
        self.screen.title("Notes")
        self.controller =  Controller()
        Label(text = "Notes",bg="grey",height="2",width="300",font = ("Calibri",12)).pack()
        Label(text="").pack()
        Button(text = "Login",width=30,height=2).pack()
        Label(text="").pack()
        Button(text = "Register",height="2",width="30",command=self.regButton).pack()
        self.screen.mainloop()

    def regButton(self):
        
        reg = RegisterScreen(self.screen,self.controller)
       
        
        


class RegisterScreen():
    
    def __init__(self, mainscreen,controller):
        self.screenreg = Toplevel(mainscreen)
        self.username = StringVar()
        self.password =StringVar()
        self.controller = controller
    
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
        Button(self.screenreg,text = "Submit",height="1",width="5",command=self.register_user).pack(side=RIGHT, padx=50)
        Button(self.screenreg,text = "Back",height="1",width="5",command=self.back).pack(side=LEFT,padx=50)

    def register_user(self):
        user = domain.User(self.username.get(),self.password.get())
        try:
            self.controller.add_user(user)
        except domain.CommitException as arg:
            messagebox.showerror(master=self.screenreg,title="Failed",message=arg)
        except domain.QuerryException as arg:
            messagebox.showerror(title="Failed",message=arg)
        except domain.UserExistsException as arg:
            messagebox.showerror(title="failed",message=arg)
        else:
            messagebox.showinfo(title="Sucess",message="User {uuser} was successfully added".format(uuser=user))
            self.controller.close_connection()
            self.screenreg.withdraw()
    def back(self):
        self.screenreg.withdraw()
        
        
MainScreen()