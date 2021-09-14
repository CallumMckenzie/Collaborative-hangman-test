
# there needs to be a menu
# there needs to be a function with a while loop for each round
# we will need access to a dictionary where we can pull words from

def Play_mode(play):
    while play is True and lives >= 1:
        guess = input("Please enter a single alphabetical character")
        if guess.alpha() is False:
            print("Error, you must enter a alphabetical character")
            continue
        elif guess.len() > 1:
            print("Error, you must add either y or n only")

def menu():
    """ This function will allow the user to decide if they want to
        play or not as well as how many lives they will have"""
    menu_active = True
    while menu_active is True:
        print("Welcome to hangman, a game by ben and callum")
        menu_choice = input("Would you like to play a round? y/n")
        if menu_choice.isalpha() is True:
            if menu_choice.lower() == "y":
                # add a lives choice here later
                play = True
                Play_mode(play)
                menu_active = False
            elif menu_choice.lower() == "n":
                exit(1) # successful exit code
            else:
                print("please enter either \"y\" or \"n\"")