# Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2.
         Players alternate turns. Each turn, a player chooses to remove one,
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')


play_str = input("Would you like to play? (0=no, 1=yes) ")


while int(play_str) != 0:

    # Initialize game variables
    pile1 = 5
    pile2 = 5
    turn = True
    cpu_choice = 0
    winsh = 0
    winsc = 0

    print("Start --> Pile 1:", pile1, "   Pile 2:", pile2)

    # Main game loop
    while pile1 + pile2 != 0:

        # Human Turn
        if turn is True and pile1 + pile2 != 0:

            # Choose pile
            pile_choice = int(input("Choose a pile (1 or 2): "))

            # Error checking for empty piles and invalid choices
            while pile_choice == 1 and pile1 == 0:
                print("Pile must be 1 or 2 and non-empty. Please try again.\n")
                pile_choice = int(input("Choose a pile (1 or 2) "))

            while pile_choice == 2 and pile2 == 0:
                print("Pile must be 1 or 2 and non-empty. Please try again.\n")
                pile_choice = int(input("Choose a pile (1 or 2) "))

            while pile_choice not in range(1, 3):
                print("Pile must be 1 or 2 and non-empty. Please try again.\n")
                pile_choice = int(input("Choose a pile (1 or 2) "))

            # Choose number of stones
            stones = int(input("Choose stones to remove from pile: "))

            # Check that pile choice isn't over 3
            while stones not in range(1, 4):
                stones = int(input("Choose stones to remove from pile: "))

            # Choose pile1 and check if it has enough stones
            if pile_choice == 1 and stones <= pile1:
                pile1 -= stones
                print("Player -> Remove", stones, "stones from pile 1")
                print("Pile 1:", pile1, "   Pile 2:", pile2)

            elif pile_choice == 1 and stones > pile1:
                print("Pile 1 is smaller than your choice, pick again:\n")
                while stones <= pile1:
                    stones = int(input("Choose stones to remove from pile: "))

            # Choose pile2 and check if it has enough stones
            if pile_choice == 2 and stones <= pile2:
                pile2 -= stones
                print("Player -> Remove", stones, "stones from pile 2")
                print("Pile 1:", pile1, "   Pile 2:", pile2)

            elif pile_choice == 2 and stones > pile2:
                print("Pile 2 is smaller than your choice, pick again:\n")
                while stones <= pile2:
                    stones = int(input("Choose stones to remove from pile: "))

            # Victory Screech
            if pile1 + pile2 == 0:
                print("\nPlayer wins!\n")
                winsh += 1
                print("Score -> human:", winsh, "; computer:", winsc)

            # Swap Turns
            turn = not(turn)

        # Computer Turn
        if turn is False and (pile1 + pile2 != 0):

            # Choose opposite pile from Human
            if pile_choice == 1:
                cpu_choice = 2

            elif pile_choice == 2:
                cpu_choice = 1

            # Set number of stones to be taken to 1
            stones = 1

            # Remove a stone from Pile 1
            if cpu_choice == 1 and pile1 != 0:
                pile1 -= stones
                print("Computer -> Remove 1 stones from pile 1")
                print("Pile 1:", pile1, "   Pile 2:", pile2)

            elif cpu_choice == 1 and pile1 == 0:
                pile2 -= stones
                print("Computer -> Remove 1 stones from pile 2")
                print("Pile 1:", pile1, "   Pile 2:", pile2)

            # Remove a stone from Pile 2
            if cpu_choice == 2 and pile2 != 0:
                pile2 -= stones
                print("Computer -> Remove 1 stones from pile 2")
                print("Pile 1:", pile1, "   Pile 2:", pile2)

            elif cpu_choice == 2 and pile2 == 0:
                pile1 -= stones
                print("Computer -> Remove 1 stones from pile 1")
                print("Pile 1:", pile1, "   Pile 2:", pile2)

            # Loss message
            if pile1 + pile2 == 0:
                print("\nComputer wins!")
                winsc += 1
                print("Score -> human:", winsh, "; computer:", winsc)

            # Swap Turns
            turn = not(turn)

    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")


else:
    print("\nThanks for playing! See you again soon!")
