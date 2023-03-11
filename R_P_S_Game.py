import random
l=['Rock','Paper','Scissor']

print('''# Winning Rules as follows:
         Rock vs Paper => Paper wins
         Rock vs Scissor => Rock wins
         Paper vs scissor => Scissor wins ''')

while True:
    Ccount=0
    Ucount=0
    Uchoise=int(input('''
Game Start..
1 Yes
2 No / Exit 

''')) 
    if Uchoise==1:
       for a in range(1,6):
        userInput=int(input(''' 
    1 Rock
    2 Paper
    3 Scissor

        '''))

        if userInput==1:
            Uchoise="Rock"
        elif userInput==2:
            Uchoise="Paper"
        elif userInput==3:
            Uchoise="Scissor"
        Cchoise=random.choice(l)
        
        if Cchoise==Uchoise:
            print("Computer Value",Cchoise)
            print("User Value",Uchoise)
            print("Game Draw")
            Ucount = Ucount + 1
            Ccount = Ccount + 1
        elif (Uchoise=="Rock" and Cchoise=="Scissor") or (Uchoise=="Paper" and Cchoise=="Rock") or (Uchoise=="Scissor" and Cchoise=="Paper"):
            print("Computer Value",Cchoise)
            print("User Value",Uchoise)
            print("You win!")
            Ccount = Ccount + 1
        else:
            print("Computer Value",Cchoise)
            print("User Value",Uchoise)
            print("Computer win!")
            Ccount = Ccount + 1

    if Ucount==Ccount:
        print("Final Game is Draw!")
        print("User Score", Ucount)
        print("Computer Score", Uchoise)
    elif Ucount>Ccount:
        print("You win the Final Game")
        print("User Score", Ucount)
        print("Computer Score", Uchoise)
    else:
        print("Computer win the Final Game")
        print("User Score", Ucount)
        print("Computer Score", Uchoise)
        
    else:
        break
       