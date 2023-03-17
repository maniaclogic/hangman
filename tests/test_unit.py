from game.core import *


def test_should_display_underscores_in_the_correct_amount():
    assert blanks_for_word("mouse") == ["_", "_", "_", "_", "_"]
    assert blanks_for_word("dog") == ["_", "_", "_"]
    assert blanks_for_word("chicken") != ["_", "_", "_"]


def test_should_evaluate_if_letter_is_part_of_word_and_return_remaining_puzzle():
    # Happy Path
    is_part_of_word, remaining_puzzle = guess_a_letter('a', "cat", ["_", "_", "_"])
    assert is_part_of_word is True
    assert remaining_puzzle == ["_", "a", "_"]
    # Sad Path
    is_not_part_of_word, remaining_puzzle_2 = guess_a_letter('a', "cut", ["_", "_", "_"])
    assert is_not_part_of_word is False
    assert remaining_puzzle_2 == ["_", "_", "_"]
    # Edge Case
    occurs_twice_in_word, remaining_puzzle_3 = guess_a_letter('t', "test", ["_", "_", "_", "_"])
    assert occurs_twice_in_word is True
    assert remaining_puzzle_3 == ["t", "_", "_", "t"]


def test_should_return_true_when_game_is_won():
    assert won(["c", "a", "t"], "Cat")
    assert not won(["j", "_"], "Ja")


def test_should_return_true_when_game_is_lost():
    assert lost(7, "answer")
    assert not lost(3, "solution")
