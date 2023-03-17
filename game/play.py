from core import *
from hangman_ascii_art import HANGMAN_STAGES


def main():
    print('''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
                   \n\n\n''')
    game_over = False
    word = get_word()
    puzzle = blanks_for_word(word)
    failures = 0
    failed_guesses = []
    print(' '.join(puzzle))
    while not game_over:

        player_guess = input("Guess a letter: ")
        success_message, remaining_puzzle = guess_a_letter(player_guess, word, puzzle)

        if success_message:
            print("Correct!")
            print(' '.join(remaining_puzzle))
            game_over = won(remaining_puzzle, word, failures)
        else:
            failures += 1
            failed_guesses.append(player_guess.upper())
            print("WRONG!")
            print(HANGMAN_STAGES[failures - 1])
            print(' '.join(failed_guesses))
            print(' '.join(remaining_puzzle))
            game_over = lost(failures, word)

        print("\n\n")


main()
