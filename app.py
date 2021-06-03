import constants
import copy
import sys

players_copy = copy.deepcopy(constants.PLAYERS)
team_copy = copy.deepcopy(constants.TEAMS)
experienced = []
non_experienced = []
panthers = []
bandits = []
warriors = []


def clean_data():
    for players in players_copy:
        height = players['height'].split()
        players['height'] = int(height[0])
        if players['experience'] == 'YES':
            players['experience'] = True
            experienced.append(players)
        elif players['experience'] == 'NO':
            players['experience'] = False
            non_experienced.append(players)
    return non_experienced, experienced


def balanced_teams():
    exp_players_per_team = int(len(experienced) / len(team_copy))
    non_exp_players_per_team = int(len(non_experienced) / len(team_copy))
    all_players = exp_players_per_team + non_exp_players_per_team
    for player in experienced:
        if len(panthers) < exp_players_per_team:
            panthers.append(player)
        elif len(bandits) < exp_players_per_team:
            bandits.append(player)
        elif len(warriors) < exp_players_per_team:
            warriors.append(player)
    for player in non_experienced:
        if len(panthers) < all_players:
            panthers.append(player)
        elif len(bandits) < all_players:
            bandits.append(player)
        elif len(warriors) < all_players:
            warriors.append(player)
    return panthers, bandits, warriors


def menu():
    team1 = "Panthers Stats"
    team2 = "Bandits Stats"
    team3 = "Warriors Stats"
    print("Basketball Team Stat Tool")
    print("\n")
    print("--- MENU ---")
    print("\n")
    print("Here are your choices: ")
    print("""
    A) Display Team Stats
    B) Quit""")
    print("\n")
    choice1 = input("Enter an option: ")
    print("\n")
    while True:
        try:
            if choice1.upper() == "A":
                print("A) Panthers")
                print("B) Bandits")
                print("C) Warriors")
                print("\n")
                break
            elif choice1.upper() == "B":
                print("Goodbye")
                sys.exit()
            raise ValueError
        except ValueError:
            print("oops..not a valid choice")
            return menu()
    while True:
        try:
            choice2 = input("Enter an option: ")
            if choice2.upper() == "A":
                print(f"Team: {team1}")
                print("--------------------")
                team_stats(panthers)
                break
            elif choice2.upper() == "B":
                print(f"Team: {team2}")
                print("--------------------")
                team_stats(bandits)
                break
            elif choice2.upper() == "C":
                print(f"Team: {team3}")
                print("--------------------")
                team_stats(warriors)
                break
            raise ValueError
        except ValueError:
            print("oops..not a valid choice")
        return menu()


def team_stats(teams):
    print(F"Total players: {int(len(constants.PLAYERS) / len(constants.TEAMS))}")
    names = [player["name"] for player in teams]
    print("\nNames of Players:")
    print(", ".join(names))
    print("\n")
    choice3 = str(input("Would you like to start again y/n: "))
    if choice3.casefold() == "y":
        menu()
    elif choice3.casefold() == "n":
        print("Goodbye")
    else:
        print("Goodbye")
        sys.exit()


if __name__ == "__main__":
    clean_data()
    balanced_teams()
    menu()
