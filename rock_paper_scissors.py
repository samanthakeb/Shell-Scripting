import random

choices = ['rock', 'paper', 'scissors']

def lets_play():
    user_choice = input("Enter your choice: (rock/paper/scissors)  ").lower()
    if user_choice not in choices:
        print("Please choose rock, paper, or scissors.")
        return user_choice

    computer_choice = random.choice(choices)
    print(f"Your opponent chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You Win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    lets_play()
