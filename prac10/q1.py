import tkinter as tk
root = tk.Tk()
root.title("Hello, World!")
root.geometry('300x250')

def get_data():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    nums = [num1, num2]
    return nums


def add():
    nums = get_data()
    result = nums[0] + nums[1]
    result_label.config(text="Result: " + str(result))


def sub():
    nums = get_data()
    result = nums[0] - nums[1]
    result_label.config(text="Result: " + str(result))


def mul():
    nums = get_data()
    result = nums[0] * nums[1]
    result_label.config(text="Result: " + str(result))


def div():
    nums = get_data()
    result = nums[0] / nums[1]
    result_label.config(text="Result: " + str(result))


label1 = tk.Label(root, text="Enter Number 1")
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(root, text="Enter Number 2")
label2.grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

button = tk.Button(root, text="Add", command=add)
button.grid(row=2, column=0, padx=10, pady=5)

button = tk.Button(root, text="Subtract", command=sub)
button.grid(row=2, column=1, padx=10, pady=5)

button = tk.Button(root, text="Multiply", command=mul)
button.grid(row=3, column=0, padx=10, pady=5)

button = tk.Button(root, text="Divide", command=div)
button.grid(row=3, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, padx=10, pady=5)

tk.mainloop()
