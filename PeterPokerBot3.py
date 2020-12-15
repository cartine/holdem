from PeterPokerGame import *
from PokerOddsCalculator import DataFrameWrapper
from multiplayer_holdem_game import *
from game2 import *
from StartingHandsBot3 import *
import math


class CPUPlayer3(Player):
    def decide(self, the_table, betting_round, call_amount, seats, your_index):
        # print('vvvvvvvvvvvvvvvv')
        # print('^^^^^^^^^^^^^^^^')
        num_seats = 0
        pos = 0
        for seat in seats:
            num_seats += 1
        if num_seats == 2:
            if your_index == 0:
                pos = 'post_flop_last'
            elif your_index == 1:
                pos = 'post_flop_first'
        else:
            if num_seats - 1 == your_index:
                pos = 'BU'
            elif your_index == 0:
                pos = 'SB'
            elif your_index == 1:
                pos = 'BB'
            elif num_seats - 2 > 1:
                if num_seats - 2 == your_index:
                    pos = 'CU'
            else:
                pos = 'EP'
        nums = []
        shapes = []
        raise_amount = 0
        for e in self.HAND:
            nums.append(e[0])
            shapes.append(e[1])
        if betting_round == BettingRound.PRE_FLOP:
            limps = 0
            nums = sorted(nums, key=lambda x: int(face_cards(x)), reverse=True)
            if shapes[0] == shapes[1]:
                hand = nums[0] + nums[1] + 's'
            else:
                hand = nums[0] + nums[1]
                hand = str(hand)
            if pos == 'SB':
                if call_amount > (the_table.BIG_BLIND/2):
                    hand_index = hand in ep_and_blind_raise_starting_hands_3bet
                    if hand_index is True:
                        raise_amount = (call_amount - the_table.BIG_BLIND) * 3.5
                        return Action.RAISE, raise_amount
                    else:
                        hand_index = hand in ep_and_blind_raise_starting_hands_call
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            return Action.FOLD, 0
                else:
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand in blind_limp_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = (3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND)
                            return Action.RAISE, raise_amount
                        else:
                            return Action.FOLD, 0
                    else:
                        return Action.CALL, 0
            if pos == 'BB':
                if call_amount > 0:
                    hand_index = hand in ep_and_blind_raise_starting_hands_3bet
                    if hand_index is True:
                        raise_amount = (call_amount - the_table.BIG_BLIND) * 3.5
                        return Action.RAISE, raise_amount
                    else:
                        hand_index = hand in ep_and_blind_raise_starting_hands_call
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            return Action.FOLD, 0
                else:
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand in blind_limp_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = (3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND)
                            return Action.RAISE, raise_amount
                        else:
                            return Action.FOLD, 0
                    else:
                        return Action.CALL, 0
            if pos == 'BU':
                if call_amount > the_table.BIG_BLIND:
                    hand_index = hand in dealer_starting_hands_3bet
                    if hand_index is True:
                        raise_amount = (call_amount - the_table.BIG_BLIND) * 3.5
                        return Action.RAISE, raise_amount
                    else:
                        hand_index = hand in dealer_starting_hands_call
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            return Action.FOLD, 0
                else:
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand in dealer_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = (3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND)
                            return Action.RAISE, raise_amount
                        else:
                            return Action.FOLD, 0
                    else:
                        return Action.CALL, 0
            if pos == 'CU':
                if call_amount > the_table.BIG_BLIND:
                    hand_index = hand in cutoff_starting_hands_3bet
                    if hand_index is True:
                        raise_amount = (call_amount - the_table.BIG_BLIND) * 3.5
                        return Action.RAISE, raise_amount
                    else:
                        hand_index = hand in cutoff_starting_hands_call
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            return Action.FOLD, 0
                else:
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand in cutoff_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = (3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND)
                            return Action.RAISE, raise_amount
                        else:
                            return Action.FOLD, 0
                    else:
                        return Action.CALL, 0
            if pos == 'EP':
                if call_amount > the_table.BIG_BLIND:
                    hand_index = hand in ep_and_blind_raise_starting_hands_3bet
                    if hand_index is True:
                        raise_amount = (call_amount - the_table.BIG_BLIND) * 3.5
                        return Action.RAISE, raise_amount
                    else:
                        hand_index = hand in ep_and_blind_raise_starting_hands_call
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            return Action.FOLD, 0
                else:
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand in ep_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = (3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND)
                            return Action.RAISE, raise_amount
                        else:
                            return Action.FOLD, 0
                    else:
                        return Action.CALL, 0
            if pos == 'post_flop_last':
                if call_amount > (the_table.BIG_BLIND/2):
                    hand_index = hand in dealer_starting_hands_3bet
                    if hand_index is True:
                        raise_amount = (call_amount - the_table.BIG_BLIND) * 3.5
                        return Action.RAISE, raise_amount
                    else:
                        hand_index = hand in dealer_starting_hands_call
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            return Action.FOLD, 0
                else:
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand in dealer_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = (3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND)
                            return Action.RAISE, raise_amount
                        else:
                            return Action.FOLD, 0
                    else:
                        return Action.CALL, 0
            if pos == 'post_flop_first':
                if call_amount > 0:
                    hand_index = hand in ep_and_blind_raise_starting_hands_3bet
                    if hand_index is True:
                        raise_amount = (call_amount - the_table.BIG_BLIND) * 3.5
                        return Action.RAISE, raise_amount
                    else:
                        hand_index = hand in ep_and_blind_raise_starting_hands_call
                        if hand_index is True:
                            return Action.CALL, 0
                        else:
                            return Action.FOLD, 0
                else:
                    if seats[your_index].HAD_CHANCE_TO_ACT is False:
                        hand_index = hand in blind_limp_starting_hands_open_raise
                        for seat in seats:
                            if seat.HAD_CHANCE_TO_ACT is True:
                                limps += 1
                            if seat.NOT_FOLDED is False:
                                limps -= 1
                        if hand_index is True:
                            raise_amount = (3 * the_table.BIG_BLIND) + (limps * the_table.BIG_BLIND)
                            return Action.RAISE, raise_amount
                        else:
                            return Action.FOLD, 0
                    else:
                        return Action.CALL, 0
            return Action.CALL, 0
        if betting_round == BettingRound.POST_FLOP:
            hand = []
            for e in the_table.SHARED_CARDS_SHOWING:
                hand.append(e)
            for e in self.HAND:
                hand.append(e)
            hand_data = DataFrameWrapper(hand)
            if hand_data.current_score5(hand).RANKING >= 3:
                raise_amount = math.floor(random.randint(math.floor((the_table.POT/2)), math.floor(the_table.POT)) + 1)
                return Action.RAISE, raise_amount
            else:
                if call_amount == 0:
                    raise_amount = math.floor(hand_data.raise_break_even_percent(the_table.POT, hand_data.hit_percent(hand_data.calculator(hand)))) + 1
                    if raise_amount > 0:
                        return Action.RAISE, raise_amount
                    else:
                        return Action.CALL, 0
                else:
                    break_even_percent = hand_data.call_break_even_percent(the_table.POT, call_amount)
                    hit_percent = hand_data.hit_percent(hand_data.calculator(hand))
                    if hit_percent > break_even_percent:
                        return Action.CALL, 0
                    else:
                        return Action.FOLD, 0
        if betting_round is BettingRound.POST_TURN:
            hand = []
            for e in the_table.SHARED_CARDS_SHOWING:
                hand.append(e)
            for e in self.HAND:
                hand.append(e)
            hand_data = DataFrameWrapper(hand)
            if int(hand_data.current_score6(hand)['Value']) >= 3:
                raise_amount = math.floor(random.randint(math.floor((the_table.POT/2)), math.floor(the_table.POT)) + 1)
                return Action.RAISE, raise_amount
            else:
                if call_amount == 0:
                    raise_amount = math.floor(hand_data.raise_break_even_percent(the_table.POT, hand_data.hit_percent(hand_data.calculator(hand)))) + 1
                    if raise_amount > 0:
                        return Action.RAISE, raise_amount
                    else:
                        return Action.CALL, 0
                else:
                    break_even_percent = hand_data.call_break_even_percent(the_table.POT, call_amount)
                    hit_percent = hand_data.hit_percent(hand_data.calculator(hand))
                    if hit_percent > break_even_percent:
                        return Action.CALL, 0
                    else:
                        return Action.FOLD, 0
        if betting_round is BettingRound.POST_RIVER:
            hand = []
            for e in the_table.SHARED_CARDS_SHOWING:
                hand.append(e)
            for e in self.HAND:
                hand.append(e)
            hand_data = DataFrameWrapper(hand)
            hit_score = hand_data.current_score7(hand)
            if hit_score.RANKING >= 3:
                raise_amount = random.randint(math.floor((the_table.POT/2)), math.floor((the_table.POT) * hit_score.RANKING)) + 1
                return Action.RAISE, raise_amount
            else:
                if call_amount == 0:
                    return Action.CALL, 0
                else:
                    return Action.FOLD, 0

    def interpret(self, input):
        pass
