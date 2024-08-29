
from tkinter import *
import random

class NumberGuessing:
    cnt = 0
    rnum = random.randint(1, 100)

    def gen(self):
        self.rnum = random.randint(1, 100)
        self.cnt = 0

    def display(self):
        cnt = self.cnt
        rnum = self.rnum

        try:
            inpt = int(entry.get())
            if inpt > 100:
                cont.configure(text = 'input number must be less than 100.', foreground = 'red')
                entry.delete(0, END) 
            elif inpt < 0:
                cont.configure(text = 'input number must be a positive number.', foreground = 'red')
                entry.delete(0, END)
            else:
                cnt += 1
                if rnum == inpt:
                    string = 'You guessed the number in '
                    string = string + str(cnt) + ' attempts'
                    cont.configure(text=string, foreground = 'green')
                elif rnum > inpt:
                    string = 'Higher number please! ('
                    string = string + str(10 - cnt) + ' attempts left)'
                    cont.configure(text=string, foreground = 'orange')
                    entry.delete(0, END)  
                else:
                    string = 'Lower number please! ('
                    string = string + str(10 - cnt) + ' attempts left)'
                    cont.configure(text=string, foreground = 'orange')
                    entry.delete(0, END)   
            self.cnt = cnt

        except ValueError:
            cont.configure(text = 'please enter a valid input.', foreground = 'red')
            entry.delete(0, END)
            
        if cnt > 10:
            cont.configure(text='Game Over! The number was ' + str(rnum), foreground = 'red')

    def reset(self):
        self.rnum = random.randint(1, 100)
        entry.delete(0, END)
        cont.configure(text = '')
        self.cnt = 0



root = Tk()
root.title('Number Guessing Game')
root.minsize(700,500)
root.configure(bg = 'white')

#creating NumberGuessing class Object.
guess = NumberGuessing()

#calling gen method 
guess.gen()

label = Label(root, text = 'Guess a number between 1 and 100', bg = 'white', font = ('times new rome', 18, 'bold'))
label.place(x = 135, y = 75)

cont = Label(root, text = '', bg = 'white', font = ('times new rome', 16, 'bold'))
cont.place(x = 100, y = 150)

entry = Entry(root, font = ('times new rome', 16, 'bold'))
entry.place(x = 200, y = 250)

button = Button(root, text = 'enter', command = guess.display, width = 10, bg = 'white', activebackground = 'green', activeforeground = 'white', font = ('times new rome', 16, 'bold'))
button.place(x = 250, y = 300)

reset = Button(root, text = 'reset', command = guess.reset, width = 10, bg = 'white', activebackground = 'green', activeforeground = 'white', font = ('times new rome', 16, 'bold'))
reset.place(x = 250, y = 350)

root.mainloop()