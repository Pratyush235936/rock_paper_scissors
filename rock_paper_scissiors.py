def rock_paper_scissors():
   import random
   c = {0: "rock", 1: "paper", 2: "scissors"}
   computer = random.choice([0, 1, 2])
   user = int(input("Enter your choice (0: rock, 1: paper, 2: scissors): "))


   print("you chose:", c[user])
   print("Computer chose:", c[computer])
   if user == computer:
       print("It's a tie!")
   else:
        if(user == 0 and computer ==1):
           print("Computer wins😭!")
        elif(user == 0 and computer == 2):
           print("you win😎!")
        elif(user == 1 and computer == 0):
           print("you win😎!")
        elif(user == 1 and computer == 2):
           print("Computer wins😭!")
        elif(user == 2 and computer == 0):
           print("Computer wins😭!")
        elif(user == 2 and computer == 1):
            print("you win😎!")
rock_paper_scissors()