# This file is designed to read and write to a file named "topPlayers.txt"
# And to maintain and display the top players' list.

# This function Will update the top player list
# It will be called after the game has been finished.
# If the player choose to quit (quit_game=true) it will not update the list.
def updateTopPlayers(playerName, attempts, quit_game=False):
    if quit_game:
        return
    # This bunch of code fore txt file reminds me the sorting file assignment.
    # Followed the code from that one. as i'm so naive in programming, and that code worked, so..
    try:
        # Now opening the "topPlayers.txt" file in read mode with r.
        with open("topPlayers.txt", "r") as file:
            # This will read the file line by line and split each line into a list of strings
            players = [line.strip().split() for line in file.readlines()]
        # This will append the new player and the attempts in the file
        players.append([str(attempts), playerName])
        # Sorting the players list based on the number of attempts in ascending order
        players.sort(key=lambda x: int(x[0]))
        # This will keep only keep 5 player In the list.
        top_players = players[:5]

        # Now opening the "topPlayers.txt" file in writing mode.
        with open("topPlayers.txt", "w") as file:
            # This will write the updated list back to the file.
            for player in top_players:
                file.write(f"{player[0]} {player[1]}\n")
    except FileNotFoundError:
        # If the file is not found, it will create one and keep the record.
        with open("topPlayers.txt", "w") as file:
            file.write(f"{attempts} {playerName}\n")

# This is to display the list of top 5 players on the screen.
def displayTopPlayers():
    try:
        # Opening the updated "topPlayers.txt" file in read mode
        with open("topPlayers.txt", "r") as file:
            # This will read the file line by line and split each line into a list of strings
            players = [line.strip().split() for line in file.readlines()]
        # It will check the player list, and if there is players than it will print the list.
        if not players:
            print(f"There is no top players. Play the game and you will be there!")
        else:
            print(f"Top Players:")
            for i, player in enumerate(players):
                score, name = player
                print(f"{i + 1}. {name} : {score} attempts.")

    # If there is no example file or no file created for top players list.
    except FileNotFoundError:
        print(f"There is no file to display!!")
    # If the file is empty or when there's an issue reading it
    except EOFError:
        print("An error occurred while reading the top players file.")
