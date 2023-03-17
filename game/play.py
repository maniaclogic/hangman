from core import blanks_for_word, guess_a_letter, won, lost
from hangman_ascii_art import HANGMAN_STAGES


def main():
    game_over = False
    word = "test"
    puzzle = blanks_for_word(word)
    failures = 0
    print(' '.join(puzzle))
    while not game_over:

        player_guess = input("Guess a letter: ")
        success_message, remaining_puzzle = guess_a_letter(player_guess, word, puzzle)

        if success_message:
            print("Correct!")
            print(' '.join(remaining_puzzle))
            game_over = won(remaining_puzzle)
        else:
            failures += 1
            print("WRONG!")
            print(HANGMAN_STAGES[failures - 1])
            print(' '.join(remaining_puzzle))
            game_over = lost(failures)

        print("\n\n\n")

main()
