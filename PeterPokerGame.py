from Peter7CardBestHandRemastered2 import *


class Player:
    def __init__(self, chips, name):
        self.CHIPS = chips
        self.HAND = None
        self.name = name
        self.POS = None

    def __str__(self):
        return str(self.CHIPS) + ", " + str(self.HAND) + ", " + str(self.name)


class CPUPlayer(Player):
    def decide(self, other, the_table):
        decision = random.randint(1, 3)
        if decision == 1:
            if the_table.ACTIVE > 0:
                self.CHIPS -= the_table.ACTIVE
                the_table.ACTIVE *= 2
                the_table.POT += the_table.ACTIVE
                the_table.ACTIVE = 0
                print('CPU CALLS')
                return 'call'
            else:
                print('CPU CHECKS')
        elif decision == 2:
            raise_amount = random.randint(1, 10)
            if the_table.ACTIVE > 0:
                self.CHIPS -= the_table.ACTIVE
                the_table.ACTIVE *= 2
                the_table.POT += the_table.ACTIVE
                the_table.ACTIVE = 0
                self.CHIPS -= raise_amount
                the_table.ACTIVE += raise_amount
                print('CPU CALLS THEN RE-RAISES', raise_amount)
                return
            if the_table.ACTIVE == 0:
                self.CHIPS -= raise_amount
                the_table.ACTIVE += raise_amount
                print('CPU RAISES', raise_amount)
                return
        elif decision == 3:
            if the_table.ACTIVE == 0:
                print('CPU CHECKS')
            if the_table.ACTIVE > 0:
                the_table.POT += the_table.ACTIVE
                the_table.ACTIVE = 0
                other.CHIPS += the_table.POT
                print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                the_table.POT = 0
                return 'fold'


class CLPlayer(Player):
    def decide(self, other, the_table):
        if (the_table.ACTIVE > 0) and (the_table.POT > 0):
            choice = input('CALL, RAISE or FOLD?')
            if choice.upper() == 'CALL':
                self.CHIPS -= the_table.ACTIVE
                the_table.ACTIVE *= 2
                the_table.POT += the_table.ACTIVE
                the_table.ACTIVE = 0
                print('USER CALLS')
                return 'call'
            elif choice.upper() == 'RAISE':
                raise_amount = int(input('Amount: '))
                self.CHIPS -= the_table.ACTIVE
                the_table.ACTIVE *= 2
                the_table.POT += the_table.ACTIVE
                the_table.ACTIVE = 0
                self.CHIPS -= raise_amount
                the_table.ACTIVE += raise_amount
                print('USER RAISES', raise_amount)
                return
            else:
                the_table.POT += the_table.ACTIVE
                the_table.ACTIVE = 0
                other.CHIPS += the_table.POT
                print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                the_table.POT = 0
                return 'fold'
        else:
            choice = input('CHECK, RAISE or FOLD?')
            if choice.upper() == 'CHECK':
                print('USER CHECKS')
                return
            elif choice.upper() == 'RAISE':
                raise_amount = int(input('Amount: '))
                self.CHIPS -= raise_amount
                the_table.ACTIVE += raise_amount
                print('USER RAISES')
                return
            else:
                the_table.POT += the_table.ACTIVE
                the_table.ACTIVE = 0
                other.CHIPS += the_table.POT
                print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                the_table.POT = 0
                return 'fold'


class Table:
    def __init__(self, active_pot, pot):
        self.ACTIVE = active_pot
        self.POT = pot
        self.COM_CARDS = None
        self.ROUND = None

    def __str__(self):
        return self.POT + ", " + str(self.COM_CARDS)


pips = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
heart = ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
spade = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
club = ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
diamond = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']
hearts = list(zip(pips, heart))
spades = list(zip(pips, spade))
clubs = list(zip(pips, club))
diamonds = list(zip(pips, diamond))
deck = hearts + spades + clubs + diamonds
User = CLPlayer(1000, 'User')
CPU = CPUPlayer(1000, 'CPU')
table = Table(0, 0)


