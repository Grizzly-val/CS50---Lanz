def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
#   the 'if not' in line 3 basically tells line 4 to print this IF NOT. But if the user inputs the expected inputs, line 4 will be skipped.

    players = input("Multiplayer or Single-player? ")
    if not(players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return
    
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("you might like,", game)

main()