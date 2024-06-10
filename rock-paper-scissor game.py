import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']
    while True:
        print("\nRock, Paper, Scissors Game")
        print("Choose your move: rock, paper, or scisssors")
        user_choice = input("Your choice: ").lower()
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, scissors.")
        computer_choice = random.choice(choices)
        print("Computer's choice:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print("Score - You:", user_score, "Computer:", computer_score)
        play_again = input("Do you want to play again? (yes\no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()                     