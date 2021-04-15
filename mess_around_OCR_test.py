import unittest
from OCR import *


class ComCardsTest(unittest.TestCase):
    def test1(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual([('J', 'C'), ('6', 'D'), ('T', 'S'), ('T', 'H')], com_cards)

    def test2(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual([('6', 'S'), ('J', 'S'), ('9', 'S'), ('2', 'S'), ('5', 'S')], com_cards)

    def test3(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual([('9', 'S'), ('5', 'H'), ('K', 'H')], com_cards)

    def test4(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual([('Q', 'C'), ('K', 'H'), ('7', 'D'), ('T', 'H'), ('Q', 'H')], com_cards)

    def test5(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual([], com_cards)

    def test6(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual([('2', 'D'), ('9', 'D'), ('J', 'H')], com_cards)

    def test7(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual([], com_cards)

    def test8(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual([('8', 'H'), ('5', 'C'), ('2', 'C'), ('A', 'H'), ('J', 'D')], com_cards)

    def test9(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual([], com_cards)

    def test10(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual([], com_cards)

    def test11(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual([('4', 'S'), ('5', 'D'), ('2', 'C'), ('4', 'C')], com_cards)

    def test12(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual([('Q', 'C'), ('Q', 'H'), ('T', 'S')], com_cards)

    def test13(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual([('Q', 'C'), ('Q', 'H'), ('T', 'S')], com_cards)

    def test14(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual([], com_cards)

    def test15(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual([('J', 'H'), ('J', 'S'), ('3', 'H'), ('8', 'H'), ('J', 'C')], com_cards)

    def test16(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual([], com_cards)

    def test17(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual([('T', 'S'), ('9', 'H'), ('5', 'H'), ('J', 'H')], com_cards)

    def test18(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual([('T', 'S'), ('9', 'H'), ('5', 'H'), ('J', 'H'), ('3', 'D')], com_cards)

    def test19(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual([], com_cards)

    def test20(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual([('A', 'C'), ('9', 'H'), ('8', 'C')], com_cards)

    def test21(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual([('A', 'C'), ('9', 'H'), ('8', 'C'), ('9', 'C'), ('5', 'C')], com_cards)

    def test22(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual([], com_cards)

    def test23(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual([], com_cards)

    def test24(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual([('K', 'S'), ('T', 'D'), ('6', 'C'), ('4', 'S')], com_cards)

    def test25(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual([('J', 'C'), ('7', 'H'), ('8', 'H'), ('A', 'H')], com_cards)

    def test26(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual([], com_cards)

    def test27(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual([], com_cards)

    def test28(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual([], com_cards)

    def test29(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual([('K', 'D'), ('T', 'C'), ('3', 'H')], com_cards)

    def test30(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual([], com_cards)

    def test31(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual([('8', 'C'), ('Q', 'H'), ('2', 'C')], com_cards)

    def test32(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual([('8', 'C'), ('Q', 'H'), ('2', 'C'), ('K', 'S')], com_cards)

    def test33(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual([], com_cards)

    def test34(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual([('2', 'C'), ('4', 'S'), ('9', 'H')], com_cards)

    def test35(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual([], com_cards)

    def test36(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual([('K', 'D'), ('J', 'D'), ('2', 'D')], com_cards)

    def test37(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual([('K', 'D'), ('J', 'D'), ('2', 'D'), ('A', 'H')], com_cards)

    def test38(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual([('K', 'D'), ('J', 'D'), ('2', 'D'), ('A', 'H'), ('6', 'C')], com_cards)

    def test39(self):
        com_cards = find_com_cards(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual([], com_cards)


class TotalPotTest(unittest.TestCase):
    def test1(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(36, total_pot)

    def test2(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(8, total_pot)

    def test3(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(30, total_pot)

    def test4(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(18, total_pot)

    def test5(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(18, total_pot)

    def test6(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(24, total_pot)

    def test7(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(14, total_pot)

    def test8(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(18, total_pot)

    def test9(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(22, total_pot)

    def test10(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(10, total_pot)

    def test11(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(20, total_pot)

    def test12(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(42, total_pot)

    def test13(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(142, total_pot)

    def test14(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(14, total_pot)

    def test15(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(14, total_pot)

    def test16(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(18, total_pot)

    def test17(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(350, total_pot)

    def test18(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(0, total_pot)

    def test19(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(14, total_pot)

    def test20(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(28, total_pot)

    def test21(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(68, total_pot)

    def test22(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(44, total_pot)

    def test23(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(10, total_pot)

    def test24(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(48, total_pot)

    def test25(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(90, total_pot)

    def test26(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(44, total_pot)

    def test27(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(40, total_pot)

    def test28(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(28, total_pot)

    def test29(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(96, total_pot)

    def test30(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(22, total_pot)

    def test31(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(48, total_pot)

    def test32(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(48, total_pot)

    def test33(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(10, total_pot)

    def test34(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(64, total_pot)

    def test35(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(6, total_pot)

    def test36(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(16, total_pot)

    def test37(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(16, total_pot)

    def test38(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(16, total_pot)

    def test39(self):
        total_pot = find_total_pot(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(22, total_pot)


class FindDealerTest(unittest.TestCase):
    def test1(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(1, dealer)

    def test2(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(1, dealer)

    def test3(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(5, dealer)

    def test4(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(6, dealer)

    def test5(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(7, dealer)

    def test6(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(7, dealer)

    def test7(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(8, dealer)

    def test8(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(8, dealer)

    def test9(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(9, dealer)

    def test10(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(1, dealer)

    def test11(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(1, dealer)

    def test12(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(5, dealer)

    def test13(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(5, dealer)

    def test14(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(6, dealer)

    def test15(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(6, dealer)

    def test16(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(7, dealer)

    def test17(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(7, dealer)

    def test18(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(7, dealer)

    def test19(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(8, dealer)

    def test20(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(8, dealer)

    def test21(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(8, dealer)

    def test22(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(3, dealer)

    def test23(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(2, dealer)

    def test24(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(2, dealer)

    def test25(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(3, dealer)

    def test26(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(5, dealer)

    def test27(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(4, dealer)

    def test28(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(6, dealer)

    def test29(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(6, dealer)

    def test30(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(7, dealer)

    def test31(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(7, dealer)

    def test32(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(7, dealer)

    def test33(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(1, dealer)

    def test34(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(3, dealer)

    def test35(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(1, dealer)

    def test36(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(2, dealer)

    def test37(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(3, dealer)

    def test38(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(3, dealer)

    def test39(self):
        dealer = find_dealer(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(5, dealer)


class FindSeat1Test(unittest.TestCase):
    def test1(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(851.14, Seat1_Player.CHIPS)

    def test2(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(517.31, Seat1_Player.CHIPS)

    def test3(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(622.54, Seat1_Player.CHIPS)

    def test4(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(618.54, Seat1_Player.CHIPS)

    def test5(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(618.54, Seat1_Player.CHIPS)

    def test6(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(618.54, Seat1_Player.CHIPS)

    def test7(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(614.54, Seat1_Player.CHIPS)

    def test8(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(614.54, Seat1_Player.CHIPS)

    def test9(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(612.54, Seat1_Player.CHIPS)

    def test10(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(184.54, Seat1_Player.CHIPS)

    def test11(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(383.06, Seat1_Player.CHIPS)

    def test12(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(383.06, Seat1_Player.CHIPS)

    def test13(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(383.06, Seat1_Player.CHIPS)

    def test14(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(383.06, Seat1_Player.CHIPS)

    def test15(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(383.06, Seat1_Player.CHIPS)

    def test16(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(379.06, Seat1_Player.CHIPS)

    def test17(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(379.06, Seat1_Player.CHIPS)

    def test18(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(379.06, Seat1_Player.CHIPS)

    def test19(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(375.06, Seat1_Player.CHIPS)

    def test20(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(375.06, Seat1_Player.CHIPS)

    def test21(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(367.06, Seat1_Player.CHIPS)

    def test22(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(3325.50, Seat1_Player.CHIPS)

    def test23(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(2695.47, Seat1_Player.CHIPS)

    def test24(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(2679.47, Seat1_Player.CHIPS)

    def test25(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(2713.47, Seat1_Player.CHIPS)

    def test26(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(2468.47, Seat1_Player.CHIPS)

    def test27(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat1_Player)

    def test28(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat1_Player)

    def test29(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat1_Player)

    def test30(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat1_Player)

    def test31(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat1_Player)

    def test32(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat1_Player)

    def test33(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual((('T', 'D'),('7', 'D')), Seat1_Player.HAND)
        self.assertEqual(92, Seat1_Player.CHIPS)
        self.assertEqual('Self', Seat1_Player.NAME)

    def test34(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(1453, Seat1_Player.CHIPS)

    def test35(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat1_Player.HAND)
        self.assertEqual(772, Seat1_Player.CHIPS)

    def test36(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat1_Player)

    def test37(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat1_Player)

    def test38(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat1_Player)

    def test39(self):
        Seat1_Player = find_seat_1(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat1_Player)


class FindSeat2Test(unittest.TestCase):
    def test1(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat2_Player)

    def test2(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual((('7', 'H'),('6', 'D')), Seat2_Player.HAND)
        self.assertEqual(118, Seat2_Player.CHIPS)
        self.assertEqual('Self', Seat2_Player.NAME)

    def test3(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test4(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test5(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test6(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test7(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(396, Seat2_Player.CHIPS)

    def test8(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(396, Seat2_Player.CHIPS)

    def test9(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test10(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test11(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test12(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test13(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test14(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test15(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat2_Player)

    def test16(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test17(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test18(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test19(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test20(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test21(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(400, Seat2_Player.CHIPS)

    def test22(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual((('8', 'S'),('2', 'C')), Seat2_Player.HAND)
        self.assertEqual(116, Seat2_Player.CHIPS)
        self.assertEqual('Self', Seat2_Player.NAME)

    def test23(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual((('5', 'C'),('Q', 'D')), Seat2_Player.HAND)
        self.assertEqual(112, Seat2_Player.CHIPS)
        self.assertEqual('Self', Seat2_Player.NAME)

    def test24(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual((('5', 'C'),('Q', 'D')), Seat2_Player.HAND)
        self.assertEqual(108, Seat2_Player.CHIPS)
        self.assertEqual('Self', Seat2_Player.NAME)

    def test25(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual((('Q', 'C'),('3', 'H')), Seat2_Player.HAND)
        self.assertEqual(108, Seat2_Player.CHIPS)
        self.assertEqual('Self', Seat2_Player.NAME)

    def test26(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual((('9', 'S'),('J', 'S')), Seat2_Player.HAND)
        self.assertEqual(104, Seat2_Player.CHIPS)
        self.assertEqual('Self', Seat2_Player.NAME)

    def test27(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(1529.91, Seat2_Player.CHIPS)

    def test28(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat2_Player)

    def test29(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat2_Player)

    def test30(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat2_Player)

    def test31(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat2_Player)

    def test32(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat2_Player)

    def test33(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat2_Player)

    def test34(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat2_Player)

    def test35(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(1585, Seat2_Player.CHIPS)

    def test36(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat2_Player.HAND)
        self.assertEqual(768, Seat2_Player.CHIPS)

    def test37(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat2_Player)

    def test38(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat2_Player)

    def test39(self):
        Seat2_Player = find_seat_2(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat2_Player)


class FindSeat3Test(unittest.TestCase):
    def test1(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat3_Player)

    def test2(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat3_Player)

    def test3(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test4(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test5(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test6(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test7(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test8(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test9(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test10(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test11(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test12(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test13(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test14(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test15(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test16(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test17(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test18(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test19(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test20(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test21(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(808, Seat3_Player.CHIPS)

    def test22(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(486, Seat3_Player.CHIPS)

    def test23(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(1162.03, Seat3_Player.CHIPS)

    def test24(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(1160.03, Seat3_Player.CHIPS)

    def test25(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(1114.03, Seat3_Player.CHIPS)

    def test26(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(1094.03, Seat3_Player.CHIPS)

    def test27(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(120, Seat3_Player.CHIPS)

    def test28(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat3_Player)

    def test29(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat3_Player)

    def test30(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat3_Player)

    def test31(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat3_Player)

    def test32(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat3_Player)

    def test33(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat3_Player)

    def test34(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual((('T', 'D'),('7', 'D')), Seat3_Player.HAND)
        self.assertEqual(84, Seat3_Player.CHIPS)
        self.assertEqual('Self', Seat3_Player.NAME)

    def test35(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(1513, Seat3_Player.CHIPS)

    def test36(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(1583, Seat3_Player.CHIPS)

    def test37(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(768, Seat3_Player.CHIPS)

    def test38(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(768, Seat3_Player.CHIPS)

    def test39(self):
        Seat3_Player = find_seat_3(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat3_Player.HAND)
        self.assertEqual(776, Seat3_Player.CHIPS)


class FindSeat4Test(unittest.TestCase):
    def test1(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual((('Q', 'C'),('8', 'S')), Seat4_Player.HAND)
        self.assertEqual(136, Seat4_Player.CHIPS)
        self.assertEqual('Self', Seat4_Player.NAME)

    def test2(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(334, Seat4_Player.CHIPS)

    def test3(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1495.27, Seat4_Player.CHIPS)

    def test4(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1491.27, Seat4_Player.CHIPS)

    def test5(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1491.27, Seat4_Player.CHIPS)

    def test6(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1491.27, Seat4_Player.CHIPS)

    def test7(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test8(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test9(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test10(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test11(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test12(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test13(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test14(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test15(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test16(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test17(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test18(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test19(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test20(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test21(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1487.27, Seat4_Player.CHIPS)

    def test22(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat4_Player)

    def test23(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat4_Player)

    def test24(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat4_Player)

    def test25(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat4_Player)

    def test26(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat4_Player)

    def test27(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1318, Seat4_Player.CHIPS)

    def test28(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat4_Player)

    def test29(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat4_Player)

    def test30(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat4_Player)

    def test31(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat4_Player)

    def test32(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat4_Player)

    def test33(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat4_Player)

    def test34(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat4_Player)

    def test35(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat4_Player)

    def test36(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1513, Seat4_Player.CHIPS)

    def test37(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1583, Seat4_Player.CHIPS)

    def test38(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1583, Seat4_Player.CHIPS)

    def test39(self):
        Seat4_Player = find_seat_4(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat4_Player.HAND)
        self.assertEqual(1571, Seat4_Player.CHIPS)


class FindSeat5Test(unittest.TestCase):
    def test1(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(574, Seat5_Player.CHIPS)

    def test2(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat5_Player)

    def test3(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(790, Seat5_Player.CHIPS)

    def test4(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(786, Seat5_Player.CHIPS)

    def test5(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(782, Seat5_Player.CHIPS)

    def test6(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(782, Seat5_Player.CHIPS)

    def test7(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(814, Seat5_Player.CHIPS)

    def test8(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(814, Seat5_Player.CHIPS)

    def test9(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(810, Seat5_Player.CHIPS)

    def test10(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(800, Seat5_Player.CHIPS)

    def test11(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(798, Seat5_Player.CHIPS)

    def test12(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(800, Seat5_Player.CHIPS)

    def test13(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(700, Seat5_Player.CHIPS)

    def test14(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(700, Seat5_Player.CHIPS)

    def test15(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(700, Seat5_Player.CHIPS)

    def test16(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(696, Seat5_Player.CHIPS)

    def test17(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(696, Seat5_Player.CHIPS)

    def test18(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(696, Seat5_Player.CHIPS)

    def test19(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(696, Seat5_Player.CHIPS)

    def test20(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(696, Seat5_Player.CHIPS)

    def test21(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(696, Seat5_Player.CHIPS)

    def test22(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(400, Seat5_Player.CHIPS)

    def test23(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(392, Seat5_Player.CHIPS)

    def test24(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(376, Seat5_Player.CHIPS)

    def test25(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(346, Seat5_Player.CHIPS)

    def test26(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(661, Seat5_Player.CHIPS)

    def test27(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(400, Seat5_Player.CHIPS)

    def test28(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(656, Seat5_Player.CHIPS)

    def test29(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(648, Seat5_Player.CHIPS)

    def test30(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(644, Seat5_Player.CHIPS)

    def test31(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(636, Seat5_Player.CHIPS)

    def test32(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(636, Seat5_Player.CHIPS)

    def test33(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat5_Player)

    def test34(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat5_Player)

    def test35(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual((('8', 'H'),('4', 'C')), Seat5_Player.HAND)
        self.assertEqual(84, Seat5_Player.CHIPS)
        self.assertEqual('Self', Seat5_Player.NAME)

    def test36(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat5_Player)

    def test37(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(1513, Seat5_Player.CHIPS)

    def test38(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(1513, Seat5_Player.CHIPS)

    def test39(self):
        Seat5_Player = find_seat_5(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat5_Player.HAND)
        self.assertEqual(1501, Seat5_Player.CHIPS)


class FindSeat6Test(unittest.TestCase):
    def test1(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat6_Player)

    def test2(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat6_Player)

    def test3(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(438, Seat6_Player.CHIPS)

    def test4(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(438, Seat6_Player.CHIPS)

    def test5(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(434, Seat6_Player.CHIPS)

    def test6(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(434, Seat6_Player.CHIPS)

    def test7(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(430, Seat6_Player.CHIPS)

    def test8(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(430, Seat6_Player.CHIPS)

    def test9(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(422, Seat6_Player.CHIPS)

    def test10(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(924, Seat6_Player.CHIPS)

    def test11(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(920, Seat6_Player.CHIPS)

    def test12(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(918, Seat6_Player.CHIPS)

    def test13(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(918, Seat6_Player.CHIPS)

    def test14(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(914, Seat6_Player.CHIPS)

    def test15(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(914, Seat6_Player.CHIPS)

    def test16(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(928, Seat6_Player.CHIPS)

    def test17(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(928, Seat6_Player.CHIPS)

    def test18(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(928, Seat6_Player.CHIPS)

    def test19(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(924, Seat6_Player.CHIPS)

    def test20(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(924, Seat6_Player.CHIPS)

    def test21(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(924, Seat6_Player.CHIPS)

    def test22(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat6_Player)

    def test23(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat6_Player)

    def test24(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat6_Player)

    def test25(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat6_Player)

    def test26(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat6_Player)

    def test27(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat6_Player)

    def test28(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(1611, Seat6_Player.CHIPS)

    def test29(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(1607, Seat6_Player.CHIPS)

    def test30(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(1603, Seat6_Player.CHIPS)

    def test31(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(1595, Seat6_Player.CHIPS)

    def test32(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(1595, Seat6_Player.CHIPS)

    def test33(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat6_Player.HAND)
        self.assertEqual(778, Seat6_Player.CHIPS)

    def test34(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat6_Player)

    def test35(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat6_Player)

    def test36(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual((('8', 'H'),('4', 'C')), Seat6_Player.HAND)
        self.assertEqual(80, Seat6_Player.CHIPS)
        self.assertEqual('Self', Seat6_Player.NAME)

    def test37(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat6_Player)

    def test38(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat6_Player)

    def test39(self):
        Seat6_Player = find_seat_6(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat6_Player)


class FindSeat7Test(unittest.TestCase):
    def test1(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat7_Player)

    def test2(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat7_Player)

    def test3(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(384, Seat7_Player.CHIPS)

    def test4(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(412, Seat7_Player.CHIPS)

    def test5(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(408, Seat7_Player.CHIPS)

    def test6(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(404, Seat7_Player.CHIPS)

    def test7(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(400, Seat7_Player.CHIPS)

    def test8(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(400, Seat7_Player.CHIPS)

    def test9(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(392, Seat7_Player.CHIPS)

    def test10(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(340, Seat7_Player.CHIPS)

    def test11(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(340, Seat7_Player.CHIPS)

    def test12(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(336, Seat7_Player.CHIPS)

    def test13(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(336, Seat7_Player.CHIPS)

    def test14(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(334, Seat7_Player.CHIPS)

    def test15(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(334, Seat7_Player.CHIPS)

    def test16(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(330, Seat7_Player.CHIPS)

    def test17(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(0, Seat7_Player.CHIPS)

    def test18(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(350, Seat7_Player.CHIPS)

    def test19(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(346, Seat7_Player.CHIPS)

    def test20(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(338, Seat7_Player.CHIPS)

    def test21(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(326, Seat7_Player.CHIPS)

    def test22(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat7_Player)

    def test23(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat7_Player)

    def test24(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat7_Player)

    def test25(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat7_Player)

    def test26(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat7_Player)

    def test27(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat7_Player)

    def test28(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(1553, Seat7_Player.CHIPS)

    def test29(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(1505, Seat7_Player.CHIPS)

    def test30(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(1589, Seat7_Player.CHIPS)

    def test31(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(1589, Seat7_Player.CHIPS)

    def test32(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(1589, Seat7_Player.CHIPS)

    def test33(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat7_Player.HAND)
        self.assertEqual(1591, Seat7_Player.CHIPS)

    def test34(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat7_Player)

    def test35(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat7_Player)

    def test36(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat7_Player)

    def test37(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual((('8', 'H'),('4', 'C')), Seat7_Player.HAND)
        self.assertEqual(80, Seat7_Player.CHIPS)
        self.assertEqual('Self', Seat7_Player.NAME)

    def test38(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual((('8', 'H'),('4', 'C')), Seat7_Player.HAND)
        self.assertEqual(80, Seat7_Player.CHIPS)
        self.assertEqual('Self', Seat7_Player.NAME)

    def test39(self):
        Seat7_Player = find_seat_7(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual((('8', 'D'),('Q', 'S')), Seat7_Player.HAND)
        self.assertEqual(90, Seat7_Player.CHIPS)
        self.assertEqual('Self', Seat7_Player.NAME)


class FindSeat8Test(unittest.TestCase):
    def test1(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat8_Player)

    def test2(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat8_Player)

    def test3(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual((('Q', 'C'),('8', 'D')), Seat8_Player.HAND)
        self.assertEqual(116, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test4(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual((('K', 'C'),('9', 'H')), Seat8_Player.HAND)
        self.assertEqual(112, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test5(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual((('T', 'H'),('5', 'H')), Seat8_Player.HAND)
        self.assertEqual(128, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test6(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual((('T', 'H'),('5', 'H')), Seat8_Player.HAND)
        self.assertEqual(126, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test7(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual((('6', 'H'),('Q', 'D')), Seat8_Player.HAND)
        self.assertEqual(126, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test8(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual((('6', 'H'),('Q', 'D')), Seat8_Player.HAND)
        self.assertEqual(122, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test9(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual((('2', 'C'),('9', 'C')), Seat8_Player.HAND)
        self.assertEqual(122, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test10(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual((('3', 'S'),('8', 'C')), Seat8_Player.HAND)
        self.assertEqual(122, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test11(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual((('3', 'S'),('8', 'C')), Seat8_Player.HAND)
        self.assertEqual(118, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test12(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual((('J', 'S'),('Q', 'D')), Seat8_Player.HAND)
        self.assertEqual(100, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test13(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual((('J', 'S'),('Q', 'D')), Seat8_Player.HAND)
        self.assertEqual(100, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test14(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual((('5', 'C'),('4', 'D')), Seat8_Player.HAND)
        self.assertEqual(238, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test15(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual((('5', 'C'),('4', 'D')), Seat8_Player.HAND)
        self.assertEqual(238, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test16(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual((('A', 'H'),('5', 'C')), Seat8_Player.HAND)
        self.assertEqual(236, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test17(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual((('A', 'H'),('5', 'C')), Seat8_Player.HAND)
        self.assertEqual(234, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test18(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual((('A', 'H'),('5', 'C')), Seat8_Player.HAND)
        self.assertEqual(234, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test19(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual((('K', 'S'),('7', 'S')), Seat8_Player.HAND)
        self.assertEqual(234, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test20(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual((('K', 'S'),('7', 'S')), Seat8_Player.HAND)
        self.assertEqual(230, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test21(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual((('K', 'S'),('7', 'S')), Seat8_Player.HAND)
        self.assertEqual(230, Seat8_Player.CHIPS)
        self.assertEqual('Self', Seat8_Player.NAME)

    def test22(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat8_Player)

    def test23(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat8_Player)

    def test24(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat8_Player)

    def test25(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat8_Player)

    def test26(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat8_Player)

    def test27(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat8_Player)

    def test28(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(None, Seat8_Player)

    def test29(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(None, Seat8_Player)

    def test30(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(None, Seat8_Player)

    def test31(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(None, Seat8_Player)

    def test32(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(None, Seat8_Player)

    def test33(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat8_Player.HAND)
        self.assertEqual(1489, Seat8_Player.CHIPS)

    def test34(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat8_Player.HAND)
        self.assertEqual(772, Seat8_Player.CHIPS)

    def test35(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat8_Player)

    def test36(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat8_Player)

    def test37(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat8_Player)

    def test38(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat8_Player)

    def test39(self):
        Seat8_Player = find_seat_8(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat8_Player)


class FindSeat9Test(unittest.TestCase):
    def test1(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(None, Seat9_Player)

    def test2(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(396, Seat9_Player.CHIPS)

    def test3(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1163.54, Seat9_Player.CHIPS)

    def test4(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1163.54, Seat9_Player.CHIPS)

    def test5(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1159.54, Seat9_Player.CHIPS)

    def test6(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1159.54, Seat9_Player.CHIPS)

    def test7(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1157.54, Seat9_Player.CHIPS)

    def test8(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1157.54, Seat9_Player.CHIPS)

    def test9(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1157.54, Seat9_Player.CHIPS)

    def test10(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1157.54, Seat9_Player.CHIPS)

    def test11(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1157.54, Seat9_Player.CHIPS)

    def test12(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1157.54, Seat9_Player.CHIPS)

    def test13(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1157.54, Seat9_Player.CHIPS)

    def test14(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1153.54, Seat9_Player.CHIPS)

    def test15(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1153.54, Seat9_Player.CHIPS)

    def test16(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1149.54, Seat9_Player.CHIPS)

    def test17(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1149.54, Seat9_Player.CHIPS)

    def test18(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1149.54, Seat9_Player.CHIPS)

    def test19(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1147.54, Seat9_Player.CHIPS)

    def test20(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1145.54, Seat9_Player.CHIPS)

    def test21(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1125.54, Seat9_Player.CHIPS)

    def test22(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(None, Seat9_Player)

    def test23(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(None, Seat9_Player)

    def test24(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(None, Seat9_Player)

    def test25(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(None, Seat9_Player)

    def test26(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(None, Seat9_Player)

    def test27(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1379.59, Seat9_Player.CHIPS)

    def test28(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual((('A', 'D'),('J', 'C')), Seat9_Player.HAND)
        self.assertEqual(112, Seat9_Player.CHIPS)
        self.assertEqual('Self', Seat9_Player.NAME)

    def test29(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual((('A', 'D'),('J', 'C')), Seat9_Player.HAND)
        self.assertEqual(104, Seat9_Player.CHIPS)
        self.assertEqual('Self', Seat9_Player.NAME)

    def test30(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual((('7', 'D'),('A', 'H')), Seat9_Player.HAND)
        self.assertEqual(102, Seat9_Player.CHIPS)
        self.assertEqual('Self', Seat9_Player.NAME)

    def test31(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual((('7', 'D'),('A', 'H')), Seat9_Player.HAND)
        self.assertEqual(92, Seat9_Player.CHIPS)
        self.assertEqual('Self', Seat9_Player.NAME)

    def test32(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual((('7', 'D'),('A', 'H')), Seat9_Player.HAND)
        self.assertEqual(92, Seat9_Player.CHIPS)
        self.assertEqual('Self', Seat9_Player.NAME)

    def test33(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(None, Seat9_Player)

    def test34(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(None, Seat9_Player.HAND)
        self.assertEqual(1587, Seat9_Player.CHIPS)

    def test35(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(None, Seat9_Player)

    def test36(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(None, Seat9_Player)

    def test37(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(None, Seat9_Player)

    def test38(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(None, Seat9_Player)

    def test39(self):
        Seat9_Player = find_seat_9(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(None, Seat9_Player)


class CallAmountTest(unittest.TestCase):
    def test1(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (1).png')
        self.assertEqual(12, call_amount)

    def test2(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (2).png')
        self.assertEqual(0, call_amount)

    def test3(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (3).png')
        self.assertEqual(12, call_amount)

    def test4(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (4).png')
        self.assertEqual(0, call_amount)

    def test5(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (5).png')
        self.assertEqual(2, call_amount)

    def test6(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (6).png')
        self.assertEqual(4, call_amount)

    def test7(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (7).png')
        self.assertEqual(4, call_amount)

    def test8(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (8).png')
        self.assertEqual(0, call_amount)

    def test9(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (9).png')
        self.assertEqual(8, call_amount)

    def test10(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (10).png')
        self.assertEqual(4, call_amount)

    def test11(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (11).png')
        self.assertEqual(4, call_amount)

    def test12(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (12).png')
        self.assertEqual(0, call_amount)

    def test13(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (13).png')
        self.assertEqual(100, call_amount)

    def test14(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (14).png')
        self.assertEqual(0, call_amount)

    def test15(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (15).png')
        self.assertEqual(0, call_amount)

    def test16(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (16).png')
        self.assertEqual(2, call_amount)

    def test17(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (17).png')
        self.assertEqual(234, call_amount)

    def test18(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (18).png')
        self.assertEqual(0, call_amount)

    def test19(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (19).png')
        self.assertEqual(4, call_amount)

    def test20(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (20).png')
        self.assertEqual(8, call_amount)

    def test21(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (21).png')
        self.assertEqual(0, call_amount)

    def test22(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (22).png')
        self.assertEqual(16, call_amount)

    def test23(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (23).png')
        self.assertEqual(4, call_amount)

    def test24(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (24).png')
        self.assertEqual(16, call_amount)

    def test25(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (25).png')
        self.assertEqual(0, call_amount)

    def test26(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (26).png')
        self.assertEqual(16, call_amount)

    def test27(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (27).png')
        self.assertEqual(0, call_amount)

    def test28(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (28).png')
        self.assertEqual(8, call_amount)

    def test29(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (29).png')
        self.assertEqual(48, call_amount)

    def test30(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (30).png')
        self.assertEqual(10, call_amount)

    def test31(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (31).png')
        self.assertEqual(0, call_amount)

    def test32(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (32).png')
        self.assertEqual(0, call_amount)

    def test33(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (33).png')
        self.assertEqual(4, call_amount)

    def test34(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (34).png')
        self.assertEqual(32, call_amount)

    def test35(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (35).png')
        self.assertEqual(4, call_amount)

    def test36(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (36).png')
        self.assertEqual(0, call_amount)

    def test37(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (37).png')
        self.assertEqual(0, call_amount)

    def test38(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (38).png')
        self.assertEqual(0, call_amount)

    def test39(self):
        call_amount = find_call_amount(r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (39).png')
        self.assertEqual(6, call_amount)


if __name__ == '__main__':
    unittest.main()