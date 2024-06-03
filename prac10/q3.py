# Write python GUI to make font menu with listbox


from tkinter import *
from tkinter import font


root = Tk()
root.title("Font Menu")
root.geometry('500x250')
font_name = "Arial"
font_size_name = 12
font_style_name = "normal"


def change_font():
    font_name = font_list.get(font_list.curselection())
    customFont = font.Font(
        family=font_name, size=font_size_name, weight=font_style_name)
    text.config(font=customFont)


def change_font_size():
    font_size_name = font_size.get(font_size.curselection())
    customFont = font.Font(
        family=font_name, size=int(font_size_name), weight=font_style_name)
    text.config(font=customFont)


def change_font_style():
    font_style_name = font_style.get(font_style.curselection())
    customFont = font.Font(
        family=font_name, size=font_size_name, weight=font_style_name)
    text.config(font=customFont)


font_list = Listbox(root, selectmode=SINGLE)
font_list.grid(row=0, column=0)
fontbtn = Button(root, text="Font", command=change_font)
fontbtn.grid(row=1, column=0)

for f in font.families():
    font_list.insert(END, f)

font_style = Listbox(root, selectmode=SINGLE)
font_style.grid(row=0, column=1)
stylebtn = Button(root, text="Style", command=change_font_style)
stylebtn.grid(row=1, column=1)

for s in ['normal', 'bold']:
    font_style.insert(END, s)


font_size = Listbox(root, selectmode=SINGLE)
font_size.grid(row=0, column=2)
sizebtn = Button(root, text="Size", command=change_font_size)
sizebtn.grid(row=1, column=2)

for i in range(8, 25):
    font_size.insert(END, i)


text = Label(root, text="Hello World", font=("Arial", 12))
text.grid(row=2, column=0, columnspan=2)


root.mainloop()
