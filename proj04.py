#!/usr/bin/python3
''' Insert heading comments here.'''

# from random import randint  # the real Python random
from cse231_random import randint  # the cse231 test random for Mimir testing


def display_game_rules():
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your poin\
t." 
          The player loses by rolling a 7 before making the point.''')


def get_bank_balance():
    '''Insert docstring here.'''
    balance = int(input("Enter an initial bank balance (dollars): "))
    return balance


def add_to_bank_balance(balance):
    '''Insert docstring here.'''
    balance += int(input("Enter how many dollars to add to your balance: "))
    return balance


def get_wager_amount():
    '''Insert docstring here.'''
    wager = int(input("Enter a wager (dollars): "))
    return wager


def is_valid_wager_amount(wager, balance):
    '''Insert docstring here.'''
    if wager > balance:
        return False
    else:
        return True


def roll_die():
    '''Insert docstring here.'''
    die = randint(1, 6)
    return die


def calculate_sum_dice(die1_value, die2_value):
    '''Insert docstring here.'''
    return die1_value + die2_value


def first_roll_result(sum_dice):
    '''Insert docstring here.'''
    if (sum_dice == 7 or
            sum_dice == 11):
        return "win"
    elif (sum_dice == 2 or
          sum_dice == 3 or
          sum_dice == 12):
        return "loss"
    else:
        return "point"


def subsequent_roll_result(sum_dice, point_value):
    '''Insert docstring here.'''
    if sum_dice == point_value:
        return "point"
    elif sum_dice == 7:
        return "loss"
    else:
        return "neither"


def main():
    '''Main function'''
    continueAnswer = "yes"
    addAnswer = "no"
    roll = 1

    display_game_rules()
    gameBalance = get_bank_balance()

    while continueAnswer.lower() == "yes":

        if roll == 1:
            gameWager = get_wager_amount()

        while is_valid_wager_amount(gameWager, gameBalance) is False:
            print("Error: wager > balance. Try again.")
            gameWager = get_wager_amount()

        gameDie1 = roll_die()
        gameDie2 = roll_die()

        dieSum = calculate_sum_dice(gameDie1, gameDie2)

        print("Die 1: " + str(gameDie1))
        print("Die 2: " + str(gameDie2))
        print("Dice sum: " + str(dieSum))

        if roll == 1:
            if first_roll_result(dieSum) == "win":
                print("Natural winner.")
                print("You WIN!")
                gameBalance += gameWager
                print("Balance: " + str(gameBalance))
                roll = 1
            elif first_roll_result(dieSum) == "loss":
                print("Craps.")
                print("You lose.")
                gameBalance -= gameWager
                print("Balance: " + str(gameBalance))
                roll = 1
            elif first_roll_result(dieSum) == "point":
                gamePoint = dieSum
                print("*** Point: " + str(gamePoint))
                roll += 1

        if roll == 1:
            continueAnswer = input("Do you want to continue? ")

        if roll == 1 and continueAnswer != "no":
            addAnswer = input("Do you want to add to your balance? ")

        if addAnswer.lower() == "yes":
            gameBalance = add_to_bank_balance(gameBalance)
            print("Balance: " + str(gameBalance))

        if addAnswer == "no" and gameBalance == 0:
            print("You don't have sufficient balance to continue.")
            continueAnswer = "no"

        if first_roll_result(dieSum) == "point":
            gameDie1 = roll_die()
            gameDie2 = roll_die()

            dieSum = calculate_sum_dice(gameDie1, gameDie2)

            print("Die 1: " + str(gameDie1))
            print("Die 2: " + str(gameDie2))
            print("Dice sum: " + str(dieSum))

            if subsequent_roll_result(dieSum, gamePoint) == "point":
                print("You matched your Point.")
                print("You WIN!")
                gameBalance += gameWager
                print("Balance: " + str(gameBalance))
                roll = 1
            elif subsequent_roll_result(dieSum, gamePoint) == "loss":
                print("You lose.")
                gameBalance -= gameWager
                print("Balance: " + str(gameBalance))
                roll = 1

            if roll == 1:
                continueAnswer = input("Do you want to continue? ")

            if roll == 1 and continueAnswer != "no":
                addAnswer = input("Do you want to add to your balance? ")

            if addAnswer.lower() == "yes":
                gameBalance = add_to_bank_balance(gameBalance)
                print("Balance: " + str(gameBalance))

            if addAnswer == "no" and gameBalance == 0:
                print("You don't have sufficient balance to continue.")
                continueAnswer = "no"

    print("Game is over.")


if __name__ == "__main__":
    main()
