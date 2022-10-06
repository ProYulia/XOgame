from tkinter import *
from tkinter import messagebox
import tkinter.font as font

window = Tk()
window.title("Крестики-нолики")

def chose_winner(mylist):
    winning_position = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],\
                       [1,4,7], [2,5,8],[6,4,2], [0,4,8]]
    for position in winning_position:
        if mylist[position[0]] == mylist[position[1]] == mylist[position[2]]\
         and mylist[position[0]] in ('X0'):
            if mylist[position[0]] == 'X':
                messagebox.showinfo("Congrats!", 'Победили крестики!')
                window.destroy()
            if mylist[position[0]] == '0':
                messagebox.showinfo("Congrats!", 'Победили нолики!')
                window.destroy()
    if ' ' not in mylist:
        messagebox.showinfo("Congrats!", 'Ничья!')
        window.destroy()

def push(board, cell):
    global turn
    if turn % 2 == 0:
        board[cell] = 'X'
        button[cell].config(text='X', state = 'disabled')
        turn += 1
    else:
        board[cell] = '0'
        button[cell].config(text='0', state = 'disabled')
        turn += 1
    if turn > 3:
        chose_winner(board)


mylist = [" "] * 9
turn = 0

myFont = font.Font(size = 42)
button = [Button( width = 2, height = 1, font = myFont, \
                 command = lambda x = i: push(mylist,x)) for i in range (9)]

row = 1; col = 0
for i in range(9):
    button[i].grid(row = row, column = col, sticky=W+E)
    col += 1
    if col == 3:
        row += 1; col = 0

label_1 = Label(height=3, text = 'Делайте ход')
label_1.grid(row = 4, column = 0, columnspan=3)

window.mainloop()
