from poker5 import Score
from poker5 import Ranking

if __name__ == "__main__":
    hand1 = ['QH', '9H', '8H', '7H', '6H']
    hand2 = ['QH', '9H', '8H', '7H', '6H']

    score1 = Score(Ranking.HIGH_CARD, hand1)
    score2 = Score(Ranking.FLUSH, hand2)

    print(score1.compare(score2))
