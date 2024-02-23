import random
while True:
    computer = random.choice(["paper", "rock", "scissors"])
    user_input = input("Choose: paper, rock, or scissors?:\n")
    
    print("Computer's choice is:", computer)

    if computer == user_input:
        print("Draw\n")
    
    elif computer == "rock" and user_input == "paper":
        print("You win\n")
    elif computer == "paper" and user_input == "scissors":
        print("You win\n")
    elif computer == "scissors" and user_input == "rock":
        print("You win\n")
    else:
        print("Computer wins\n")



    
    
  
   
    