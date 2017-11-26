from GUI import play


def choose_difficult(diff):
    choices = {'Easy': 3, 'Normal': 5, 'Hard': 6}
    return choices.get(diff, 'Normal')


def main():
    difficult = choose_difficult("Easy")
    ask_to_restart = ""    
    while(ask_to_restart == ""):
        print("finish?")
        ask_to_restart = play(difficult)
        print(ask_to_restart)
        if ask_to_restart == "N":
            exit()
        elif ask_to_restart == "Y":
            ask_to_restart = ""
main()
