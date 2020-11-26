from Peter7CardBestHandRemastered2 import *


class Player:
    def __init__(self, chips, position):
        self.CHIPS = chips
        self.HAND = None
        self.POS = position  # 'BB' or 'SB/D' for Big Blind or Small Blind/Dealer

    def __str__(self):
        return str(self.CHIPS) + ", " + str(self.HAND) + ", " + str(self.POS)


class Table:
    def __init__(self, active_pot, pot):
        self.ACTIVE = active_pot
        self.POT = pot
        self.COM_CARDS = None

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
User = Player(1000, 'SB/D')
CPU = Player(1000, 'BB')
table = Table(0, 0)


def cpu_play():
    decision = random.randint(1, 3)
    if decision == 1:
        if table.ACTIVE > 0:
            CPU.CHIPS -= table.ACTIVE
            table.ACTIVE *= 2
            table.POT += table.ACTIVE
            table.ACTIVE = 0
            print('CPU CALLS')
            return 'call'
        else:
            print('CPU CHECKS')
    elif decision == 2:
        raise_amount = random.randint(1, 10)
        if table.ACTIVE > 0:
            CPU.CHIPS -= table.ACTIVE
            table.ACTIVE *= 2
            table.POT += table.ACTIVE
            table.ACTIVE = 0
            CPU.CHIPS -= raise_amount
            table.ACTIVE += raise_amount
            print('CPU CALLS THEN RE-RAISES', raise_amount)
            return
        if table.ACTIVE == 0:
            CPU.CHIPS -= raise_amount
            table.ACTIVE += raise_amount
            print('CPU RAISES', raise_amount)
            return
    elif decision == 3:
        return 'cpu fold'


def user_play():
    if table.ACTIVE and table.POT > 0:
        choice = input('CALL, RAISE or FOLD?')
        if choice.upper() == 'CALL':
            User.CHIPS -= table.ACTIVE
            table.ACTIVE *= 2
            table.POT += table.ACTIVE
            table.ACTIVE = 0
            print('USER CALLS')
            return 'call'
        elif choice.upper() == 'RAISE':
            raise_amount = int(input('Amount: '))
            User.CHIPS -= table.ACTIVE
            table.ACTIVE *= 2
            table.POT += table.ACTIVE
            table.ACTIVE = 0
            User.CHIPS -= raise_amount
            table.ACTIVE += raise_amount
            print('USER RAISES', raise_amount)
            return
        else:
            return 'user fold'
    else:
        choice = input('CHECK, RAISE or FOLD?')
        if choice.upper() == 'CHECK':
            print('USER CHECKS')
            return
        elif choice.upper() == 'RAISE':
            raise_amount = int(input('Amount: '))
            User.CHIPS -= raise_amount
            table.ACTIVE += raise_amount
            print('USER RAISES')
            return
        else:
            return 'user fold'


def table_action(decision):
    if decision == 'user fold':
        table.POT += table.ACTIVE
        table.ACTIVE = 0
        CPU.CHIPS += table.POT
        print('USER FOLDS \n CPU +' + str(table.POT))
        table.POT = 0
        return 'fold'
    elif decision == 'cpu fold':
        table.POT += table.ACTIVE
        table.ACTIVE = 0
        User.CHIPS += table.POT
        print('CPU FOLDS \n USER +' + str(table.POT))
        table.POT = 0
        return 'fold'
    elif decision == 'call':
        return 'call'
    else:
        print('ACTIVE POT:', table.ACTIVE, 'CENTER POT:', table.POT)


