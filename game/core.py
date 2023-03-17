from urllib.request import urlopen
import json


def get_word():
    url = "https://random-word-api.herokuapp.com/word"
    word = json.loads(urlopen(url).read())
    return word[0]


def blanks_for_word(hidden_word):
    return ["_" for i in range(len(hidden_word))]


def guess_a_letter(letter, word, puzzle):
    letter_occurrences = [index for index, char_in_word in enumerate(word) if char_in_word == letter]
    if len(letter_occurrences) > 0:
        for occurrence in letter_occurrences:
            puzzle[occurrence] = letter
        return True, puzzle
    else:
        return False, puzzle


def won(puzzle, word, failures):
    if "_" not in puzzle:
        print("\n################################")
        print("#  🎉 You got it. Congrats! 🎉  #")
        print("################################\n")
        print("The word was: ", word.title())
        print(f'Solved with {failures}/7 wrong guesses.')
        return True
    else:
        return False


def lost(failures, word):
    if failures >= 7:
        print("\n###################")
        print("#    GAME OVER    #")
        print("###################\n")
        print("The word was: ", word.title())
        return True
    else:
        return False
