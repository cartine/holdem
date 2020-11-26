

class Player:
    def __init__(self, name, chips):
        self.NAME = name
        self.CHIPS = chips

    def decide(self):
        print('inside Player')


class CPUPlayer(Player):
    def decide(self):
        print('inside CPUPlayer')


class CLPlayer(Player):
    def decide(self):
        print('inside CLPlayer')


if __name__ == "__main__":
    # player1 = Player('x', 0)
    # player2 = CPUPlayer('x', 0)
    # player3 = CLPlayer('x', 0)
    #
    # player1.decide()
    # player2.decide()
    # player3.decide()

    x = -1
    y = 3
    z = (x) and (y > 0)
    print(z)