def play():
    User.HAND = random.sample(deck, 2)
    CPU.HAND = random.sample(deck, 2)
    table.COM_CARDS = random.sample(deck, 5)
    print(User.HAND)
    print('USER CHIPS: ', User.CHIPS)
    print('CPU CHIPS: ', CPU.CHIPS)
    print('USER POSITION: ', User.POS)
    table_action_var = 0
    if User.POS == 'SB/D':
        CPU.CHIPS -= 10
        User.CHIPS -= 5
        table.POT += 10
        table.ACTIVE += 5
        print('USER ANTES 5 \n CPU ANTES 10')
        table_action_var = table_action(user_play())
        if table_action_var == 'fold':
            return 'fold'
        table_action_var = table_action(cpu_play())
        if table_action_var == 'fold':
            return 'fold'
        while table.ACTIVE > 0:
            table_action_var = table_action(user_play())
            if table_action_var == 'fold':
                return 'fold'
            if table_action_var == 'call':
                if table.POT == 20:
                    table_action_var = table_action(cpu_play())
                    if table_action_var == 'fold':
                        return 'fold'
        else:
            print(table.COM_CARDS[:3])
            table_action_var = table_action(cpu_play())
            if table_action_var == 'fold':
                return 'fold'
            table_action_var = table_action(user_play())
            if table_action_var == 'fold':
                return 'fold'
            while table.ACTIVE > 0:
                table_action_var = table_action(cpu_play())
                if table_action_var == 'fold':
                    return 'fold'
                if table_action_var != 'call':
                    table_action_var = table_action(user_play())
                    if table_action_var == 'fold':
                        return 'fold'
            else:
                print(table.COM_CARDS[:4])
                table_action_var = table_action(cpu_play())
                if table_action_var == 'fold':
                    return 'fold'
                table_action_var = table_action(user_play())
                if table_action_var == 'fold':
                    return 'fold'
                while table.ACTIVE > 0:
                    table_action_var = table_action(cpu_play())
                    if table_action_var == 'fold':
                        return 'fold'
                    if table_action_var != 'call':
                        table_action_var = table_action(user_play())
                        if table_action_var == 'fold':
                            return 'fold'
                else:
                    print(table.COM_CARDS[:5])
                    table_action_var = table_action(cpu_play())
                    if table_action_var == 'fold':
                        return 'fold'
                    table_action_var = table_action(user_play())
                    if table_action_var == 'fold':
                        return 'fold'
                    while table.ACTIVE > 0:
                        table_action_var = table_action(cpu_play())
                        if table_action_var == 'fold':
                            return 'fold'
                        if table_action_var != 'call':
                            table_action_var = table_action(user_play())
                            if table_action_var == 'fold':
                                return 'fold'
                    else:
                        hand1 = User.HAND
                        hand1.extend(table.COM_CARDS)
                        pips1 = []
                        suits1 = []
                        for e in hand1:
                            pips1.append(e[0])
                            suits1.append(e[1])
                        hand2 = CPU.HAND
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
                            User.CHIPS += table.POT
                            print('USER WINS WITH ' + str(score2) + ' +' + str(table.POT))
                            table.POT = 0
                            return 'fold'
                        elif c < 0:
                            CPU.CHIPS += table.POT
                            print('CPU WINS WITH ' + str(score2) + ' +' + str(table.POT))
                            table.POT = 0
                            return 'fold'
                        elif c == 0:
                            table.POT /= 2
                            User.CHIPS += table.POT
                            CPU.CHIPS += table.POT
                            print('IT\'S A TIE! \n USER +' + str(table.POT) + '\n CPU +' + str(table.POT))
                            return 'fold'
    if User.POS == 'BB':
        User.CHIPS -= 10
        CPU.CHIPS -= 5
        table.POT += 10
        table.ACTIVE += 5
        print('CPU ANTES 5 \n USER ANTES 10')
        table_action_var = table_action(cpu_play())
        if table_action_var == 'fold':
            return 'fold'
        table_action_var = table_action(user_play())
        if table_action_var == 'fold':
            return 'fold'
        while table.ACTIVE > 0:
            table_action_var = table_action(cpu_play())
            if table_action_var == 'fold':
                return 'fold'
            if table_action_var == 'call':
                if table.POT == 20:
                    table_action_var = table_action(user_play())
                    if table_action_var == 'fold':
                        return 'fold'
        else:
            print(table.COM_CARDS[:3])
            table_action_var = table_action(user_play())
            if table_action_var == 'fold':
                return 'fold'
            table_action_var = table_action(cpu_play())
            if table_action_var == 'fold':
                return 'fold'
            while table.ACTIVE > 0:
                table_action_var = table_action(user_play())
                if table_action_var == 'fold':
                    return 'fold'
                if table_action_var == 'call':
                    table_action_var = table_action(cpu_play())
                    if table_action_var == 'fold':
                        return 'fold'
            else:
                print(table.COM_CARDS[:4])
                table_action_var = table_action(user_play())
                if table_action_var == 'fold':
                    return 'fold'
                table_action_var = table_action(cpu_play())
                if table_action_var == 'fold':
                    return 'fold'
                while table.ACTIVE > 0:
                    table_action_var = table_action(user_play())
                    if table_action_var == 'fold':
                        return 'fold'
                    if table_action_var == 'call':
                        table_action_var = table_action(cpu_play())
                        if table_action_var == 'fold':
                            return 'fold'
                else:
                    print(table.COM_CARDS[:5])
                    table_action_var = table_action(user_play())
                    if table_action_var == 'fold':
                        return 'fold'
                    table_action_var = table_action(cpu_play())
                    if table_action_var == 'fold':
                        return 'fold'
                    while table.ACTIVE > 0:
                        table_action_var = table_action(user_play())
                        if table_action_var == 'fold':
                            return 'fold'
                        if table_action_var == 'call':
                            table_action_var = table_action(cpu_play())
                            if table_action_var == 'fold':
                                return 'fold'
                    else:
                        hand1 = User.HAND
                        hand1.extend(table.COM_CARDS)
                        pips1 = []
                        suits1 = []
                        for e in hand1:
                            pips1.append(e[0])
                            suits1.append(e[1])
                        hand2 = CPU.HAND
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
                            User.CHIPS += table.POT
                            print('USER WINS WITH ' + str(score2) + ' +' + str(table.POT))
                            table.POT = 0
                            return 'fold'
                        elif c < 0:
                            CPU.CHIPS += table.POT
                            print('CPU WINS WITH ' + str(score2) + ' +' + str(table.POT))
                            table.POT = 0
                            return 'fold'
                        elif c == 0:
                            table.POT /= 2
                            User.CHIPS += table.POT
                            CPU.CHIPS += table.POT
                            print('IT\'S A TIE! \n USER +' + str(table.POT) + '\n CPU +' + str(table.POT))
                            return 'fold'


if __name__ == '__main__':
    while CPU.CHIPS and User.CHIPS > 0:
        play_return = play()
        if play_return == 'fold':
            if User.POS == 'BB':
                User.POS = 'SB/D'
                CPU.POS = 'BB'
            else:
                User.POS = 'BB'
                CPU.POS = 'SB/D'
