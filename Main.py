from GUI import play


def choose_difficult(diff):
    choices = {'Easy': 2, 'Normal': 4, 'Hard': 6}
    return choices.get(diff, 'Normal')


def main():
    end_game = False
    difficult = choose_difficult("Easy")
    while (not end_game):
        play(difficult)
        ask_to_restart = input("Restart? Y/N")
        if ask_to_restart == "N":
            end_game = True
        elif ask_to_restart == "Y":
            end_game = False
        else:
            ask_to_restart = ""
            while (ask_to_restart != "Y" or ask_to_restart != "N"):
                ask_to_restart = input("Restart? Y/N")


main()
