import random
# there needs to be a menu
# there needs to be a function with a while loop for each round
# we will need access to a dictionary where we can pull words from


def play_mode(play, lives, difficulty_input):
    # initialisation
    guesses = 0
    unfinished_answer = []
    guesslist = []
    # draw a word from a text file
    with open('words.txt') as word_file:
        words = word_file.readline()
        word_list = words.split(',')
        rand_index = random.randint(0, len(word_list) - 1)
        answer = word_list[rand_index]
        for letters in answer: unfinished_answer.append('_')
    while play is True and lives >= 1:
        guess = input("Please enter a single alphabetical character or a complete answer")
        guesses += 1
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
                lives -= 1
                print("That is incorrect")
            # test mode answer output
            if difficulty_input == "test": print('test result = ' + answer)
        # single letter guesses
        else:
            if guess in answer:
                # test difficulty output
                if difficulty_input == 'test':
                    print(answer)
                for indices in range(len(answer)):
                    if guess == answer[indices]:
                        unfinished_answer[indices] = guess
                # this will add the guess to the unfinished answer
                unfinished_answer[answer.index(guess)] = guess
                print(unfinished_answer)

            else:
                if difficulty_input == "test":
                    print(answer)
                lives -= 1
                print("you are incorrect")
                print("you have " + str(lives) + " remaining")
                guesslist.append(guess)
                print(guesslist)
                print(unfinished_answer)
        if lives == 0:
            print("You have run out of lives, you lose")
            print('guesses: ' + guesses)
            print('your guesses: ' + guesslist)
            print('answer: ' + answer)

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
                difficulty = ['easy', 'medium', 'hard', 'test']
                lives_options = [10, 6, 3, 10]
                # add a lives choice here later
                dif_menu_done = False
                while dif_menu_done is False:
                    # maybe use a list instead of a cascade
                    difficulty_input = input("what difficulty would you like to play on? easy, medium, hard or test?")
                    if difficulty_input in difficulty:
                        lives = lives_options[difficulty.index(difficulty_input)]
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