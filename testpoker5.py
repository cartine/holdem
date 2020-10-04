import unittest
from poker5 import *


class TestPoker5(unittest.TestCase):

    def test_get_match_ordered_cards(self):
        cards = ('TC', '9D', '9C', '9H', '8C', '3S', '3D')
        match_ordered_cards = get_match_ordered_cards(cards)
        self.assertEqual(match_ordered_cards, ['9D', '9C', '9H', '3S', '3D', 'TC', '8C'])

    def test_getHighest(self):
        cards = ('QS', '9S', 'KS', 'TD', 'TH', '4C', '8C')
        self.assertEqual(get_highest(cards, 0), 'KS')
        self.assertEqual(get_highest(cards, 1), 'KS')
        self.assertEqual(get_highest(cards, 2), 'KS')
        self.assertEqual(get_highest(cards, 3), 'TD')
        self.assertEqual(get_highest(cards, 4), 'TH')
        self.assertEqual(get_highest(cards, 5), '8C')
        self.assertEqual(get_highest(cards, 6), '8C')

    def test_score_highCard(self):
        cards = ('TC', '9D', '3S', '2H', 'AH', '8C', 'KD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.HIGH_CARD)
        self.assertEqual(score.HAND, ['AH', 'KD', 'TC', '9D', '8C'])

    def test_score_pair(self):
        cards = ('QS', '9S', 'KS', 'TD', 'TH', '4C', '8C')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.PAIR)
        self.assertEqual(score.HAND, ['TD', 'TH', 'KS', 'QS', '9S'])

    def test_score_twoPair(self):
        cards = ('QS', '5C', '7D', '7H', '6C', '6H', '5H')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.TWO_PAIRS)
        self.assertEqual(score.HAND, ['7D', '7H', '6C', '6H', 'QS'])

    def test_score_threeOfAKind(self):
        cards = ('6H', 'AC', 'QC', '4S', 'AS', 'AH', '7S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.THREE_OF_A_KIND)
        self.assertEqual(score.HAND, ['AC', 'AS', 'AH', 'QC', '7S'])

    def test_score_straight_noAce(self):
        # 5-card
        cards = ('5D', '6H', '3S', '4D', '2H', '3D', '4S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['6H', '5D', '4D', '3S', '2H'])

        # 6-card
        cards = ('5D', '6H', '9S', '4D', '2H', '3D', '7S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['7S', '6H', '5D', '4D', '3D'])

        # 7-card
        cards = ('5D', '6H', '8S', '4D', '2H', '3D', '7S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['8S', '7S', '6H', '5D', '4D'])

    def test_score_straight_ace_high(self):
        # 5 card
        cards = ('4H', 'AD', 'KD', 'JS', 'TC', 'TH', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JS', 'TC'])

        # 6 card
        cards = ('9H', 'AD', 'KD', 'JS', 'TC', 'TH', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JS', 'TC'])

        # 7 card
        cards = ('9H', 'AD', 'KD', 'JS', '8S', 'TH', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JS', 'TH'])

        # 5 card extra ace
        cards = ('AD', 'KD', 'AH', 'JS', 'TC', 'TH', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JS', 'TC'])

        # 6 card extra ace
        cards = ('9H', 'AD', 'KD', 'JS', 'TC', 'AH', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JS', 'TC'])

    def test_score_straight_ace_low(self):
        # 1 ace
        cards = ('4C', '5C', 'AH', '3D', '7S', '2S', '3H')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['5C', '4C', '3D', '2S', 'AH'])

        # 2 aces
        cards = ('4C', '5C', 'AH', '3D', '7S', '2S', 'AC')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['5C', '4C', '3D', '2S', 'AH'])

        # 3 aces
        cards = ('4C', '5C', 'AH', '3D', 'AS', '2S', 'AC')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT)
        self.assertEqual(score.HAND, ['5C', '4C', '3D', '2S', 'AH'])

    def test_score_flush_6_diamonds(self):
        cards = ('3D', 'AD', '4D', '2D', 'TD', 'JC', '6D')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual(score.HAND, ['AD', 'TD', '6D', '4D', '3D'])

    def test_score_flush_5_hearts(self):
        cards = ('8C', '8H', '9H', 'AD', '7H', 'QH', 'JH')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual(score.HAND, ['QH', 'JH', '9H', '8H', '7H'])

    def test_score_flush_7_clubs(self):
        cards = ('5C', 'JC', '9C', 'QC', '7C', 'AC', '6C')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual(score.HAND, ['AC', 'QC', 'JC', '9C', '7C'])

    def test_score_flush_5_spades(self):
        cards = ('8H', '5S', 'TS', 'JS', '4S', '2H', '8S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual(score.HAND, ['JS', 'TS', '8S', '5S', '4S'])

    def test_score_fullHouse(self):
        cards = ('AD', 'AC', 'TS', '3S', 'TD', 'TC', '7S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FULL_HOUSE)
        self.assertEqual(score.HAND, ['TS', 'TD', 'TC', 'AD', 'AC'])

    def test_score_fourOfAKind(self):
        cards = ('3D', '5D', '8C', '8S', '8D', '8H', '7S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FOUR_OF_A_KIND)
        self.assertEqual(score.HAND, ['8C', '8S', '8D', '8H', '7S'])

        cards = ('5D', 'AC', '3D', 'AS', 'AD', '7S', 'AH')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FOUR_OF_A_KIND)
        self.assertEqual(score.HAND, ['AC', 'AS', 'AD', 'AH', '7S'])

        cards = ('2C', '5D', '3D', '2S', '2D', '7S', '2H')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FOUR_OF_A_KIND)
        self.assertEqual(score.HAND, ['2C', '2S', '2D', '2H', '7S'])

    def test_score_straightFlush_no_ace(self):
        # 5 cards
        cards = ('6H', 'TH', '8H', '2C', 'JD', '7H', '9H')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['TH', '9H', '8H', '7H', '6H'])

        # 6 cards
        cards = ('6H', 'TH', '8H', '2C', 'JH', '7H', '9H')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['JH', 'TH', '9H', '8H', '7H'])

        # 6 cards
        cards = ('6H', 'TH', '8H', 'QH', 'JH', '7H', '9H')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['QH', 'JH', 'TH', '9H', '8H'])

    def test_score_straightFlush_ace_high(self):
        # 5 cards
        cards = ('4H', 'AD', 'KD', 'JD', 'TC', 'TD', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JD', 'TD'])

        # 5 cards extra ace
        cards = ('4H', 'AD', 'KD', 'JD', 'AS', 'TD', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JD', 'TD'])

        # 5 cards 2 extra aces
        cards = ('AC', 'AD', 'KD', 'JD', 'AS', 'TD', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JD', 'TD'])

        # 6 cards
        cards = ('9D', 'AD', 'KD', 'JD', 'TC', 'TD', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JD', 'TD'])

        # 6 cards extra ace
        cards = ('AS', 'AD', 'KD', 'JD', 'TC', 'TD', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JD', 'TD'])

        # 7 cards
        cards = ('9D', 'AD', 'KD', 'JD', '8D', 'TD', 'QD')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['AD', 'KD', 'QD', 'JD', 'TD'])

    def test_score_straightFlush_ace_low(self):
        cards = ('4C', '5C', 'AC', '3C', '6S', '2C', '3H')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['5C', '4C', '3C', '2C', 'AC'])

        # extra ace
        cards = ('4C', '5C', 'AC', '3C', '7C', '2C', 'AH')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['5C', '4C', '3C', '2C', 'AC'])

        # 2 extra aces
        cards = ('4C', '5C', 'AC', '3C', 'AD', '2C', 'AH')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.STRAIGHT_FLUSH)
        self.assertEqual(score.HAND, ['5C', '4C', '3C', '2C', 'AC'])

    def test_score_straight_and_flush_but_not_both(self):
        cards = ('6H', 'TH', '8H', '2C', 'JH', '7H', '9S')
        score = get_score(cards)
        self.assertEqual(score.RANKING, Ranking.FLUSH)
        self.assertEqual(score.HAND, ['JH', 'TH', '8H', '7H', '6H'])

    def test_score_compare(self):
        # identical hand (a pair)
        p1 = ['7C', '6H']
        p2 = ['7C', '6H']
        shared = ['QS', '6C', 'TC', '5C', 'AH']
        score1 = get_score(p1 + shared)
        score2 = get_score(p2 + shared)
        c = score1.compare(score2)
        self.assertTrue(c == 0)

        # high card versus high card (a tie)
        p1 = ['7C', '2H']
        p2 = ['4S', '7D']
        shared = ['QS', '6C', 'TC', '5C', 'AH']
        score1 = get_score(p1 + shared)
        score2 = get_score(p2 + shared)
        c = score1.compare(score2)
        self.assertTrue(c == 0)

        # pair versus pair
        p1 = ['7C', '6H']
        p2 = ['TS', '9H']
        shared = ['QS', '6C', 'TC', '5C', 'AH']
        score1 = get_score(p1 + shared)
        score2 = get_score(p2 + shared)
        c = score1.compare(score2)
        self.assertTrue(c < 0)

        # flush versus flush
        p1 = ['KC', '7D']
        p2 = ['JH', '9C']
        shared = ['7C', 'KD', 'QC', '6C', '2C']
        score1 = get_score(p1 + shared)
        score2 = get_score(p2 + shared)
        c = score1.compare(score2)
        self.assertTrue(c > 0)

        # pair versus two-pair
        p1 = ['6S', 'JS']
        p2 = ['KS', 'QC']
        shared = ['QS', 'JH', 'KC', '9C', '5H']
        score1 = get_score(p1 + shared)
        score2 = get_score(p2 + shared)
        c = score1.compare(score2)
        self.assertTrue(c < 0)

        # pair versus high card
        p1 = ['2C', 'AH']
        p2 = ['3D', '7C']
        shared = ['9S', '2D', 'QD', '4H', 'TD']
        score1 = get_score(p1 + shared)
        score2 = get_score(p2 + shared)
        c = score1.compare(score2)
        self.assertTrue(c > 0)


if __name__ == '__main__':
    unittest.main()
