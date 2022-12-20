from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        new_game = Game()
        # exercise
        new_grid = new_game.grid
        # verify
        assert type(new_grid) == list
        assert len(new_grid) == 9
        for letter in new_grid:
            assert letter in string.ascii_uppercase

    def test_empty_word(self):
        game = Game()
        assert game.is_valid('') is False

    def test_word_in_grid(self):
        game = Game()
        game.grid = ["B","A","R","O","Q","U","E","Z","Z"]
        assert game.is_valid("HELLO") is False
        assert game.is_valid("BAROQUE") is True
        assert game.is_valid("BARON") is False
