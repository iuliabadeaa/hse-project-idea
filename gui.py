from tkinter import *
from PIL import Image, ImageTk


def open_and_gate_simulator():
    menu.destroy()
    root=Tk()
    root.title("AND GATE")
    root.geometry("600x600")

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
        if (x==0 or x==1) and (y==0 or y==1):
            output=x and y
            description_label=Label(root,text="Output: ")
            description_label.place(x=500,y=250)
            and_label=Label(root,text=bool(output))
            and_label.place(x=550,y=250)

        else:
            root.destroy()
            error_root=Tk()
            error_root.title("Error!")
            error_label=Label(error_root,text="Input must be 0 or 1!")
            error_label.configure(font="40,red")
            error_label.place(x=30,y=80)
            mainloop() 
            

    def reset():
        entry1.delete(0,END)
        entry2.delete(0,END)

    resetbutton=Button(root,text="RESET",command=reset)
    resetbutton.place(x=400,y=400)
        

    runbutton=Button(root,text="RUN",command=andgate)
    runbutton.place(x=300,y=400)

    mainloop()


def open_or_gate_simulator():
    menu.destroy()
    root=Tk()
    root.title("OR GATE")
    root.geometry("600x600")

    description=Label(root,text="OR gate requires at least two inputs: ")
    description.place(x=100,y=100)
    input1=Label(root,text="A")
    input1.place(x=200,y=200)
    entry1=Entry(root)
    entry1.place(x=220,y=200)
    input2=Label(root,text="B")
    input2.place(x=200,y=300)
    entry2=Entry(root)
    entry2.place(x=220,y=300)
    img = ImageTk.PhotoImage(Image.open("orgate.png"))
    label = Label(root, image = img)
    label.pack()
    label.place(x=270,y=200)

    def orgate():
        x=int(entry1.get())
        y=int(entry2.get())
        if (x==0 or x==1) and (y==0 or y==1):
            output=x or y
            description_label=Label(root,text="Output: ")
            description_label.place(x=500,y=250)
            and_label=Label(root,text=bool(output))
            and_label.place(x=550,y=250)

        else:
            root.destroy()
            error_root=Tk()
            error_root.title("Error!")
            error_label=Label(error_root,text="Input must be 0 or 1!")
            error_label.configure(font="40,red")
            error_label.place(x=30,y=80)
            mainloop() 
            

    def reset():
        entry1.delete(0,END)
        entry2.delete(0,END)

    resetbutton=Button(root,text="RESET",command=reset)
    resetbutton.place(x=400,y=400)
        

    runbutton=Button(root,text="RUN",command=orgate)
    runbutton.place(x=300,y=400)

    mainloop()

menu=Tk()
menu.title("MENU")
menu.geometry("500x500")
sugestive_label=Label(menu,text="Choose what gate you want to try: ")
sugestive_label.place(x=50,y=50)
and_button=Button(menu,text="AND GATE",command=open_and_gate_simulator)
and_button.place(x=100,y=100)
or_button=Button(menu,text="OR GATE",command=open_or_gate_simulator)
or_button.place(x=200,y=100)


mainloop()