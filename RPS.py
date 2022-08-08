import random

play_options = ["Rock", "Paper", "Scissors"]

user_name = input("Enter your name: ")
user_action = input("Enter a choice (Rock, Paper, Scissors): ")

computer_choice = random.choice(play_options)

print(f"\n{user_name} chose {user_action}, computer chose {computer_choice}.\n")

# Tie situation
if user_action == computer_choice:
  print("It's a tie!")

# User chooses Rock

elif user_action == "Rock":
  if computer_choice == "Paper":
    print("Paper covers Rock -- Computer wins!")
  if computer_choice == "Scissors":
    print(f"Rock smashes Scissors -- {user_name} wins!")

# User chooses Paper

elif user_action == "Paper":
  if computer_choice == "Rock":
    print(f"Paper covers Rock -- {user_name} wins!")
  if computer_choice == "Scissors":
    print("Scissors cuts Paper -- Computer wins!")

# User chooses Scissors

elif user_action == "Scissors":
  if computer_choice == "Rock":
    print(f"Rock smashes Scissors -- Computer wins!")
  if computer_choice == "Paper":
    print(f"Scissors cuts Paper -- {user_name} wins!")
