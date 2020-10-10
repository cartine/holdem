import unittest
from PeterBestHand import *

class TestPeterBestHand(unittest.TestCase):

    # high card
    h1 = ('TC', '9D', '3S', '2H', 'AH', '8C', 'KD')

    # straight flush
    h2 = ('6H', 'TH', '8H', '7H', '9H')

    # straight flush, cards ordered
    h2 = ('TH', '9H', '8H', '7H', '6H')

    # straight flush
    h3 = ('6H', 'TH', '8H', '7H', '9H')

    # straight flush
    h4 = ('TH', '8H', '7H', '6H', '9H')

    def test_straight_flush(self):
        # p1 = changeParams(self.h1)
        # self.assertFalse(Straight_flush(*p1))
        #
        # p2 = changeParams(self.h2)
        # r2 = Straight_flush(*p2)
        # self.assertTrue(r2)

        # p3 = changeParams(self.h3)
        # r3 = Straight_flush(*p3)
        # self.assertTrue(r3)

        p = changeParams(self.h4)
        r = Straight_flush(*p)
        self.assertTrue(r)


if __name__ == '__main__':
    unittest.main()
