from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

# X starts so true
clicked = True
count = 0


#disable all the buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#Check to see if someone won
def check_if_won():
    global winner
    winner = False #if there already a winner,winner be change to true then the game will stop otherwise the game will continue

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
      b1.config(bg="purple")
      b2.config(bg="purple")
      b3.config(bg="purple")
      winner = True
      messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
      disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="purple")
        b5.config(bg="purple")
        b6.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="purple")
        b8.config(bg="purple")
        b9.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="purple")
        b4.config(bg="purple")
        b7.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="purple")
        b5.config(bg="purple")
        b8.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "" and b9["text"] == "X":
        b3.config(bg="purple")
        b6.config(bg="purple")
        b9.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="purple")
        b5.config(bg="purple")
        b9.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="purple")
        b5.config(bg="purple")
        b7.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! X WINS")
        disable_all_buttons()
    #Check for O WINS
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
      b1.config(bg="purple")
      b2.config(bg="purple")
      b3.config(bg="purple")
      winner = True
      messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
      disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="purple")
        b5.config(bg="purple")
        b6.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="purple")
        b8.config(bg="purple")
        b9.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="purple")
        b4.config(bg="purple")
        b7.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="purple")
        b5.config(bg="purple")
        b8.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="purple")
        b6.config(bg="purple")
        b9.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
        disable_all_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="purple")
        b5.config(bg="purple")
        b9.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="purple")
        b5.config(bg="purple")
        b7.config(bg="purple")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulation! O WINS")
        disable_all_buttons()



# Button Clicked Function
def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_if_won()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_if_won()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey that box has already been selected \nPick another box....")
#define reset
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count= 0
    b1 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = tk.Button(text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # Grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#Create Menu
my_menu = Menu(window)
window.config(menu=my_menu)

#Create Options
OptionMenu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=OptionMenu)
OptionMenu.add_command(label="Reset Game", command=reset)
reset()
window.mainloop()
