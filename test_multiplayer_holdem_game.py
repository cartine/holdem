import unittest
import RunGame
import multiplayer_holdem_game
from PeterPokerBot3 import CPUPlayer3
import game2


class MyTestCase(unittest.TestCase):
    def testPotDistribution(self):
        player1 = CPUPlayer3(10, "Player 1")
        from PeterPokerBot2 import CPUPlayer2
        player2 = CPUPlayer2(10, "Player 2")
        player3 = CPUPlayer3(10, "Player 3")
        player4 = CPUPlayer2(10, "Player 4")
        player5 = CPUPlayer2(10, "Player 5")
        player1.HAND = ['JH', 'KC']
        player1.CHIPS_IN = 10
        player2.HAND = ['JD', 'KH']
        player2.CHIPS_IN = 100
        player3.HAND = ['KS', '9D']
        player3.CHIPS_IN = 1000
        player4.HAND = ['9S', '2D']
        player4.CHIPS_IN = 10000
        player5.HAND = ['9C', '2S']
        player5.CHIPS_IN = 100000
        tebble = game2.Table(player1, player2)
        tebble.SHARED_CARDS_SHOWING = ['KD', '9H', '2H', 'JC', 'JS']
        multiplayer_holdem_game.play_hand([player1, player2, player3, player4, player5], table=tebble, hand_number=7)
        self.assertEqual(player1.CHIPS, 35)
        self.assertEqual(player2.CHIPS, 395)
        self.assertEqual(player3.CHIPS, 2710)
        self.assertEqual(player4.CHIPS, 9010)
        self.assertEqual(player5.CHIPS, 99010)


if __name__ == '__main__':
    unittest.main()
