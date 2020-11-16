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


    def testTwoPair(self):
        hand = ['TS', '9H', 'JS', '6D', 'TD', '6S', 'JD']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.TWO_PAIRS)
        self.assertEqual([11, 11, 10, 10, 9], score.HAND)


    def testTwoPair2(self):
        hand = ['AS', '4H', '9C', 'AD', '9S', '4S', '2H']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.TWO_PAIRS)
        self.assertEqual([14, 14, 9, 9, 4], score.HAND)


    def testTwoPair3(self):
        hand = ['5S', '6D', 'KD', 'TH', 'AS', '6C', '5D']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.TWO_PAIRS)
        self.assertEqual([6, 6, 5, 5, 14], score.HAND)


    def testPair(self):
        hand = ['JS', '8S', '6C', '9C', 'JD', '4S', 'AD']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.PAIR)
        self.assertEqual([11, 11, 14, 9, 8], score.HAND)


    def testFullHouse(self):
        hand = ['QD', '8S', '8H', 'KH', 'KC', 'QH', 'KS']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.FULL_HOUSE)
        self.assertEqual([13, 13, 13, 12, 12], score.HAND)


    def testAceLowStraight(self):
        hand = ['3S', '5H', '2C', 'AH', 'AD', 'TS', '4H']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual([5, 4, 3, 2, 14], score.HAND)


    def testFlush2(self):
        hand = ['5C', 'QH', '4C', '6H', '9H', '8H', '2H']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual([12, 9, 8, 6, 2], score.HAND)


    def testFlush3(self):
        hand = ['8H', 'AC', 'QH', 'JH', 'TH', '9S', '4H']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual([12, 11, 10, 8, 4], score.HAND)


    def testStraight2(self):
        hand = ['7S', 'AH', '8H', 'QD', 'JC', 'TS', '9H']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual([12, 11, 10, 9, 8], score.HAND)


    def testAceLowStraight2(self):
        hand = ['2S', '5D', 'AH', '4D', 'JS', '3H', 'QD']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual([5, 4, 3, 2, 14], score.HAND)


    def testStraight3(self):
        hand = ['5C', 'QH', '6C', '3C', 'KS', '7D', '4S']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual([7, 6, 5, 4, 3], score.HAND)


    def testHighCard(self):
        hand = ['JH', 'TC', '5C', 'AD', '6D', '4C', 'QS']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.HIGH_CARD)
        self.assertEqual([14, 12, 11, 10, 6], score.HAND)


    def testFullHouse(self):
        hand = ['4C', '2H', '4S', '2D', 'KS', '2S', '4H']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.FULL_HOUSE)
        self.assertEqual([4, 4, 4, 2, 2], score.HAND)


    def testStraight4(self):
        hand = ['6D', 'TH', 'AS', '5S', '3D', '4C', '2S']
        pips = [i for i, j in hand]
        suits = [j for i, j in hand]
        score = best_hands(*pips, *suits)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual([6, 5, 4, 3, 2], score.HAND)


if __name__ == '__main__':
    unittest.main()
