from poker5 import Ranking


if __name__ == "__main__":
    r1 = Ranking.FOUR_OF_A_KIND
    r2 = Ranking.FLUSH
    if r1 > r2:
        print("r1 has a better hand")
    else:
        print("r2 has a better hand")
