# Name: Farhana Lima
# Purpose: Assignment on number guessing game version 2.
# New properties to be fulfilled:
# Ask the player for their name prior to playing the game
# After each game:
# Update a file called topPlayers.txt with the results of the game
# Only save the top five players and scores
# Display the updated top 5 players from the topPlayers.txt file
# Allow the player to play again without having to rerun the program
# Use the topPlayers.txt Download topPlayers.txtfile as a starting file
# If you opt to use functions, move those functions into a single library file
# Anticipate exceptions and catch them (i.e., fail nicely)
# The game should feel like a nice game to play
# Make it easy for the player to play the game
# Do not make the player do a bunch of extra stuff to play

# As we need to choose a random number, I am importing the random library
import random
# This is for importing the function from the library.
from playerLibrary import updateTopPlayers, displayTopPlayers

# Now I'm going to define a function for my number guessing game.
# The attempts function will keep the track of the players attempt.
def numberGuessingGame():
    secretNumber = random.randint(1, 100)
    attempts = 0

    # Here I am going to print greetings, and some rules for the player.
    # For the header trying to follow pet chooser solution code.
    print("*".center(36, "*"))
    print(" Number Guessing Game Version-2 ".center(36, "*"))
    print("*".center(36, "*"))
    # Blank line.
    print()
    # Give the Player an option to add name.
    playerName = input("Enter your name: ")
    print(f"Welcome, {playerName}!")
    print()
    print(f"Rules: It's a simple game, just 2 things for you:")
    print(f"1. Choose a number from 1 to 100,")
    print(f"2. You can quit any time by typing 'Q'.")
    print()

    # Using while as an infinite loop, will continue until the player wants.
    # using try-except block for handling the exception that may occur.
    while True:
            try:
                playerInput = input("Guess the number: ")
                # This code is for quit the game anytime, when the player wants.
                # If the player input 'q' it will break the loop, and end the game.
                if playerInput.lower() == "q":
                  print(f"Thanks for playing. The correct number was {secretNumber}.")
                  break
                # If the player didn't quit, the code will convert the input into an integer.
                playerGuess = int(playerInput)

                # When player choose any number out of the range, will get this massage.
                # With 'continue' the player is prompted to make another guess.
                if playerGuess < 1 or playerGuess > 100:
                  print(f"Please enter a number within the range of 1 to 100.")
                  continue
                # It incremented by 1 with each guess.
                attempts += 1
                # This code is for checking whether the player's guess is low or high
                # As the player guess the correct number it will break the code by 'break"
                if playerGuess < secretNumber:
                   print(f"Wrong guess! Try a higher number.")
                elif playerGuess > secretNumber:
                   print(f"Wrong guess! Try a lower number.")
                else:
                   print(f"Great! You guessed the correct number {secretNumber} in {attempts} attempts.")
                   updateTopPlayers(playerName, attempts)
                   displayTopPlayers()
                   break
                # Checking the difference to give a clue for  the player.
                difference = (playerGuess - secretNumber)
                clue = abs(difference)
                if clue <= 5:
                    print(f"Clue: You're getting closer!")
            # This is for exception.
            except ValueError:
                print(f"Please enter a valid number.")

# This code allow the script to run directly
# IT ensures that the game is executed only when this script is run directly.
if __name__ == "__main__":
    # This is to give the player an option to play again if he/she wants.
    # Game will continue with this infinite loop until the player choose no.
    while True:
        numberGuessingGame()
        # Option for player. the lower will convert the into lower case.
        play_again = input(f"Do you want to play again? (Y/N): ").lower()
        if play_again != "Y":
            # If player don't input Y, it will print the line and exit the loop.
            print(f"Thank you for playing!")
            break

