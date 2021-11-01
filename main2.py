import random
# there needs to be a menu
# there needs to be a function with a while loop for each round
# we will need access to a dictionary where we can pull words from

def openfile():
    unfinished_answer = []
    with open('words.txt') as word_file:
        word_list = (word_file.readline()).split(',')
        rand_index = random.randint(0, len(word_list) - 1)
        answer = word_list[rand_index]
        for letters in answer:
            unfinished_answer.append('_')
        return unfinished_answer, answer
def play_mode(play, lives, difficulty_input):
    # initialisation
    guesses = 0
    guesslist = []
    # draw a word from a text file
    unfinished_answer, answer = openfile()
    while play is True and lives >= 1:
        guess = input("Please enter a single alphabetical character or a complete answer")
        guesses += 1
        guesslist.append(guess)
        if guess.isalpha() is False:
            print("Error, you must enter a alphabetical character")
        # this handles full word guesses
        elif len(guess) > 1:
            # correct full word guess
            if guess == answer:
                print('You guessed the correct word, you win! \n your stats are \n lives = ' + str(lives) + ',\
                 \n guesses = ' + str(guesses) + '\n The answer was: ' + answer)
                play = False
            # incorrect full word guess
            else:
                guesslist.append(guess)
                lives -= 1
                print("That is incorrect")
            # test mode answer output
            if difficulty_input == "test": print('test result = ' + answer)
        # single letter guesses
        else:
            if guess in answer and guess not in unfinished_answer:
                print(guesslist)
                # test difficulty output
                if difficulty_input == 'test':
                    print(answer)
                for indices in range(len(answer)):
                    if guess == answer[indices]:
                        unfinished_answer[indices] = guess
                        guesslist.append(guess)
                        print("guess list: " + str(guesslist))
                # this will add the guess to the unfinished answer
                unfinished_answer[answer.index(guess)] = guess
                print(unfinished_answer)
            # this needs to check the partially made answer for the guess
            elif guess in unfinished_answer:
                print("you have already guessed that letter")
                lives -= 1
                print("lives: " + str(lives))
                print("guesses: " + str(guesses))
            else:
                if difficulty_input == "test":
                    print(answer)
                lives -= 1
                print("you are incorrect")
                print("you have " + str(lives) + " remaining")
                print(guesslist)
                print(unfinished_answer)
        if lives == 0:
            print("You have run out of lives, you lose")
            print('guesses: ' + str(guesses))
            print('your guesses: ' + str(guesslist))
            print('answer: ' + answer)

# test comment
def menu():
    """ This function will allow the user to decide if they want to
        play or not as well as how many lives they will have"""
    menu_active = True
    while menu_active is True:
        print("Welcome to hangman, a game by ben and callum")
        menu_choice = (input("Would you like to play a round? y/n")).strip()
        if menu_choice.isalpha() is True:
            if menu_choice.lower() == "y":
                difficulties = {'easy': 10, 'medium': 6, 'hard': 3, 'test': 10}
                # add a lives choice here later
                dif_menu_done = False
                while dif_menu_done is False:
                    difficulty_input = input("what difficulty would you like to play on? easy, medium, hard or test?")
                    # this if ensures the user entered a valid difficulty option
                    if difficulty_input in difficulties.keys():
                        # this chooses the number of lives from the lives_options list based
                        # on the index of the entered difficulty of the difficulty list
                        # I should replace both the lists with a single dictionary
                        lives = difficulties[difficulty_input]
                        dif_menu_done = True
                    else:
                        print("Please select one of the available options")
                play = True
                play_mode(play, lives, difficulty_input)
                menu_active = False
            elif menu_choice.lower() == "n":
                exit(1)  # successful exit code
            else:
                print("please enter either \"y\" or \"n\"")

menu()