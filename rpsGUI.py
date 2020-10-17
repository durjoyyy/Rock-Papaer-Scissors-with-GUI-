import random
from tkinter import *

#Dictionary and variables
dict_out={
     "rock":{"rock":1,"paper":0,"scissors":2},
     "paper":{"rock":2,"paper":1,"scissors":0},
     "scissors":{"rock":0,"paper":2,"scissors":1},
}
comp_score=0
player_score=0

#Functions
'''def converted_outcome(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"
'''
def outcome_handler(user_choice):
     global comp_score
     global player_score
     options=["rock","paper","scissors"]
     rand_num=random.randint(0,2)
     computer_choice=options[rand_num]
     result=dict_out[user_choice][computer_choice]

     player_choice_label.config(fg="blue",text="Player Choice : "+str(user_choice))
     computer_choice_label.config(fg="red",text="Computer Choice : "+str(computer_choice))

     if result==2:
          player_score=player_score+1
          player_score_label.config(text="Player : "+str(player_score))
          outcome_label.config(fg="green",text="Outcome : Player Won")
     elif result==1:
          player_score=player_score+0
          computer_score=comp_score+0
          player_score_label.config(text="Player : "+str(player_score))
          computer_score_label.config(text="Player : "+str(comp_score))
          outcome_label.config(fg="green",text="Outcome : Draw")
     elif result ==0:
          comp_score=comp_score+1
          computer_score_label.config(text="Player : "+str(comp_score))
          outcome_label.config(fg="green",text="Outcome : Computrt Won")





#Screen
master =Tk()
master.title("Rock-Paper-Scissors")
#Labels
Label(master, text="Rock,Paper,Scissors", font=("Calibri",40)).grid(row=0,sticky=N, pady=15,padx=200)
Label(master, text="Select an Option to Play", font=("Calibri",20)).grid(row=1,sticky=N)
player_score_label= Label(master, text="Player: 0", font=("Calibri",15))
player_score_label.grid(row=2,sticky=W)
computer_score_label= Label(master, text="Computer: 0", font=("Calibri",15))
computer_score_label.grid(row=2,sticky=E)
player_choice_label=Label(master, font=("Calibri",15))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label=Label(master, font=("Calibri",15))
computer_choice_label.grid(row=3,sticky=E)
outcome_label=Label(master, font=("Calibri",15))
outcome_label.grid(row=3,sticky=N)
#Buttons
Button(master, text="Rock",width=20,command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(master, text="Paper",width=20,command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,pady=5)
Button(master, text="Scissors",width=20,command=lambda:outcome_handler("scissors")).grid(row=4,sticky=E,padx=5,pady=5)

#Dummy Label
'''Label(master).grid(row=5)'''

master.mainloop()


