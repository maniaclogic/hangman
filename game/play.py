from core import *
from hangman_ascii_art import HANGMAN_STAGES


def main():
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
            game_over = won(remaining_puzzle, word)
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
