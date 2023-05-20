import random
def game():
    print("Choose your move: ")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    choices = ['Stone', 'Paper', 'Scissors']
    while True:
        player_choice = input("Enter your choice (1-3): ")
        if player_choice in ['1', '2', '3']:
            break
        print("Invalid choice. Please enter a number between 1 and 3.")
    player_choice = choices[int(player_choice) - 1]
    computer_choice = random.choice(choices)
    print("You chose:", player_choice)
    print("Computer choce:", computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == 'Stone' and computer_choice == 'Scissors') or
        (player_choice == 'Paper' and computer_choice == 'Stone') or
        (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        print("Congratulations! You win!")
    else:
        print("Oops! Computer wins.")
game()