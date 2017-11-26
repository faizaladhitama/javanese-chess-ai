from GUI import play


def main():
    ask_to_restart = ""
    has_play = 0
    difficult = None
    while (ask_to_restart == ""):
        print("finish?")
        print(has_play)
        if (difficult == None):
            ask_to_restart, difficult = play(has_play)
            has_play += 1
            print(ask_to_restart)
        else:
            ask_to_restart, difficult = play(has_play, difficult)
            has_play += 1
            print(ask_to_restart)
        if (ask_to_restart == "N"):
            ask_to_restart = ""
            has_play = 0
        elif (ask_to_restart == "Y"):
            print("Y")
            ask_to_restart = ""
            has_play += 1


main()
