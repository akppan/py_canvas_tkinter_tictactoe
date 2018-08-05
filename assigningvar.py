label=Label(root,text="Player 1's SIGN")
label.place(x=400,y=450)

siign=StringVar()
select=ttk.Combobox(root,textvariable=siign,background="red")
select.place(x=400,y=490)
select.config(values=('X','O'))
signp1 = siign.get()
if(signp1=='X'):
    signp2='O'
elif(signp1=='O'):
    signp2='X'

dictt={'pl1':[signp1,1],'pl2':[signp2,2]}
sign=signp1
#place_marker()
