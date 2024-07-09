from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
from time import sleep
from threading import Thread # Chạy theo luồng

window = Tk()
window.title("CV Tkinter")
# window.geometry('800x600')

cap = cv2.VideoCapture(0)
canvas_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH) // 2
canvas_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2
canvas = Canvas(window, width=canvas_w, height=canvas_h, background="red")
canvas.pack()

b_w = 0
def handlebw():
    global b_w
    b_w= 1 - b_w

but = Button(window, text="Đen trắng", command=handlebw)
but.pack()

photo = None
count = 0

def send_to_server():
    global but
    sleep(10)
    but.configure(text="Binh.TX")
    return
def update_frame():
    global canvas, photo, b_w, count
    ret, frame = cap.read()
    frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
    if b_w == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    count += 1
    if count % 10 == 0:
        # send_to_server()
        thread = Thread(target=send_to_server)
        thread.start()

    window.after(19, update_frame)


update_frame()

window.mainloop()