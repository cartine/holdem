# import pyautogui
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# if __name__ == '__main__':
#     i = Image.open('10ofClubs.png')
#     iar = np.asarray(i)
#     plt.imshow(iar)
#     print(iar)
#
#
#
# pyautogui.hotkey('alt', 'tab')
# pyautogui.moveTo(100, 100)
from PeterPokerGame import *
from PokerOddsCalculator import calculator


class CPUPlayer2(Player):
    def decide(self, other, the_table):
        nums1 = []
        shapes = []
        raise_amount = 0
        for e in self.HAND:
            nums1.append(e[0])
            shapes.append(e[1])
        nums2 = [face_cards(num) for num in nums1]
        nums = sorted(nums2, reverse=True)
        if the_table.ROUND == 'PRE-FLOP':
            if the_table.ACTIVE == 0:
                if nums[0] == nums[1]:
                    if nums[0] > 6:
                        if nums[0] == 7:
                            raise_amount = random.randint(the_table.POT/4, (the_table.POT/2))
                        if nums[0] == 8:
                            raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 3)
                        if nums[0] == 9:
                            raise_amount = random.randint((the_table.POT/4) + 2, (the_table.POT/8) * 5)
                        if nums[0] == 10:
                            raise_amount = random.randint((the_table.POT/4) + 3, (the_table.POT/4) * 3)
                        if nums[0] == 11:
                            raise_amount = random.randint((the_table.POT/2), (the_table.POT/8) * 7)
                        if nums[0] == 12:
                            raise_amount = random.randint((the_table.POT/2), the_table.POT)
                        if nums[0] == 13:
                            raise_amount = random.randint((the_table.POT/2), the_table.POT)
                        if nums[0] == 14:
                            raise_amount = random.randint((the_table.POT/2), the_table.POT)
                        self.CHIPS -= raise_amount
                        the_table.ACTIVE += raise_amount
                        print('CPU2 RAISES', raise_amount)
                        return
                    else:
                        print('CPU2 CHECKS')
                        return
                else:
                    if nums[0] >= 13:
                        if shapes[0] == shapes[1]:
                            if nums[0] == 14:
                                if nums[1] == 10:
                                    raise_amount = random.randint((the_table.POT/4), (the_table.POT/2))
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 1)
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 2)
                                self.CHIPS -= raise_amount
                                the_table.ACTIVE += raise_amount
                                print('CPU2 RAISES', raise_amount)
                                return
                            elif nums[0] == 13:
                                if nums[1] == 12:
                                    raise_amount = random.randint((the_table.POT/4) - 1, (the_table.POT/2) - 1)
                                self.CHIPS -= raise_amount
                                the_table.ACTIVE += raise_amount
                                print('CPU2 RAISES', raise_amount)
                                return
                            else:
                                print('CPU2 CHECKS')
                                return
                        else:
                            if nums[0] == 14:
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT/4) - 1, (the_table.POT/2))
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT/4) + 1, (the_table.POT/2) + 1)
                                self.CHIPS -= raise_amount
                                the_table.ACTIVE += raise_amount
                                print('CPU2 RAISES', raise_amount)
                                return
                            else:
                                print('CPU2 CHECKS')
                                return
                    else:
                        print('CPU2 CHECKS')
                        return
            else:
                if nums[0] == nums[1]:
                    if nums[0] > 6:
                        if nums[0] == 7:
                            raise_amount = random.randint(the_table.POT / 4, (the_table.POT / 2))
                        if nums[0] == 8:
                            raise_amount = random.randint((the_table.POT / 4) + 1, (the_table.POT / 2) + 3)
                        if nums[0] == 9:
                            raise_amount = random.randint((the_table.POT / 4) + 2, (the_table.POT / 8) * 5)
                        if nums[0] == 10:
                            raise_amount = random.randint((the_table.POT / 4) + 3, (the_table.POT / 4) * 3)
                        if nums[0] == 11:
                            raise_amount = random.randint((the_table.POT / 2), (the_table.POT / 8) * 7)
                        if nums[0] == 12:
                            raise_amount = random.randint((the_table.POT / 2), the_table.POT)
                        if nums[0] == 13:
                            raise_amount = random.randint((the_table.POT / 2), the_table.POT)
                        if nums[0] == 14:
                            raise_amount = random.randint((the_table.POT / 2), the_table.POT)
                        self.CHIPS -= the_table.ACTIVE
                        the_table.ACTIVE *= 2
                        the_table.POT += the_table.ACTIVE
                        the_table.ACTIVE = 0
                        self.CHIPS -= raise_amount
                        the_table.ACTIVE += raise_amount
                        print('CPU2 RAISES', raise_amount)
                        return
                    else:
                        if (nums[0] == 5) or (nums[0] == 6):
                            self.CHIPS -= the_table.ACTIVE
                            the_table.ACTIVE *= 2
                            the_table.POT += the_table.ACTIVE
                            the_table.ACTIVE = 0
                            print('CPU2 CALLS')
                            return 'call'
                        else:
                            the_table.POT += the_table.ACTIVE
                            the_table.ACTIVE = 0
                            other.CHIPS += the_table.POT
                            print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                            the_table.POT = 0
                            return 'fold'
                else:
                    if shapes[0] == shapes[1]:
                        if nums[0] == 14:
                            if nums[1] > 9:
                                if nums[1] == 10:
                                    raise_amount = random.randint((the_table.POT / 4), (the_table.POT / 2))
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT / 4) + 1,
                                                                  (the_table.POT / 2) + 1)
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT / 4) + 1,
                                                                  (the_table.POT / 2) + 2)
                                self.CHIPS -= the_table.ACTIVE
                                the_table.ACTIVE *= 2
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                self.CHIPS -= raise_amount
                                the_table.ACTIVE += raise_amount
                                print('CPU2 RAISES', raise_amount)
                                return
                            else:
                                if (nums[1] == 9) or (nums[1] == 8) or (nums[1] == 7) or (nums[1] == 5):
                                    self.CHIPS -= the_table.ACTIVE
                                    the_table.ACTIVE *= 2
                                    the_table.POT += the_table.ACTIVE
                                    the_table.ACTIVE = 0
                                    print('CPU2 CALLS')
                                    return 'call'
                                else:
                                    the_table.POT += the_table.ACTIVE
                                    the_table.ACTIVE = 0
                                    other.CHIPS += the_table.POT
                                    print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                                    the_table.POT = 0
                                    return 'fold'
                        elif nums[0] == 13:
                            if nums[1] == 12:
                                raise_amount = random.randint((the_table.POT / 4) - 1,
                                                              (the_table.POT / 2) - 1)
                                self.CHIPS -= the_table.ACTIVE
                                the_table.ACTIVE *= 2
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                self.CHIPS -= raise_amount
                                the_table.ACTIVE += raise_amount
                                print('CPU2 RAISES', raise_amount)
                                return
                            else:
                                if (nums[1] == 9) or (nums[1] == 10) or (nums[1] == 11):
                                    self.CHIPS -= the_table.ACTIVE
                                    the_table.ACTIVE *= 2
                                    the_table.POT += the_table.ACTIVE
                                    the_table.ACTIVE = 0
                                    print('CPU2 CALLS')
                                    return 'call'
                                else:
                                    the_table.POT += the_table.ACTIVE
                                    the_table.ACTIVE = 0
                                    other.CHIPS += the_table.POT
                                    print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                                    the_table.POT = 0
                                    return 'fold'
                        elif nums[0] == 12:
                            if (nums[1] == 11) or (nums[1] == 12):
                                self.CHIPS -= the_table.ACTIVE
                                the_table.ACTIVE *= 2
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                print('CPU2 CALLS')
                                return 'call'
                            else:
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                other.CHIPS += the_table.POT
                                print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                                the_table.POT = 0
                                return 'fold'
                        else:
                            the_table.POT += the_table.ACTIVE
                            the_table.ACTIVE = 0
                            other.CHIPS += the_table.POT
                            print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                            the_table.POT = 0
                            return 'fold'
                    else:
                        if nums[0] == 14:
                            if nums[1] > 10:
                                if 13 > nums[1] > 10:
                                    raise_amount = random.randint((the_table.POT / 4) - 1, (the_table.POT / 2))
                                if nums[1] == 13:
                                    raise_amount = random.randint((the_table.POT / 4) + 1,
                                                                  (the_table.POT / 2) + 1)
                                self.CHIPS -= the_table.ACTIVE
                                the_table.ACTIVE *= 2
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                self.CHIPS -= raise_amount
                                the_table.ACTIVE += raise_amount
                                print('CPU2 RAISES', raise_amount)
                                return
                            elif nums[1] == 10:
                                self.CHIPS -= the_table.ACTIVE
                                the_table.ACTIVE *= 2
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                print('CPU2 CALLS')
                                return 'call'
                            else:
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                other.CHIPS += the_table.POT
                                print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                                the_table.POT = 0
                                return 'fold'
                        elif nums[0] == 13:
                            if nums[1] > 9:
                                self.CHIPS -= the_table.ACTIVE
                                the_table.ACTIVE *= 2
                                the_table.POT += the_table.ACTIVE
                                the_table.ACTIVE = 0
                                print('CPU2 CALLS')
                                return 'call'
                        else:
                            the_table.POT += the_table.ACTIVE
                            the_table.ACTIVE = 0
                            other.CHIPS += the_table.POT
                            print(f'{self.name} FOLDS \n {other.name} +' + str(the_table.POT))
                            the_table.POT = 0
                            return 'fold'
        elif the_table.ROUND == 'FLOP':
            up_cards = []
            for x in self.HAND:
                up_cards.append(x)
            for x in the_table.COM_CARDS[:3]:
                up_cards.append(x)
            print(up_cards)
            hand_odds = calculator(up_cards)
            high_card_score = hand_odds[hand_odds.Score == 'HIGH_CARD']
            pair_score = hand_odds[hand_odds.Score == 'PAIR']
            two_pair_score = hand_odds[hand_odds.Score == 'TWO_PAIRS']
            trips_score = hand_odds[hand_odds.Score == 'THREE_OF_A_KIND']
            straight_score = hand_odds[hand_odds.Score == 'STRAIGHT']
            flush_score = hand_odds[hand_odds.Score == 'FLUSH']
            full_house_score = hand_odds[hand_odds.Score == 'FULL_HOUSE']
            quads_score = hand_odds[hand_odds.Score == 'FOUR_OF_A_KIND']
            straight_flush_score = hand_odds[hand_odds.Score == 'STRAIGHT_FLUSH']
            high_card_index = high_card_score[high_card_score['Score'] == 'HIGH_CARD'].Value.values
            pair_index = pair_score[pair_score['Score'] == 'PAIR'].Value.values
            two_pair_index = two_pair_score[two_pair_score['Score'] == 'TWO_PAIRS'].Value.values
            trips_index = trips_score[trips_score['Score'] == 'THREE_OF_A_KIND'].Value.values
            straight_index = straight_score[straight_score['Score'] == 'STRAIGHT'].Value.values
            flush_index = flush_score[flush_score['Score'] == 'FLUSH'].Value.values
            full_house_index = full_house_score[full_house_score['Score'] == 'FULL_HOUSE'].Value.values
            quads_index = quads_score[quads_score['Score'] == 'FOUR_OF_A_KIND'].Value.values
            straight_flush_index = straight_flush_score[straight_flush_score['Score'] == 'STRAIGHT_FLUSH'].Value.values
            high_card_percent = high_card_score[high_card_score['Score'] == 'HIGH_CARD'].Percent.values
            pair_percent = pair_score[pair_score['Score'] == 'PAIR'].Percent.values
            two_pair_percent = two_pair_score[two_pair_score['Score'] == 'TWO_PAIRS'].Percent.values
            trips_percent = trips_score[trips_score['Score'] == 'THREE_OF_A_KIND'].Percent.values
            straight_percent = straight_score[straight_score['Score'] == 'STRAIGHT'].Percent.values
            flush_percent = flush_score[flush_score['Score'] == 'FLUSH'].Percent.values
            full_house_percent = full_house_score[full_house_score['Score'] == 'FULL_HOUSE'].Percent.values
            quads_percent = quads_score[quads_score['Score'] == 'FOUR_OF_A_KIND'].Percent.values
            straight_flush_percent = straight_flush_score[straight_flush_score['Score'] == 'STRAIGHT_FLUSH'].Percent.values
            if the_table.ACTIVE > 0:
                if high_card_index.size == 0:
                    self.CHIPS -= the_table.ACTIVE
                    the_table.ACTIVE *= 2
                    the_table.POT += the_table.ACTIVE
                    the_table.ACTIVE = 0
                    print('CPU2 CALLS')
                    return 'call'
                else:
                    if (pair_percent > 30) or (pair_percent == 0):
                        self.CHIPS -= the_table.ACTIVE
                        the_table.ACTIVE *= 2
                        the_table.POT += the_table.ACTIVE
                        the_table.ACTIVE = 0
                        print('CPU2 CALLS')
                        return 'call'


if __name__ == '__main__':
    CPU2 = CPUPlayer2(1000, 'CPU2')
    player_1 = CPU
    player_2 = CPU2
    play2(player_1, player_2)
    # while CPU.CHIPS and CPU2.CHIPS > 0:
    #     print()
    #     play2(player_1, player_2)
    #     y = player_1
    #     player_1 = player_2
    #     player_2 = y


