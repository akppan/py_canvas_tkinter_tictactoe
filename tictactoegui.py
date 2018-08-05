from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.geometry("450x700+400+0")


#===============================================================================

##DISPLAYGUITIC
c0=Canvas(root,width=200,height=40,bg="yellow")
c0.place(x=150,y=10)
i0=c0.create_text(100,20,text="Player "+str(1)+"\'s Turn",font=("Arial",16))
c1=Canvas(root,width=100,height=100,bg="yellow")
c1.place(x=100,y=100)
i1=c1.create_text(50,50,text='',font=("Arial",40))
c2=Canvas(root,width=100,height=100,bg="yellow")
c2.place(x=200,y=100)
i1=c2.create_text(50,50,text='',font=("Arial",40))
c3=Canvas(root,width=100,height=100,bg="yellow")
c3.place(x=300,y=100)
i1=c3.create_text(50,50,text='',font=("Arial",40))
c4=Canvas(root,width=100,height=100,bg="yellow")
c4.place(x=100,y=200)
i1=c4.create_text(50,50,text='',font=("Arial",40))
c5=Canvas(root,width=100,height=100,bg="yellow")
c5.place(x=200,y=200)
i1=c5.create_text(50,50,text='',font=("Arial",40))
c6=Canvas(root,width=100,height=100,bg="yellow")
c6.place(x=300,y=200)
i1=c6.create_text(50,50,text='',font=("Arial",40))
c7=Canvas(root,width=100,height=100,bg="yellow")
c7.place(x=100,y=300)
i1=c7.create_text(50,50,text='',font=("Arial",40))
c8=Canvas(root,width=100,height=100,bg="yellow")
c8.place(x=200,y=300)
i1=c8.create_text(50,50,text='',font=("Arial",40))
c9=Canvas(root,width=100,height=100,bg="yellow")
c9.place(x=300,y=300)
i1=c9.create_text(50,50,text='',font=("Arial",40))
c10=Canvas(root,width=250,height=60,bg="yellow")
c10.place(x=150,y=550)
i1=c10.create_text(50,50,text='',font=("Arial",40))


#============================================================================================

def rule():
    messagebox.showinfo(title="Rule Violation",message="This place is automatically filled")


#=============================================================================================


cond=1
p=0
turn=0
dictt={}
li=[]
global sign
global signp1
global signp2
signp2=StringVar()
siign=StringVar()

s=""
for i in range(9):
    li.append(s)



#=============================================================================================

def replay():
    global i0,i1
    global p,li
    global turn
    cond=1
    p=0
    turn=0
    dictt={}
    li=[]
    s=""
    for i in range(9):
        li.append(s)
    signp2=StringVar()
    siign=StringVar()
    try:
        c0.delete(i0)
        c0.create_text(100,20,text="Player "+str(1)+"\'s Turn",font=("Arial",16))
        c1.delete(i1)
        c1.create_text(0,0,text="",font=("Arial",40))
        c2.delete(i1)
        c2.create_text(50,50,text="",font=("Arial",40))
        c3.delete(i1)
        c3.create_text(50,50,text="",font=("Arial",40))
        c4.delete(i1)
        c4.create_text(50,50,text="",font=("Arial",40))
        c5.delete(i1)
        c5.create_text(50,50,text="",font=("Arial",40))
        c6.delete(i1)
        c6.create_text(50,50,text="",font=("Arial",40))
        c7.delete(i1)
        c7.create_text(50,50,text="",font=("Arial",40))
        c8.delete(i1)
        c8.create_text(50,50,text="",font=("Arial",40))
        c9.delete(i1)
        c9.create_text(50,50,text="",font=("Arial",40))
        c1.delete(i10)
        c10.create_text(50,50,text="",font=("Arial",40))
    except:
        pass
    print(li)


#===========================================================================================



def dictass():
    global dictt
    global signp1
    global signp2
    global sign
    signp1 = siign.get()
    if(signp1=='X'):
        signp2='O'
    else:
        signp2='X'
    dictt={'pl1':[signp1,1],'pl2':[signp2,2]}
    sign=signp1
    select.config(state='disabled')




##==========================================================================================


#### ASSIGNING VARIABLES
label=Label(root,text="Player 1's SIGN")
label.place(x=25,y=450)

select=ttk.Combobox(root,textvariable=siign,background="red")
select.place(x=25,y=490)
select.config(values=('X','O'))


btn=ttk.Button(root,text="ASSIGN",command=dictass)
btn.place(x=25,y=530)

btn1=ttk.Button(root,text="REPLAY",command=replay)
btn1.place(x=325,y=490)

btn2=ttk.Button(root,text="EXIT",command=root.destroy)
btn2.place(x=225,y=620)


#===========================================================================================

def place_marker():
    global p
    global turn
    global li
    global sign
    global dictt
    global signp1
    global signp2
    dictt={'pl1':[signp1,1],'pl2':[signp2,2]}
    print(sign)
    print(dictt)
    if(not win_check() and turn<9):
        if(cond==1):
            sign=dictt['pl'+str(int(not p)+1)][0]
            player_turn(dictt['pl'+str(int(not p)+1)][1])
            turn+=1
            p=not p
        elif(cond==0):
            p=p
    if(not win_check() and turn>=9):
        try:
            c10.delete(i)
            i=c10.create_text(125,30,text="Match Draw",font=("Arial",16))
        except NameError:
            i=c10.create_text(125,30,text="Match Draw",font=("Arial",16))
        #replay()
    elif(win_check()):
        player_win(dictt['pl'+str(int(p)+1)][1])
    
