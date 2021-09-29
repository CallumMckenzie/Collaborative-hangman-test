
# there needs to be a menu
# there needs to be a function with a while loop for each round
# we will need access to a dictionary where we can pull words from

def Play_mode(play, difficulty):
    lives_options = [10, 6, 3, 10]
    lives = lives_options[difficulty]
    while play is True and lives >= 1:
        guess = input("Please enter a single alphabetical character")
        if guess.isalpha() is False:
            print("Error, you must enter a alphabetical character")
            continue
        elif len(guess) > 1:
            print("Error, you must add either y or n only")
#test comment
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
                dif_menu_done = False
                while dif_menu_done is False:
                    difficulty_check = input("what difficulty would you like to play on? easy, medium, hard or test?")
                    if difficulty_check == "easy":
                        difficulty = 1
                        dif_menu_done = True
                    elif difficulty_check == "medium":
                        difficulty = 1
                        dif_menu_done = True
                    elif difficulty_check == "hard":
                        difficulty = 3
                        dif_menu_done = True
                    elif difficulty_check == "test":
                        difficulty = 4
                    else:
                        print("Please select one of the available options")
                play = True
                Play_mode(play, difficulty)
                menu_active = False
            elif menu_choice.lower() == "n":
                exit(1) # successful exit code
            else:
                print("please enter either \"y\" or \"n\"")

menu()