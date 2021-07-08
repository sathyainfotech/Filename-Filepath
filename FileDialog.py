from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import os

def myfile():

    global myImage

    filename=filedialog.askopenfilename(initialdir="H:/",title="Select File",filetype=(("PNG Files","*.png"),("JPG Files","*.jpg"),("JPEG Files","*.jpeg"),("All Files","*.*")))

    mylabel=Label(window,text=filename)
    mylabel.pack()

    image=Image.open(filename)
    resized=image.resize((250,300))
    myImage=ImageTk.PhotoImage(resized)

    imglbl=Label(window,image=myImage,height=300,width=250)
    imglbl.pack()

    # 0 - File Path
    # 1 - File Name

    data = os.path.split(filename)
    out=data[1]

    imglbl1 = Label(window, text=out)
    imglbl1.pack()

window=Tk()
window.geometry("500x500")
window.title("File Dialog")

btnFile=Button(window,text="Open File",bg="#1289A7",fg="white",width=10,font=("times",15,"bold"),command=myfile)
btnFile.pack(pady=30)

window.mainloop()

