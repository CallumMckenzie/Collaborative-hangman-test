import random
# there needs to be a menu
# there needs to be a function with a while loop for each round
# we will need access to a dictionary where we can pull words from

def Play_mode(play, difficulty):
    # initialisation
    guesses = 0
    lives_options = [10, 6, 3, 10]
    lives = lives_options[difficulty]
    unfinished_answer = []
    # draw a word from a text file
    with open('words.txt') as word_file:
        words = word_file.readline()
        word_list = words.split(',')
        rand_index = random.randint(0, len(word_list) - 1)
        answer = word_list[rand_index]
        for letters in answer: unfinished_answer.append('_')
    while play is True and lives >= 1:
        guess = input("Please enter a single alphabetical character")
        if guess.isalpha() is False:
            print("Error, you must enter a alphabetical character")
        # this handles full word guesses
        elif len(guess) > 1:
            if guess == answer:
                print('You guessed the correct word, you win! \n your stats are lives = ' + str(lives) + ',\
                 guesses = ' + str(guesses))
            else:
                guesses += 1
                lives -= 1
                print("That is incorrect")
            if difficulty == 'test': print(answer)
        else:
            if guess in answer:
                for indicies in range (len(answer)):
                    if guess == letters:

                #this will add the guess to the unfinished answer
                unfinished_answer[answer.index(guess)] = guess
                print(unfinished_answer)
            else:
                guesses += 1
                lives -= 1
# test comment
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
                    # maybe use a list instead of a cascade
                    difficulty_check = input("what difficulty would you like to play on? easy, medium, hard or test?")
                    if difficulty_check == "easy":
                        difficulty = 0
                        dif_menu_done = True
                    elif difficulty_check == "medium":
                        difficulty = 1
                        dif_menu_done = True
                    elif difficulty_check == "hard":
                        difficulty = 2
                        dif_menu_done = True
                    elif difficulty_check == "test":
                        difficulty = 3
                        dif_menu_done = True
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