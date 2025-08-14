from tkinter import *
import pyshorteners
window=Tk()
window.title("Areej-URL Shortener")
window.geometry("300x150")
icon=PhotoImage(file="pink.png")
window.iconphoto(True,icon)

def shorten():
    shortener=pyshorteners.Shortener()
    short_url=shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0,short_url)

# Creating Widgets
longurl_label=Label(window,text="Enter Long URL")
longurl_entry=Entry(window)
shorturl_label=Label(window,text="Username")
shorturl_entry=Entry(window)
Shorten_button=Button(window,text="Shorten URL",command=shorten)

# Placing Widgets on the screen
longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
Shorten_button.pack()

window.mainloop()



