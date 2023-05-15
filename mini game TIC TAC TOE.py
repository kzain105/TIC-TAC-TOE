# first setup the variables
from tkinter import*
import tkinter.messagebox
# for displaying the screen
screen = Tk()
# it will import and setup the icon
screen.iconbitmap('tic tac toe.ico')
# for giving the title to the creen
screen.title('My Tic Tac Toe')

# for setting up the colors
white = '#FFFFFF'
black = '#000000'
red = '#FF0000'
green = '#00FF00'
magneta = '#FF00FF'

# it will not allow the user to resize the window from width/height
screen.resizable(width = False, height = False)
# Global variable
turn = True
# global variable and will keep track of the number of moves made
count = 0
# these will be assigned to text variables inorders to display boxes
control1 = StringVar()
control2 = StringVar()
control3 = StringVar()
control4 = StringVar()
control5 = StringVar()
control6 = StringVar()
control7 = StringVar()
control8 = StringVar()
control9 = StringVar()
# will bring the X and O image in the tic tac board
x_image = PhotoImage(file='X.png')
o_image = PhotoImage(file='O.png')
# this function will contain the game and display it
def player():
    button1 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F8F8FF', textvariable=control1,
                     command=lambda: press(1, 0, 0))
    button1.grid(row=0, column=0)

    button2 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F8F8FF' , textvariable=control2,
                     command=lambda: press(2, 0, 1))
    button2.grid(row=0, column=1)

    button3 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F8F8FF', textvariable=control3,
                     command=lambda: press(3, 0, 2))
    button3.grid(row=0, column=2)

    button4 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F0F8FF', textvariable=control4,
                     command=lambda: press(4, 1, 0))
    button4.grid(row=1, column=0)

    button5 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F0F8FF', textvariable=control5,
                     command=lambda: press(5, 1, 1))
    button5.grid(row=1, column=1)

    button6 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F0F8FF', textvariable=control6,
                     command=lambda: press(6, 1, 2))
    button6.grid(row=1, column=2)

    button7 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F0FFFF', textvariable=control7,
                     command=lambda: press(7, 2, 0))
    button7.grid(row=2, column=0)

    button8 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F0FFFF', textvariable=control8,
                     command=lambda: press(8, 2, 1))
    button8.grid(row=2, column=1)

    button9 = Button(screen, height=15, width=28, borderwidth=1.5, relief='ridge', background= '#F0FFFF' , textvariable=control9,
                     command=lambda: press(9, 2, 2))
    button9.grid(row=2, column=2)

# this function will check which button user have pressed
def press(number, y, z):
    global turn, count
    if turn == True:
        labelPhoto = Label(screen, image=o_image) # will import image
        labelPhoto.grid(row=y, column=z)
        if number == 1:
            control1.set('O')
        elif number == 2:
            control2.set('O')
        elif number == 3:
            control3.set('O')
        elif number == 4:
            control4.set('O')
        elif number == 5:
            control5.set('O')
        elif number == 6:
            control6.set('O')
        elif number == 7:
            control7.set('O')
        elif number == 8:
            control8.set('O')
        else:
            control9.set('O')
        count = count + 1
        turn = False
        Win_check()

    else:
        labelPhoto = Label(screen, image=x_image)
        labelPhoto.grid(row=y, column=z)
        if number == 1:
            control1.set('X')
        elif number == 2:
            control2.set('X')
        elif number == 3:
            control3.set('X')
        elif number == 4:
            control4.set('X')
        elif number == 5:
            control5.set('X')
        elif number == 6:
            control6.set('X')
        elif number == 7:
            control7.set('X')
        elif number == 8:
            control8.set('X')
        else:
            control9.set('X')
        count = count + 1
        turn = True
        Win_check()

# check for the winner
def Win_check():
    global count, turn

    if (control1.get() == 'O' and control2.get() == 'O' and control3.get() == 'O' or
            control4.get() == 'O' and control5.get() == 'O' and control6.get() == 'O' or
            control7.get() == 'O' and control8.get() == 'O' and control9.get() == 'O' or
            control1.get() == 'O' and control4.get() == 'O' and control7.get() == 'O' or
            control2.get() == 'O' and control5.get() == 'O' and control8.get() == 'O' or
            control3.get() == 'O' and control6.get() == 'O' and control9.get() == 'O' or
            control1.get() == 'O' and control5.get() == 'O' and control9.get() == 'O' or
            control3.get() == 'O' and control5.get() == 'O' and control7.get() == 'O'):
        tkinter.messagebox.showinfo('Tic Tac Toe', 'Player O Wins !')
        turn = True
        count = 0
        clear()
        player()

    elif (control1.get() == 'X' and control2.get() == 'X' and control3.get() == 'X' or
          control4.get() == 'X' and control5.get() == 'X' and control6.get() == 'X' or
          control7.get() == 'X' and control8.get() == 'X' and control9.get() == 'X' or
          control1.get() == 'X' and control4.get() == 'X' and control7.get() == 'X' or
          control2.get() == 'X' and control5.get() == 'X' and control8.get() == 'X' or
          control3.get() == 'X' and control6.get() == 'X' and control9.get() == 'X' or
          control1.get() == 'X' and control5.get() == 'X' and control9.get() == 'X' or
          control3.get() == 'X' and control5.get() == 'X' and control7.get() == 'X'):
        tkinter.messagebox.showinfo('Tic Tac Toe', 'Player X Wins !')
        count = 0
        clear()
        player()

    elif (count == 9):
        tkinter.messagebox.showinfo('Tic Tac Toe', 'Its a Draw!')
        turn = True
        count = 0
        clear()
        player()

# this function will clear the text variables
def clear():
    control1.set('')
    control2.set('')
    control3.set('')
    control4.set('')
    control5.set('')
    control6.set('')
    control7.set('')
    control8.set('')
    control9.set('')


player()
# An event handler
screen.mainloop()
