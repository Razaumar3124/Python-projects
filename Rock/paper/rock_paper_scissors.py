import random

user_wins = 0
computer_wins = 0
both_tie = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_input = random.randint(0,2)          #here it will generate random number between 0,1,2 for 0 = rock , 1 = paper , 2 = scissors
    computer_pick = options[random_input]              #here we are doing indexing using randon value
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("Its a tie")
        both_tie += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Its a tie")
        both_tie += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Its a tie")
        both_tie += 1

    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print(f"both tie {both_tie} times.")
print("Goodbye!")