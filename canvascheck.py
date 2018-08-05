from tkinter import *
from tkinter import messagebox


root=Tk()


c0=Canvas(root,width=250,height=40,bg="yellow")
c0.pack()

c1=Canvas(root,width=200,height=100,bg="yellow")
c1.pack()
c1

def sub():
    print(c0.itemcget(i,'text'))
    messagebox.showinfo(title="Rule Violation",message="This place is automatically filled")

def draw(event):
    global i
    i=c0.create_text(50,50,text="O",font=("Arial",40))

c0.bind('<Button-1>',draw)
def dele():
    try:
        c0.delete(i)
        i=c0.create_text(0,0,text="Player "+str(6)+"\'s Turn",font=("Arial",16))
    except NameError:
        i=c0.create_text(0,0,text="Player "+str(6)+"\'s Turn",font=("Arial",16))

btn=Button(root,text="Submit",command=sub)
btn.pack()

btn=Button(root,text="Delete",command=dele)
btn.pack()

i=c0.create_text(125,20,text="Player "+str(5)+"\'s Turn",font=("Arial",16))
