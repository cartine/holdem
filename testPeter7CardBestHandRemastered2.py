import unittest
from Peter7CardBestHandRemastered2 import *


class TestPeterBestHand(unittest.TestCase):

    def testStraight(self):
        score = best_hands(7, 3, 9, 6, 8, 5, 'T', 'S', 'S', 'D', 'S', 'C', 'H', 'H')
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual([10, 9, 8, 7, 6], score.HAND)


    def testPair(self):
        score = best_hands('T', 'A', 'Q', 'A', 8, 6, 7, 'H', 'H', 'D', 'C', 'S', 'H', 'C')
        self.assertEqual(score.RANKING, Ranking.PAIR)
        self.assertEqual([14, 14, 12, 10, 8], score.HAND)

    def testFlush(self):
        hand = ['5H', '3H', 'JH', 'KH', '2C', 'AH', '8C']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual([14, 13, 11, 5, 3], score.HAND)


if __name__ == '__main__':
    unittest.main()
