from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Areej-Login Form")
window.geometry("500x500")
window.configure(bg="#333333")
icon=PhotoImage(file="pink.png")
window.iconphoto(True,icon)

def login():
    username="Areej"
    password="12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success",message=" You Successfully Logged in")
    else:
        messagebox.showerror(title="Error!",message=" Invalid Login")

frame=Frame(bg="#333333")

# Creating Widgets
login_label=Label(frame,text="Login",bg="#333333",fg="#FF3399",font=("Arial",30))
icon1=PhotoImage(file="user.png")
username_label=Label(frame,text="Username",bg="#333333",fg="#FFFFFF",font=("Arial",16),image=icon1,compound="left")
username_entry=Entry(frame,font=("Arial",16))
password_entry=Entry(frame,show="*",font=("Arial",16))
icon2=PhotoImage(file="lock.png")
password_label=Label(frame,text="Password",bg="#333333",fg="#FFFFFF",font=("Arial",16),image=icon2,compound="left")
login_button=Button(frame,text="Login",bg="#FF3399",fg="#FFFFFF",font=("Arial",16),command=login)

# Placing Widgets on the screen
login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)

frame.pack()
window.mainloop()



