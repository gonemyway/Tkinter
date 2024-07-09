from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("By tao")
window.geometry('800x600')

# Them label
label = tkinter.Label(window, text="Hi!", fg="red", font=("Times New Roman", 60))
label.grid(column=0, row=0)

# Textbox
txt = Entry(window, width=100)
txt.grid(column=0, row=1)

def abc():
    # label.configure(text="Hi, " + txt.get())
    messagebox.showinfo("Test", "Hi, " + combo.get())
    return
# Button
but = Button(window, text="Say Cobham", command=abc)
but.grid(column=1, row=1)

# ComboBox
combo = Combobox(window)
combo['values'] = ("Chọn 1 cái", "Người 1", "Người 2", "Người 3")
combo.grid(column=0, row=2)
combo.current(0)
def abc1():
    label.configure(text="Hi, " + combo.get())
    return
but = Button(window, text="Ấn vào đây", command=abc1)
but.grid(column=1, row=2)

window.mainloop()