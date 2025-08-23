import tkinter,PyPDF2
from tkinter import filedialog
from tkinter import *
def openfile():
 filename=filedialog.askopenfilename(title="Open PDF file",initialdir="Documents",filetypes=[('PDF files','*.pdf')])
 print(filename)
 file_label.configure(text=filename)
 outputfile_text.delete("1.0",END)
 reader =PyPDF2.PdfReader(filename)
 for i in range(len(reader.pages)):
  page = reader.pages[i]
  text = page.extract_text()
  outputfile_text.insert(END,text)

window=Tk()
window.title("Areej-PDF Text Extractor")
icon=PhotoImage(file="pink.png")
window.iconphoto(True,icon)

file_label=Label(window,text="No File Selected ")
outputfile_text=Text(window)
outputfile_button=Button(window,text="Open PDF File",command=openfile)

file_label.pack()
outputfile_text.pack()
outputfile_button.pack()
window.mainloop()