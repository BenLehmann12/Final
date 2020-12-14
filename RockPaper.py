import tkinter as tk
from datetime import datetime
import random


window = tk.Tk()
window.configure(background='blue')

user_score = 0
computer_score = 0
user = input("Press rock,paper or scissors")
computer = ""

def choices(choice):   #Take user written input
    decisions = {"rock":0,"paper":1,"scissors":2}
        try:
        return decisions[choice]
    except:
        return "Choice is invalid"

def computer():
    comp = random.choice(["rock","paper","scissors"])
    return comp

def test(user,computer):
    global user_score
    global computer_score
    user = choices(user)
    computer = choices(computer)
    if(user == computer):
        print("Tie")
        winner.config(text="Tie!")
    elif((user-computer) % 3 ==1):
        print("You Win")
        winner.config(text="You are the Winner")
        user_score+=1
    else:
        print("Computer Wins")
        winner.config(text="You Lost and the Computer Wins")
        computer_score+= 1

def Rock():
    global user
    global computer
    user = "rock"
    computer = computer()
    test(user,computer)

def Paper():
    global user
    global computer
    user = "paper"
    computer = computer()
    test(user,computer)

def Scissors():
    global user
    global computer
    user = "scissors"
    computer = computer()
    test(user,computer)

winner = tk.Label(text='Let us Play')
winner.grid(column=1,row=1)


date = datetime.now()
date_format = f"{date:%m\%d\%Y}"
w = tk.Label(window,text="Date: " + date_format)
w.grid(column=10,row=10)

rock_button = tk.Button(text= " Rock ",command=Rock)
rock_button.grid(column=4, row=1)
paper_button = tk.Button(text= " Paper ", command=Paper)
paper_button.grid(column=4, row=2)
scissor_button = tk.Button(text= " Scissors ", command=Scissors)
scissor_button.grid(column=4, row=5)
window.mainloop()
#if __name__ == "__main__":
    #print(test('rock','paper'))

