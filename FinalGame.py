import tkinter as tk
import random

'''
Author: Ben Lehmann
Project: Rock Paper Scissors
- We have multiple methods
    - computer_selection(self): this will return a random value, from the list of rock, paper, scissors
    - def test(self,input): this will return whether you have beaten the computer or have tied, we will take the input button being the input

Date Modified: 12/02/20 -- 12/14/20 (Modifications with buttons and making sure it can reset or can keep running)

'''

class Game:
    def __init__(self,Master):
        new_frame = tk.Frame(Master)
        new_frame.pack()
        self.winner = tk.Label(window, text="Start the Game")
        self.winner.pack()

        self.options = [('rock', 0), ('paper', 1), ('scissors', 2)]  #Create a list, with tuples, each with a score, rock is 0, paper is 1, scissors is 2
        self.rock = tk.Button(new_frame, text='Rock', command=lambda: self.test(self.options[0]))
        self.rock.grid(row=1, column=1)

        self.paper = tk.Button(new_frame, text='Paper', command=lambda: self.test(self.options[1]))
        self.paper.grid(row=1, column=2)

        self.scissors = tk.Button(new_frame, text='Scissors', command=lambda: self.test(self.options[2]))
        self.scissors.grid(row=1, column=3)

        self.user_display = tk.Label(new_frame, text="You Selected ")
        self.user_display.grid(row=3, column=1)

        self.computer_display = tk.Label(new_frame, text="The Computer Selects: ")
        self.computer_display.grid(row=4, column=1)

    def computer_selection(self):
        self.computer_choice = random.choice(self.options)
        try:
            return self.computer_choice
        except:
            return "Error"

    def test(self,input):
        computer_select = self.computer_selection()
        self.user_display.config(text="You Chose: " + input[0])
        self.computer_display.config(text="The Computer Chose: " + computer_select[0])
        if (input == computer_select):
            self.winner.config(text="It's a Tie")
            print("Tie")
        elif ((input[1] - computer_select[1]) % 3 == 1):
            print("You Won")
            self.winner.config(text="You are the winner")
        else:
            print("The Computer Won")
            self.winner.config(text="The Computer is the Winner")
window = tk.Tk()
window.geometry('400x400')
window.title('Rock,Paper,Scissors')
window.configure(background='blue')
b = Game(window)
window.mainloop()







