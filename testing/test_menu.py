import unittest
import menu
import mock


class TestMenu(unittest.TestCase):

    def test_opening_menu(self):
        with mock.patch('builtins.input', return_value="1"):
            assert menu.opening_menu() == 1

        with mock.patch('builtins.input', return_value="2"):
            assert menu.opening_menu() == 2

    def test_fight_menu(self):
        with mock.patch('builtins.input', return_value=1):
            assert menu.fight_menu() == 1

        with mock.patch('builtins.input', return_value=2):
            assert menu.fight_menu() == 2

    def test_spell_menu(self):
        with mock.patch('builtins.input', return_value=1):
            assert menu.fight_menu() == 1

        with mock.patch('builtins.input', return_value=2):
            assert menu.fight_menu() == 2

        with mock.patch('builtins.input', return_value=3):
            assert menu.fight_menu() == 3

    if __name__ == '__main__':
        unittest.main()
