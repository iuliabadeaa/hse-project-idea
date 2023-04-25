from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Interface")
root.geometry("600x600")


# def if_not_zero_or_one():
#     if int(entry1.get())!=0 or int(entry1.get())!=1:
#         root.destroy()
#         error_root=Tk()
#         error_root.title("Error!")
#         error_label=Label(error_root,text="Input must be 0 or 1!")
#         error_label.configure(font="40,red")

description=Label(root,text="AND gate requires at least two inputs: ")
description.place(x=100,y=100)
input1=Label(root,text="A")
input1.place(x=200,y=200)
entry1=Entry(root)
entry1.place(x=220,y=200)
input2=Label(root,text="B")
input2.place(x=200,y=300)
entry2=Entry(root)
entry2.place(x=220,y=300)
img = ImageTk.PhotoImage(Image.open("andgate.png"))
label = Label(root, image = img)
label.pack()
label.place(x=270,y=200)

def andgate():
    x=int(entry1.get())
    y=int(entry2.get())
    if (x!=0 or x!=1) and (y!=0 or y!=1):
        root.destroy()
        error_root=Tk()
        error_root.title("Error!")
        error_label=Label(error_root,text="Input must be 0 or 1!")
        error_label.configure(font="40,red")
        error_label.place(x=30,y=80)    
    else:
        output=x and y
        description_label=Label(root,text="Output: ")
        description_label.place(x=500,y=250)
        and_label=Label(root,text=bool(output))
        and_label.place(x=550,y=250)
        

    

runbutton=Button(root,text="RUN",command=andgate)
runbutton.place(x=300,y=400)

mainloop()