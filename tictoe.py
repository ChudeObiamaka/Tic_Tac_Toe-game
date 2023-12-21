from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

#X starts so true
clicked = True
count = 0

#Button Clicked Function
def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1 
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "Hey that box has already been selected \nPick another box....")




b1 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b1))
b2 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b2))
b3 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b3))

b4 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b4))
b5 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b5))
b6 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b6))

b7 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b7))
b8 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b8))
b9 = tk.Button(text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b9))

#Grid our buttons to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

window.mainloop()