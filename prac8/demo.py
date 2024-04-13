from tkinter import *
top=Tk()
top.geometry("200x200")
radio=IntVar()
r1=Radiobutton(top,text="hello brother").pack(anchor=W)
r2=Radiobutton(top,text="hello sister").pack(anchor=S)
r3=Radiobutton(top,text="hello friend").pack(anchor=E)
r4=Radiobutton(top,text="hello enemy").pack(anchor=N)
top.mainloop()
sb=Scrollbar(top)
sb.pack(side=RIGHT,fill=Y)
mylist=Listbox(top,xscrollcommand=sb.set)
en.pack()


