# import poker5
#
#
# if __name__ == '__main__':
#     deck = poker5.get_deck()
#     player1 = deck[0:2]
#     player2 = deck[2:4]
#     player3 = deck[4:6]
#     player4 = deck[6:8]
#     shared = deck[8:13]
#     score1 = poker5.get_score(player1 + shared)
#     score2 = poker5.get_score(player2 + shared)
#     score3 = poker5.get_score(player3 + shared)
#     score4 = poker5.get_score(player4 + shared)
#     a = score1.compare(score2)
#     b = score1.compare(score3)
#     c = score1.compare(score4)
#     print(player1)
#     print(player2)
#     print(player3)
#     print(player4)
#     print(shared)
#     print(score1)
#     print(score2)
#     print(score3)
#     print(score4)
#     print(a)
#     print(b)
#     print(c)
import random

if __name__ == '__main__':
    re = None
    Q = random.randint(0, 1)
    if Q == 1:
        if re is None:
            re = []
        re.append(Q)
    print(re)
