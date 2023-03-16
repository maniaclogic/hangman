from core import blanks_for_word, guess_a_letter


def main():
    game_over = False
    word = "test"
    puzzle = blanks_for_word(word)
    print(' '.join(puzzle))
    while not game_over:

        player_guess = input("Guess a letter: ")
        success_message, remaining_puzzle = guess_a_letter(player_guess, word, puzzle)

        if success_message:
            print("Correct!")
            print(' '.join(remaining_puzzle))
        else:
            print("Ascii art intensifies ...")
            print(' '.join(remaining_puzzle))


main()
