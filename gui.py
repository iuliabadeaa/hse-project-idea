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
    
def open_xor_gate_simulator():
    menu.destroy()
    root=Tk()
    root.title("XOR GATE")
    root.geometry("600x600")

    description=Label(root,text="XOR gate requires at least two inputs: ")
    description.place(x=100,y=100)
    input1=Label(root,text="A")
    input1.place(x=200,y=200)
    entry1=Entry(root)
    entry1.place(x=220,y=200)
    input2=Label(root,text="B")
    input2.place(x=200,y=300)
    entry2=Entry(root)
    entry2.place(x=220,y=300)
    img = ImageTk.PhotoImage(Image.open("xorgate.png"))
    label = Label(root, image = img)
    label.pack()
    label.place(x=270,y=200)

    def xorgate():
        x=int(entry1.get())
        y=int(entry2.get())
        if (x==0 or x==1) and (y==0 or y==1):
            if x==y:
                output=0
                description_label=Label(root,text="Output: ")
                description_label.place(x=500,y=250)
                and_label=Label(root,text=bool(output))
                and_label.place(x=550,y=250)
            else:
                output=1
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
        

    runbutton=Button(root,text="RUN",command=xorgate)
    runbutton.place(x=300,y=400)

    mainloop()

def open_nand_gate_simulator():
    menu.destroy()
    root=Tk()
    root.title("NAND GATE")
    root.geometry("600x600")

    description=Label(root,text="NAND gate requires at least two inputs: ")
    description.place(x=100,y=100)
    input1=Label(root,text="A")
    input1.place(x=200,y=200)
    entry1=Entry(root)
    entry1.place(x=220,y=200)
    input2=Label(root,text="B")
    input2.place(x=200,y=300)
    entry2=Entry(root)
    entry2.place(x=220,y=300)
    img = ImageTk.PhotoImage(Image.open("nandgate.png"))
    label = Label(root, image = img)
    label.pack()
    label.place(x=270,y=200)

    def orgate():
        x=int(entry1.get())
        y=int(entry2.get())
        if (x==0 or x==1) and (y==0 or y==1):
            output=not(x and y)
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
    
def open_nor_gate_simulator():
    menu.destroy()
    root=Tk()
    root.title("NOR GATE")
    root.geometry("600x600")

    description=Label(root,text="NOR gate requires at least two inputs: ")
    description.place(x=100,y=100)
    input1=Label(root,text="A")
    input1.place(x=200,y=200)
    entry1=Entry(root)
    entry1.place(x=220,y=200)
    input2=Label(root,text="B")
    input2.place(x=200,y=300)
    entry2=Entry(root)
    entry2.place(x=220,y=300)
    img = ImageTk.PhotoImage(Image.open("norgate.png"))
    label = Label(root, image = img)
    label.pack()
    label.place(x=270,y=200)

    def norgate():
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
        

    runbutton=Button(root,text="RUN",command=norgate)
    runbutton.place(x=300,y=400)

    mainloop()

def open_xnor_gate_simulator():
    menu.destroy()
    root=Tk()
    root.title("XNOR GATE")
    root.geometry("600x600")

    description=Label(root,text="XNOR gate requires at least two inputs: ")
    description.place(x=100,y=100)
    input1=Label(root,text="A")
    input1.place(x=200,y=200)
    entry1=Entry(root)
    entry1.place(x=220,y=200)
    input2=Label(root,text="B")
    input2.place(x=200,y=300)
    entry2=Entry(root)
    entry2.place(x=220,y=300)
    img = ImageTk.PhotoImage(Image.open("xnorgate.png"))
    label = Label(root, image = img)
    label.pack()
    label.place(x=270,y=200)

    def xnorgate():
        x=int(entry1.get())
        y=int(entry2.get())
        if (x==0 or x==1) and (y==0 or y==1):
            if x==y:
                output=1
                description_label=Label(root,text="Output: ")
                description_label.place(x=500,y=250)
                and_label=Label(root,text=bool(output))
                and_label.place(x=550,y=250)
            else:
                output=0
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
        

    runbutton=Button(root,text="RUN",command=xnorgate)
    runbutton.place(x=300,y=400)

    mainloop()

def open_not_gate_simulator():
    menu.destroy()
    root=Tk()
    root.title("NOT GATE")
    root.geometry("600x600")

    description=Label(root,text="NOT gate requires one input: ")
    description.place(x=100,y=100)
    input1=Label(root,text="A")
    input1.place(x=200,y=255)
    entry1=Entry(root)
    entry1.place(x=220,y=255)
    img = ImageTk.PhotoImage(Image.open("notgate.png"))
    label = Label(root, image = img)
    label.pack()
    label.place(x=270,y=200)

    def andgate():
        x=int(entry1.get())
        if (x==0 or x==1):
            output=not(x)
            description_label=Label(root,text="Output: ")
            description_label.place(x=500,y=255)
            and_label=Label(root,text=bool(output))
            and_label.place(x=550,y=255)

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

    resetbutton=Button(root,text="RESET",command=reset)
    resetbutton.place(x=400,y=400)
        

    runbutton=Button(root,text="RUN",command=andgate)
    runbutton.place(x=300,y=400)

    mainloop()

def exit_function():
    menu.destroy()

menu=Tk()
menu.title("MENU")
menu.geometry("400x200")
sugestive_label=Label(menu,text="Choose what gate you want to try: ")
sugestive_label.place(x=50,y=50)
and_button=Button(menu,text="AND GATE",command=open_and_gate_simulator)
and_button.place(x=100,y=100)
or_button=Button(menu,text="OR GATE",command=open_or_gate_simulator)
or_button.place(x=200,y=100)
xor_button=Button(menu,text="XOR GATE",command=open_xor_gate_simulator)
xor_button.place(x=300,y=100)
nand_button=Button(menu,text="NAND GATE",command=open_nand_gate_simulator)
nand_button.place(x=100,y=140)
nor_button=Button(menu,text="NOR GATE",command=open_nor_gate_simulator)
nor_button.place(x=200,y=140)
xnor_button=Button(menu,text="XNOR GATE",command=open_xnor_gate_simulator)
xnor_button.place(x=300,y=140)
not_button=Button(menu,text="NOT GATE",command=open_not_gate_simulator)
not_button.place(x=100,y=180)
exit_button=Button(menu,text="EXIT",command=exit_function)
exit_button.place(x=200,y=180)

mainloop()