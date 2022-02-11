import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    
    def setUp(self):
        self.ace = Card("Ace", 1)
        self.king = Card("King", 13)
        self.card_game = CardGame([self.king, self.ace])


    def test_check_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.king))
    
    def test_check_for_ace_True(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.ace))

    def test_check_highest_card_card1(self):
        self.assertEqual(self.king, self.card_game.highest_card(self.king, self.ace))
    
    def test_check_highest_card_card2(self):
        self.assertEqual(self.king, self.card_game.highest_card(self.ace, self.king))

    def test_check_cards_total(self):
        self.assertEqual("You have a total of 14", self.card_game.cards_total(self.card_game.cards))