import tkinter as tk
root = tk.Tk()
root.title("Hello, World!")
root.geometry('500x250')

label = tk.Label(root, text="Enter the weight in kg : ")
label.grid(row=0, column=0,padx=10,pady=5)
entry = tk.Entry(root)
entry.grid(row=0, column=1,padx=10,pady=5)

def convert():
    weight = float(entry.get())
    gram = weight * 1000
    pound = weight * 2.20462
    ounce = weight * 35.274
    gram_label.config(text="grams: " + str(gram))
    pound_label.config(text="pounds: " + str(pound))
    ounce_label.config(text="ounces: " + str(ounce))


convert_btn = tk.Button(root, text="Convert", command=convert)
convert_btn.grid(row=0, column=2,padx=10,pady=5)

gram_label = tk.Label(root, text="grams: ")
gram_label.grid(row=1, column=0,padx=10,pady=5)
pound_label = tk.Label(root, text="pounds: ")
pound_label.grid(row=1, column=1,padx=10,pady=5)
ounce_label = tk.Label(root, text="ounces: ")
ounce_label.grid(row=1, column=2,padx=10,pady=5)
tk.mainloop()