##============================================================================================


####DRAWING FUNCTIONS
def draw1(event):
    global li
    global i1
    global cond
    global sign
    if(li[0]==''):
        i1=c1.create_text(50,50,text=sign,font=("Arial",40))
        li[0]=sign
        cond=1
    elif(li[0]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        

def draw2(event):
    global li
    global i1
    global cond
    global sign
    if(li[1]==''):
        i1=c2.create_text(50,50,text=sign,font=("Arial",40))
        li[1]=sign
        cond=1
    elif(li[1]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        

def draw3(event):
    global li
    global i1
    global cond
    global sign
    if(li[2]==''):
        i1=c3.create_text(50,50,text=sign,font=("Arial",40))
        li[2]=sign
        cond=1
    elif(li[2]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        

def draw4(event):
    global li
    global i1
    global cond
    global sign
    if(li[3]==''):
        i1=c4.create_text(50,50,text=sign,font=("Arial",40))
        li[3]=sign
        cond=1
    elif(li[3]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        

def draw5(event):
    global li
    global i1
    global cond
    global sign
    if(li[4]==''):
        i1=c5.create_text(50,50,text=sign,font=("Arial",40))
        li[4]=sign
        cond=1
    elif(li[4]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        
    
def draw6(event):
    global li
    global i1
    global cond
    global sign
    if(li[5]==''):
        i1=c6.create_text(50,50,text=sign,font=("Arial",40))
        li[5]=sign
        cond=1
    elif(li[5]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
    

def draw7(event):
    global li
    global i1
    global cond
    global sign
    if(li[6]==''):
        i1=c7.create_text(50,50,text=sign,font=("Arial",40))
        li[6]=sign
        cond=1
    elif(li[6]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        

def draw8(event):
    global li
    global i1
    global cond
    global sign
    if(li[7]==''):
        i1=c8.create_text(50,50,text=sign,font=("Arial",40))
        li[7]=sign
        cond=1
    elif(li[7]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        

def draw9(event):
    global li
    global i1
    global cond
    global sign
    if(li[8]==''):
        i1=c9.create_text(50,50,text=sign,font=("Arial",40))
        li[8]=sign
        cond=1
    elif(li[8]!=''):
        cond=0
        rule()
    #print(li,sign)
    place_marker()
        



##============================================================================================


####HITCOMMANDS

c1.bind('<Button-1>',draw1)
c2.bind('<Button-1>',draw2)
c3.bind('<Button-1>',draw3)
c4.bind('<Button-1>',draw4)
c5.bind('<Button-1>',draw5)
c6.bind('<Button-1>',draw6)
c7.bind('<Button-1>',draw7)
c8.bind('<Button-1>',draw8)
c9.bind('<Button-1>',draw9)



##=============================================================================================

def win_check():
    if(li[0]==li[1]==li[2] and li[0]!=''):
        c1.itemconfig(i1,fill="cyan")
        c2.itemconfig(i1,fill="cyan")
        c3.itemconfig(i1,fill="cyan")
        return True
    if(li[3]==li[4]==li[5] and li[3]!=''):
        c4.itemconfig(i1,fill="cyan")
        c5.itemconfig(i1,fill="cyan")
        c6.itemconfig(i1,fill="cyan")
        return True
    if(li[6]==li[7]==li[8] and li[6]!=''):
        c7.itemconfig(i1,fill="cyan")
        c8.itemconfig(i1,fill="cyan")
        c9.itemconfig(i1,fill="cyan")
        return True
    if(li[0]==li[3]==li[6] and li[0]!=''):
        c1.itemconfig(i1,fill="cyan")
        c4.itemconfig(i1,fill="cyan")
        c7.itemconfig(i1,fill="cyan")
        return True
    if(li[1]==li[4]==li[7] and li[1]!=''):
        c2.itemconfig(i1,fill="cyan")
        c5.itemconfig(i1,fill="cyan")
        c8.itemconfig(i1,fill="cyan")
        return True
    if(li[2]==li[5]==li[8] and li[2]!=''):
        c3.itemconfig(i1,fill="cyan")
        c6.itemconfig(i1,fill="cyan")
        c9.itemconfig(i1,fill="cyan")
        return True
    if(li[0]==li[4]==li[8] and li[0]!=''):
        c1.itemconfig(i1,fill="cyan")
        c5.itemconfig(i1,fill="cyan")
        c9.itemconfig(i1,fill="cyan")
        return True
    if(li[2]==li[4]==li[6] and li[2]!=''):
        c3.itemconfig(i1,fill="cyan")
        c5.itemconfig(i1,fill="cyan")
        c7.itemconfig(i1,fill="cyan")
        return True

##============================================================================================

def space_check(pos):
    if(li[pos-1]==''):
        return True
    else:
        return False



##=============================================================================================

def full_board_check():
    while(replay()):
        global li
        li=[]
        s=""
        for i in range(9):
            li.append(s)
        player_input()

def player_win(pla):
    global sign
    sign=""
    try:
        c10.delete(i)
        i=c10.create_text(100,20,text="Player "+str(pla)+" Wins",font=("Arial",20))
    except NameError:
        i=c10.create_text(100,20,text="Player "+str(pla)+" Wins",font=("Arial",20))


##==============================================================================================


def player_turn(no):
    global i0
    try:
        c0.delete(i0)
        i0=c0.create_text(100,20,text="Player "+str(no)+"\'s Turn",font=("Arial",16))
    except NameError:
        i0=c0.create_text(100,20,text="Player "+str(no)+"\'s Turn",font=("Arial",16))






















