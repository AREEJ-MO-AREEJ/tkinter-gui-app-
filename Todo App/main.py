from customtkinter import *
def add():
    todo=entry.get()
    label=CTkLabel(scorable_frame,text=todo)
    label.pack()
    entry.delete(0,"end")

window=CTk()
window.geometry("750x450")
window.title("Areej-Todo App")

title_label=CTkLabel(window,text="Daily Tasks",font=CTkFont(size=30,weight="bold"))
title_label.pack(padx=10,pady=(40,20))

scorable_frame=CTkScrollableFrame(window,width=500,height=200)
scorable_frame.pack()

entry=CTkEntry(scorable_frame,placeholder_text="Add todo")
entry.pack(fill="x")

add_label=CTkButton(window,text="Add",width=500,command=add)
add_label.pack(pady=20)

window.mainloop()