def play2(sb_player, bb_player):
    all_cards = random.sample(deck, 9)
    sb_player.HAND = all_cards[:2]
    bb_player.HAND = all_cards[2:4]
    table.COM_CARDS = all_cards[4:]
    bb_player.POS = 'BB'
    sb_player.POS = 'SB/D'
    print(sb_player.HAND)
    print(bb_player.HAND)
    print('Big Blind is:', bb_player.name)
    print('Small Blind is:', sb_player.name)
    print('USER CHIPS: ', User.CHIPS)
    print('CPU CHIPS: ', CPU.CHIPS)
    bb_player.CHIPS -= 10
    sb_player.CHIPS -= 5
    table.POT += 10
    table.ACTIVE += 5
    table.ROUND = 'PRE-FLOP'
    print(f'{sb_player.name} ANTES 5 \n{bb_player.name} ANTES 10')
    table_action_var = sb_player.decide(bb_player, table)
    if table_action_var == 'fold':
        return 'fold'
    table_action_var = bb_player.decide(sb_player, table)
    if table_action_var == 'fold':
        return 'fold'
    while table.ACTIVE > 0:
        table_action_var = sb_player.decide(bb_player, table)
        if table_action_var == 'fold':
            return 'fold'
        if table_action_var == 'call':
            if table.POT == 20:
                table_action_var = bb_player.decide(sb_player, table)
                if table_action_var == 'fold':
                    return 'fold'

    # Now we've finished the first round of betting

    else:  # now we are going to flip the first three shared cards (the flop)
        print(table.COM_CARDS[:3])
        table.ROUND = 'FLOP'
        table_action_var = bb_player.decide(sb_player, table)
        if table_action_var == 'fold':
            return 'fold'
        table_action_var = sb_player.decide(bb_player, table)
        if table_action_var == 'fold':
            return 'fold'
        while table.ACTIVE > 0:
            table_action_var = bb_player.decide(sb_player, table)
            if table_action_var == 'fold':
                return 'fold'
            if table_action_var != 'call':
                table_action_var = sb_player.decide(bb_player, table)
                if table_action_var == 'fold':
                    return 'fold'
        else:  # now we are going to flip the 4th shared card (the turn)
            print(table.COM_CARDS[:4])
            table.ROUND = 'TURN'
            table_action_var = bb_player.decide(sb_player, table)
            if table_action_var == 'fold':
                return 'fold'
            table_action_var = sb_player.decide(bb_player, table)
            if table_action_var == 'fold':
                return 'fold'
            while table.ACTIVE > 0:
                table_action_var = bb_player.decide(sb_player, table)
                if table_action_var == 'fold':
                    return 'fold'
                if table_action_var != 'call':
                    table_action_var = sb_player.decide(bb_player, table)
                    if table_action_var == 'fold':
                        return 'fold'
            else:  # now we are going to flip the 5th shared card (the river)
                print(table.COM_CARDS[:5])
                table.ROUND = 'RIVER'
                table_action_var = bb_player.decide(sb_player, table)
                if table_action_var == 'fold':
                    return 'fold'
                table_action_var = sb_player.decide(bb_player, table)
                if table_action_var == 'fold':
                    return 'fold'
                while table.ACTIVE > 0:
                    table_action_var = bb_player.decide(sb_player, table)
                    if table_action_var == 'fold':
                        return 'fold'
                    if table_action_var != 'call':
                        table_action_var = sb_player.decide(bb_player, table)
                        if table_action_var == 'fold':
                            return 'fold'
                else:  # Now we determine which hand won
                    hand1 = sb_player.HAND
                    hand1.extend(table.COM_CARDS)
                    pips1 = []
                    suits1 = []
                    for e in hand1:
                        pips1.append(e[0])
                        suits1.append(e[1])
                    hand2 = bb_player.HAND
                    hand2.extend(table.COM_CARDS)
                    pips2 = []
                    suits2 = []
                    for x in hand2:
                        pips2.append(x[0])
                        suits2.append(x[1])
                    score1 = best_hands(*pips1, *suits1)
                    score2 = best_hands(*pips2, *suits2)
                    c = score1.compare(score2)
                    if c > 0:
                        sb_player.CHIPS += table.POT
                        print(f'{sb_player.name} WINS WITH ' + str(score1) + ' +' + str(table.POT))
                        table.POT = 0
                        print(sb_player.HAND[:2])
                        print(bb_player.HAND[:2])
                        return 'fold'
                    elif c < 0:
                        bb_player.CHIPS += table.POT
                        print(f'{bb_player.name} WINS WITH ' + str(score2) + ' +' + str(table.POT))
                        table.POT = 0
                        print(sb_player.HAND[:2])
                        print(bb_player.HAND[:2])
                        return 'fold'
                    elif c == 0:
                        table.POT /= 2
                        sb_player.CHIPS += table.POT
                        bb_player.CHIPS += table.POT
                        print(f'IT\'S A TIE! \n {sb_player.name} +' + str(table.POT) + f'\n {bb_player.name} +' + str(table.POT))
                        print(sb_player.HAND[:2])
                        print(bb_player.HAND[:2])
                        return 'fold'


if __name__ == '__main__':
    player_1 = User
    player_2 = CPU
    # Next line isn't right
    while CPU.CHIPS and User.CHIPS > 0:
        print()
        play2(player_1, player_2)
        y = player_1
        player_1 = player_2
        player_2 = y
