import cv2
import pytesseract
from matplotlib import pyplot as plt
from PeterPokerBot3 import *

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


def find_com_cards(filename):
    img = cv2.imread(filename)
    com_card1 = img[400:450, 560:620, :]
    com_card1_suit = img[480:530, 600:650, :]
    com_card2 = img[395:450, 675:730, :]
    com_card2_suit = img[480:530, 715:765, :]
    com_card3 = img[400:450, 790:860, :]
    com_card3_suit = img[480:530, 830:880, :]
    com_card4 = img[400:450, 910:980, :]
    com_card4_suit = img[481:531, 945:995, :]
    com_card5 = img[400:450, 1030:1090, :]
    com_card5_suit = img[481:531, 1060:1110, :]
    com_card1 = pytesseract.image_to_string(com_card1, config='--psm 6')[0]
    com_card1_suit = pytesseract.image_to_string(com_card1_suit, config='--psm 6')[0]
    com_card2 = pytesseract.image_to_string(com_card2, config='--psm 6')[0]
    com_card2_suit = pytesseract.image_to_string(com_card2_suit, config='--psm 6')[0]
    com_card3 = pytesseract.image_to_string(com_card3, config='--psm 6')[0]
    com_card3_suit = pytesseract.image_to_string(com_card3_suit, config='--psm 6')[0]
    com_card4 = pytesseract.image_to_string(com_card4, config='--psm 6')[0]
    com_card4_suit = pytesseract.image_to_string(com_card4_suit, config='--psm 6')[0]
    com_card5 = pytesseract.image_to_string(com_card5, config='--psm 6')[0]
    com_card5_suit = pytesseract.image_to_string(com_card5_suit, config='--psm 6')[0]
    com_cards = [com_card1, com_card2, com_card3, com_card4, com_card5]
    com_card_suits = [com_card1_suit, com_card2_suit, com_card3_suit, com_card4_suit, com_card5_suit]
    blank_cards = []
    for i in range(0, len(com_cards)):
        if com_cards[i] == '1':
            com_cards[i] = '10'
        if com_cards[i] == '10':
            com_cards[i] = 'T'
        if com_cards[i] == 'I':
            com_cards[i] = 'K'
        if com_cards[i] == '|':
            com_cards[i] = 'Q'
        if com_card_suits[i] == 'o':
            com_card_suits[i] = 'C'
        if com_card_suits[i] == 'j':
            com_card_suits[i] = 'C'
        if com_card_suits[i] == 'q':
            com_card_suits[i] = 'D'
        if com_card_suits[i] == '&':
            com_card_suits[i] = 'S'
        if com_card_suits[i] == 's':
            com_card_suits[i] = 'S'
        if com_card_suits[i] == 'X':
            com_card_suits[i] = 'H'
        if com_card_suits[i] == 'N':
            com_card_suits[i] = 'H'
    for i in range(0, len(com_cards)):
        if com_cards[i] == '\x0c' or com_card_suits[i] == '\x0c':
            blank_cards.insert(0, i)
    for i in blank_cards:
        del com_cards[i]
        del com_card_suits[i]
    com_cards2 = zip(com_cards, com_card_suits)
    return list(com_cards2)


def find_total_pot(filename):
    img = cv2.imread(filename)
    total_pot1 = img[325:349, 880:920, :]
    total_pot2 = img[303:335, 883:920, :]
    total_pot1 = pytesseract.image_to_string(total_pot1, config='--psm 6')[:-1]
    total_pot2 = pytesseract.image_to_string(total_pot2, config='--psm 6')[:-1]
    if total_pot2[:2] == '8\n':
        total_pot2 = 8
    if total_pot2 == '72)\n':
        total_pot2 = 28
    if total_pot1 == ':6—\n':
        total_pot1 = 6
    try:
        int(total_pot1)
    except:
        try:
            int(total_pot2)
        except:
            return 0
        else:
            return int(total_pot2)
    else:
        return int(total_pot1)


def find_dealer(filename):
    img = cv2.imread(filename)
    seat1 = img[210:230, 760:790, :]
    seat2 = img[210:230, 900:930, :]
    seat3 = img[319:339, 1250:1275, :]
    seat4 = img[568:588, 1280:1310, :]
    seat5 = img[635:655, 1040:1070, :]
    seat6 = img[658:678, 915:945, :]
    seat7 = img[635:655, 615:645, :]
    seat8 = img[569:589, 380:410, :]
    seat9 = img[319:340, 415:445, :]
    seat1 = pytesseract.image_to_string(seat1, config='--psm 6')[0]
    seat2 = pytesseract.image_to_string(seat2, config='--psm 6')[0]
    seat3 = pytesseract.image_to_string(seat3, config='--psm 6')[0]
    seat4 = pytesseract.image_to_string(seat4, config='--psm 6')[0]
    seat5 = pytesseract.image_to_string(seat5, config='--psm 6')[0]
    seat6 = pytesseract.image_to_string(seat6, config='--psm 6')[0]
    seat7 = pytesseract.image_to_string(seat7, config='--psm 6')[0]
    seat8 = pytesseract.image_to_string(seat8, config='--psm 6')[0]
    seat9 = pytesseract.image_to_string(seat9, config='--psm 6')[0]
    seats = [seat1, seat2, seat3, seat4, seat5, seat6, seat7, seat8, seat9]
    for i in range(0, len(seats)):
        if seats[i] == 'B':
            return i + 1


def find_call_amount(filename):
    img = cv2.imread(filename)
    call_amount = img[830:880, 940:990, :]
    all_in_amount = img[836:886, 1216:1266, :]
    call_amount = pytesseract.image_to_string(call_amount, config='--psm 8')[:-1]
    all_in_amount = pytesseract.image_to_string(all_in_amount, config='--psm 8')[:-1]
    if call_amount == '3 |\n':
        call_amount = 8
    if call_amount == 'La\n':
        call_amount = 4
    if call_amount == 'L2\n':
        call_amount = 2
    if call_amount == '6 |\n':
        call_amount = 6
    try:
        int(call_amount)
    except:
        call_amount = 0
        try:
            int(all_in_amount)
        except:
            return int(call_amount)
        else:
            return int(all_in_amount)
    else:
        int(call_amount)
    return int(call_amount)


def find_seat_1(filename):
    img = cv2.imread(filename)
    seat1 = img[78:288, 530:750, :]
    seat1_is_vacant = seat1[104:131, 72:149, :]
    seat1_is_vacant = pytesseract.image_to_string(seat1_is_vacant, config='--psm 8')[:-2]
    seat1_is_self = False
    if seat1_is_vacant == 'Vacant':
        seat1_is_vacant = True
    else:
        seat1_is_vacant = False
    if seat1_is_vacant is False:
        seat1_chips = seat1[110:150, 55:200, :]
        seat1_chips = pytesseract.image_to_string(seat1_chips, config='--psm 6')[:-2]
        is_float = seat1_chips.find('.')
        if is_float == -1:
            seat1_chips = int(seat1_chips.replace(',', ''))
        else:
            seat1_chips = float(seat1_chips.replace(',', ''))
        seat1_hole_card1 = seat1[18:54, 39:77, :]
        seat1_hole_card1 = pytesseract.image_to_string(seat1_hole_card1, config='--psm 6')[:-2]
        if seat1_hole_card1 != '':
            seat1_is_self = True
        seat1_hole_card1_suit = seat1[70:103, 58:103, :]
        seat1_hole_card1_suit = pytesseract.image_to_string(seat1_hole_card1_suit, config='--psm 6')[:-2]
        seat1_hole_card2 = seat1[17:51, 113:145, :]
        seat1_hole_card2 = pytesseract.image_to_string(seat1_hole_card2, config='--psm 6')[:-2]
        seat1_hole_card2_suit = seat1[70:103, 131:176, :]
        seat1_hole_card2_suit = pytesseract.image_to_string(seat1_hole_card2_suit, config='--psm 6')[:-2]
        if seat1_hole_card1 == '10':
            seat1_hole_card1 = 'T'
        if seat1_hole_card2 == '10':
            seat1_hole_card2 = 'T'
        if seat1_hole_card2 == 'Oo':
            seat1_hole_card2 = 'Q'
        if seat1_hole_card1_suit == 'cfo':
            seat1_hole_card1_suit = 'C'
        if seat1_hole_card1_suit == '. A':
            seat1_hole_card1_suit = 'D'
        if seat1_hole_card1_suit == '.':
            seat1_hole_card1_suit = 'H'
        if seat1_hole_card1_suit == '@':
            seat1_hole_card1_suit = 'S'
# |||||||||||||||||||||||||||||||||||||||||||||
        if seat1_hole_card2_suit == '. A':
            seat1_hole_card2_suit = 'D'
        if seat1_hole_card2_suit == '. J':
            seat1_hole_card2_suit = 'H'
        if seat1_hole_card2_suit == 'cfo':
            seat1_hole_card2_suit = 'C'
        if seat1_hole_card2_suit == '@':
            seat1_hole_card2_suit = 'S'
    if seat1_is_vacant is False:
        if seat1_is_self is True:
            Seat1_Player = CPUPlayer3(seat1_chips, "Self")
        else:
            Seat1_Player = Player(seat1_chips, "Seat 1")
    else:
        Seat1_Player = None
    if seat1_is_self is True:
        seat1_hand = (seat1_hole_card1, seat1_hole_card1_suit), (seat1_hole_card2, seat1_hole_card2_suit)
        Seat1_Player.HAND = seat1_hand
    return Seat1_Player


def find_seat_2(filename):
    img = cv2.imread(filename)
    seat2 = img[76:286, 940:1160, :]
    seat2_is_vacant = seat2[107:134, 73:150, :]
    seat2_is_vacant = pytesseract.image_to_string(seat2_is_vacant, config='--psm 8')[:-2]
    seat2_is_self = False
    if seat2_is_vacant == 'Vacant':
        seat2_is_vacant = True
    else:
        seat2_is_vacant = False
    if seat2_is_vacant is False:
        seat2_chips = seat2[111:151, 66:200, :]
        seat2_chips = pytesseract.image_to_string(seat2_chips, config='--psm 6')[:-2]
        is_float = seat2_chips.find('.')
        if is_float == -1:
            seat2_chips = int(seat2_chips.replace(',', ''))
        else:
            seat2_chips = float(seat2_chips.replace(',', ''))
        seat2_hole_card1 = seat2[18:55, 38:77, :]
        seat2_hole_card1 = pytesseract.image_to_string(seat2_hole_card1, config='--psm 6')[:-2]
        if seat2_hole_card1 != '':
            seat2_is_self = True
        seat2_hole_card1_suit = seat2[70:103, 58:103, :]
        seat2_hole_card1_suit = pytesseract.image_to_string(seat2_hole_card1_suit, config='--psm 6')[:-2]
        seat2_hole_card2 = seat2[21:55, 117:149, :]
        seat2_hole_card2 = pytesseract.image_to_string(seat2_hole_card2, config='--psm 6')[:-2]
        seat2_hole_card2_suit = seat2[67:100, 133:178, :]
        seat2_hole_card2_suit = pytesseract.image_to_string(seat2_hole_card2_suit, config='--psm 6')[:-2]
        if seat2_hole_card1 == '10':
            seat2_hole_card1 = 'T'
        if seat2_hole_card2 == '10':
            seat2_hole_card2 = 'T'
        if seat2_hole_card1_suit == 'oe':
            seat2_hole_card1_suit = 'C'
        if seat2_hole_card1_suit == 'ee':
            seat2_hole_card1_suit = 'C'
        if seat2_hole_card1_suit == '| J':
            seat2_hole_card1_suit = 'H'
        if seat2_hole_card1_suit == '@':
            seat2_hole_card1_suit = 'S'
        if seat2_hole_card1_suit == '.':
            seat2_hole_card1_suit = 'D'
# ||||||||||||||||||||||||||||||||||||||||||||
        if seat2_hole_card2_suit == 'ee':
            seat2_hole_card2_suit = 'C'
        if seat2_hole_card2_suit == '<>':
            seat2_hole_card2_suit = 'D'
        if seat2_hole_card2_suit == '(':
            seat2_hole_card2_suit = 'H'
        if seat2_hole_card2_suit == '@':
            seat2_hole_card2_suit = 'S'
    if seat2_is_vacant is False:
        if seat2_is_self is True:
            Seat2_Player = CPUPlayer3(seat2_chips, "Self")
        else:
            Seat2_Player = Player(seat2_chips, "Seat 2")
    else:
        Seat2_Player = None
    if seat2_is_self is True:
        seat2_hand = (seat2_hole_card1, seat2_hole_card1_suit), (seat2_hole_card2, seat2_hole_card2_suit)
        Seat2_Player.HAND = seat2_hand
    return Seat2_Player


def find_seat_3(filename):
    img = cv2.imread(filename)
    seat3 = img[190:400, 1287:1507, :]
    seat3_is_vacant = seat3[95:122, 72:149, :]
    seat3_is_vacant = pytesseract.image_to_string(seat3_is_vacant, config='--psm 8')[:-2]
    seat3_is_self = False
    if seat3_is_vacant == 'Vacant':
        seat3_is_vacant = True
    else:
        seat3_is_vacant = False
    if seat3_is_vacant is False:
        seat3_chips = seat3[110:150, 55:200, :]
        seat3_chips = pytesseract.image_to_string(seat3_chips, config='--psm 6')[:-2]
        is_float = seat3_chips.find('.')
        if is_float == -1:
            seat3_chips = int(seat3_chips.replace(',', ''))
        else:
            seat3_chips = float(seat3_chips.replace(',', ''))
        seat3_hole_card1 = seat3[18:54, 39:77, :]
        seat3_hole_card1 = pytesseract.image_to_string(seat3_hole_card1, config='--psm 6')[:-2]
        if seat3_hole_card1 != '':
            seat3_is_self = True
        seat3_hole_card1_suit = seat3[67:100, 58:103, :]
        seat3_hole_card1_suit = pytesseract.image_to_string(seat3_hole_card1_suit, config='--psm 6')[:-2]
        seat3_hole_card2 = seat3[17:51, 113:145, :]
        seat3_hole_card2 = pytesseract.image_to_string(seat3_hole_card2, config='--psm 6')[:-2]
        seat3_hole_card2_suit = seat3[67:100, 132:177, :]
        seat3_hole_card2_suit = pytesseract.image_to_string(seat3_hole_card2_suit, config='--psm 6')[:-2]
        if seat3_hole_card1 == '10':
            seat3_hole_card1 = 'T'
        if seat3_hole_card2 == '10':
            seat3_hole_card2 = 'T'
        if seat3_hole_card1_suit == '@':
            seat3_hole_card1_suit = 'S'
        if seat3_hole_card1_suit == '. A':
            seat3_hole_card1_suit = 'D'
        if seat3_hole_card1_suit == 'cfo':
            seat3_hole_card1_suit = 'C'
        if seat3_hole_card1_suit == '. J':
            seat3_hole_card1_suit = 'H'
# ||||||||||||||||||||||||||||||||||||||||||
        if seat3_hole_card2_suit == '@':
            seat3_hole_card2_suit = 'S'
        if seat3_hole_card2_suit == '. A':
            seat3_hole_card2_suit = 'D'
        if seat3_hole_card2_suit == 'cfo':
            seat3_hole_card2_suit = 'C'
        if seat3_hole_card2_suit == '. J':
            seat3_hole_card2_suit = 'H'
    if seat3_is_vacant is False:
        if seat3_is_self is True:
            Seat3_Player = CPUPlayer3(seat3_chips, "Self")
        else:
            Seat3_Player = Player(seat3_chips, "Seat 3")
    else:
        Seat3_Player = None
    if seat3_is_self is True:
        seat3_hand = (seat3_hole_card1, seat3_hole_card1_suit), (seat3_hole_card2, seat3_hole_card2_suit)
        Seat3_Player.HAND = seat3_hand
    return Seat3_Player


def find_seat_4(filename):
    img = cv2.imread(filename)
    seat4 = img[460:670, 1320:1540, :]
    seat4_is_vacant = seat4[104:131, 72:149, :]
    seat4_is_vacant = pytesseract.image_to_string(seat4_is_vacant, config='--psm 8')[:-2]
    seat4_is_self = False
    if seat4_is_vacant == 'Vacant':
        seat4_is_vacant = True
    else:
        seat4_is_vacant = False
    if seat4_is_vacant is False:
        seat4_chips = seat4[110:150, 55:200, :]
        seat4_chips = pytesseract.image_to_string(seat4_chips, config='--psm 6')[:-2]
        is_float = seat4_chips.find('.')
        if is_float == -1:
            seat4_chips = int(seat4_chips.replace(',', ''))
        else:
            seat4_chips = float(seat4_chips.replace(',', ''))
        seat4_hole_card1 = seat4[18:54, 39:77, :]
        seat4_hole_card1 = pytesseract.image_to_string(seat4_hole_card1, config='--psm 6')[:-2]
        if seat4_hole_card1 != '':
            seat4_is_self = True
        seat4_hole_card1_suit = seat4[70:103, 58:103, :]
        seat4_hole_card1_suit = pytesseract.image_to_string(seat4_hole_card1_suit, config='--psm 6')[:-2]
        seat4_hole_card2 = seat4[17:51, 113:145, :]
        seat4_hole_card2 = pytesseract.image_to_string(seat4_hole_card2, config='--psm 6')[:-2]
        seat4_hole_card2_suit = seat4[67:100, 133:178, :]
        seat4_hole_card2_suit = pytesseract.image_to_string(seat4_hole_card2_suit, config='--psm 6')[:-2]
        if seat4_hole_card1 == '10':
            seat4_hole_card1 = 'T'
        if seat4_hole_card2 == '10':
            seat4_hole_card2 = 'T'
        if seat4_hole_card2 == 'QO':
            seat4_hole_card2 = 'Q'
        if seat4_hole_card1_suit == 'ojo':
            seat4_hole_card1_suit = 'C'
        if seat4_hole_card1_suit == '.':
            seat4_hole_card1_suit = 'H'
        if seat4_hole_card1_suit == 'WwW':
            seat4_hole_card1_suit = 'D'
        if seat4_hole_card1_suit == '@':
            seat4_hole_card1_suit = 'S'
# ||||||||||||||||||||||||||||||||||||||||||||
        if seat4_hole_card2_suit == '@':
            seat4_hole_card2_suit = 'S'
        if seat4_hole_card2_suit == 'YY':
            seat4_hole_card2_suit = 'H'
        if seat4_hole_card2_suit == '~Y':
            seat4_hole_card2_suit = 'D'
        if seat4_hole_card2_suit == 'oe':
            seat4_hole_card2_suit = 'C'
    if seat4_is_vacant is False:
        if seat4_is_self is True:
            Seat4_Player = CPUPlayer3(seat4_chips, "Self")
        else:
            Seat4_Player = Player(seat4_chips, "Seat 4")
    else:
        Seat4_Player = None
    if seat4_is_self is True:
        seat4_hand = ((seat4_hole_card1, seat4_hole_card1_suit), (seat4_hole_card2, seat4_hole_card2_suit))
        Seat4_Player.HAND = seat4_hand
    return Seat4_Player


def find_seat_5(filename):
    img = cv2.imread(filename)
    seat5 = img[589:799, 1036:1256, :]
    seat5_is_vacant = seat5[104:131, 72:149, :]
    seat5_is_vacant = pytesseract.image_to_string(seat5_is_vacant, config='--psm 8')[:-2]
    seat5_is_self = False
    if seat5_is_vacant == 'Vacant':
        seat5_is_vacant = True
    else:
        seat5_is_vacant = False
    if seat5_is_vacant is False:
        seat5_chips = seat5[110:150, 55:200, :]
        seat5_chips = pytesseract.image_to_string(seat5_chips, config='--psm 6')[:-2]
        is_float = seat5_chips.find('.')
        if is_float == -1:
            seat5_chips = int(seat5_chips.replace(',', ''))
        else:
            seat5_chips = float(seat5_chips.replace(',', ''))
        seat5_hole_card1 = seat5[18:54, 39:77, :]
        seat5_hole_card1 = pytesseract.image_to_string(seat5_hole_card1, config='--psm 6')[:-2]
        try:
            int(face_cards(seat5_hole_card1))
        except:
            pass
        else:
            seat5_is_self = True
        seat5_hole_card1_suit = seat5[70:103, 58:103, :]
        seat5_hole_card1_suit = pytesseract.image_to_string(seat5_hole_card1_suit, config='--psm 6')[:-2]
        seat5_hole_card2 = seat5[17:51, 113:145, :]
        seat5_hole_card2 = pytesseract.image_to_string(seat5_hole_card2, config='--psm 6')[:-2]
        seat5_hole_card2_suit = seat5[70:103, 133:178, :]
        seat5_hole_card2_suit = pytesseract.image_to_string(seat5_hole_card2_suit, config='--psm 6')[:-2]
        if seat5_hole_card1 == '10':
            seat5_hole_card1 = 'T'
        if seat5_hole_card2 == '10':
            seat5_hole_card2 = 'T'
        if seat5_hole_card2 == 'Oo':
            seat5_hole_card2 = 'Q'
        if seat5_hole_card1_suit == '\\ a':
            seat5_hole_card1_suit = 'H'
        if seat5_hole_card1_suit == '_':
            seat5_hole_card1_suit = 'D'
        if seat5_hole_card1_suit == 'r J':
            seat5_hole_card1_suit = 'S'
        if seat5_hole_card1_suit == 'Cojo':
            seat5_hole_card1_suit = 'C'
# ||||||||||||||||||||||||||||||||||||||||||||||
        if seat5_hole_card2_suit == 'ofo':
            seat5_hole_card2_suit = 'C'
        if seat5_hole_card2_suit == 'OF':
            seat5_hole_card2_suit = 'H'
        if seat5_hole_card2_suit == 'a':
            seat5_hole_card2_suit = 'D'
        if seat5_hole_card2_suit == 'T J':
            seat5_hole_card2_suit = 'S'
    if seat5_is_vacant is False:
        if seat5_is_self is True:
            Seat5_Player = CPUPlayer3(seat5_chips, "Self")
        else:
            Seat5_Player = Player(seat5_chips, "Seat 5")
    else:
        Seat5_Player = None
    if seat5_is_self is True:
        seat5_hand = (seat5_hole_card1, seat5_hole_card1_suit), (seat5_hole_card2, seat5_hole_card2_suit)
        Seat5_Player.HAND = seat5_hand
    return Seat5_Player


def find_seat_6(filename):
    img = cv2.imread(filename)
    seat6 = img[610:820, 735:955, :]
    seat6_is_vacant = seat6[104:131, 72:149, :]
    seat6_is_vacant = pytesseract.image_to_string(seat6_is_vacant, config='--psm 8')[:-2]
    seat6_is_self = False
    if seat6_is_vacant == 'Vacant':
        seat6_is_vacant = True
    else:
        seat6_is_vacant = False
    if seat6_is_vacant is False:
        seat6_chips = seat6[110:150, 55:200, :]
        seat6_chips = pytesseract.image_to_string(seat6_chips, config='--psm 6')[:-2]
        is_float = seat6_chips.find('.')
        if is_float == -1:
            seat6_chips = int(seat6_chips.replace(',', ''))
        else:
            seat6_chips = float(seat6_chips.replace(',', ''))
        seat6_hole_card1 = seat6[18:54, 39:77, :]
        seat6_hole_card1 = pytesseract.image_to_string(seat6_hole_card1, config='--psm 6')[:-2]
        if seat6_hole_card1 != '':
            seat6_is_self = True
        seat6_hole_card1_suit = seat6[70:103, 58:103, :]
        seat6_hole_card1_suit = pytesseract.image_to_string(seat6_hole_card1_suit, config='--psm 6')[:-2]
        seat6_hole_card2 = seat6[17:51, 113:145, :]
        seat6_hole_card2 = pytesseract.image_to_string(seat6_hole_card2, config='--psm 6')[:-2]
        seat6_hole_card2_suit = seat6[67:100, 133:178, :]
        seat6_hole_card2_suit = pytesseract.image_to_string(seat6_hole_card2_suit, config='--psm 6')[:-2]
        if seat6_hole_card1 == '10':
            seat6_hole_card1 = 'T'
        if seat6_hole_card2 == '10':
            seat6_hole_card2 = 'T'
        if seat6_hole_card2 == 'Oo':
            seat6_hole_card2 = 'Q'
        if seat6_hole_card1_suit == '. 4':
            seat6_hole_card1_suit = 'H'
        if seat6_hole_card1_suit == '~ 4':
            seat6_hole_card1_suit = 'D'
        if seat6_hole_card1_suit == '@':
            seat6_hole_card1_suit = 'S'
        if seat6_hole_card1_suit == 'cfo':
            seat6_hole_card1_suit = 'C'
# |||||||||||||||||||||||||||||||||||||||||||||
        if seat6_hole_card2_suit == 'ae':
            seat6_hole_card2_suit = 'C'
        if seat6_hole_card2_suit == '~q':
            seat6_hole_card2_suit = 'D'
        if seat6_hole_card2_suit == 'oI':
            seat6_hole_card2_suit = 'H'
        if seat6_hole_card2_suit == '@':
            seat6_hole_card2_suit = 'S'
    if seat6_is_vacant is False:
        if seat6_is_self is True:
            Seat6_Player = CPUPlayer3(seat6_chips, "Self")
        else:
            Seat6_Player = Player(seat6_chips, "Seat 6")
    else:
        Seat6_Player = None
    if seat6_is_self is True:
        seat6_hand = (seat6_hole_card1, seat6_hole_card1_suit), (seat6_hole_card2, seat6_hole_card2_suit)
        Seat6_Player.HAND = seat6_hand
    return Seat6_Player


def find_seat_7(filename):
    img = cv2.imread(filename)
    seat7 = img[589:799, 433:653, :]
    seat7_is_vacant = seat7[104:131, 72:149, :]
    seat7_is_vacant = pytesseract.image_to_string(seat7_is_vacant, config='--psm 8')[:-2]
    seat7_is_self = False
    if seat7_is_vacant == 'Vacant':
        seat7_is_vacant = True
    else:
        seat7_is_vacant = False
    if seat7_is_vacant is False:
        seat7_chips = seat7[110:150, 55:200, :]
        seat7_chips = pytesseract.image_to_string(seat7_chips, config='--psm 6')[:-2]
        is_float = seat7_chips.find('.')
        if is_float == -1:
            seat7_chips = int(seat7_chips.replace(',', ''))
        else:
            seat7_chips = float(seat7_chips.replace(',', ''))
        seat7_hole_card1 = seat7[18:54, 39:77, :]
        seat7_hole_card1 = pytesseract.image_to_string(seat7_hole_card1, config='--psm 6')[:-2]
        try:
            int(face_cards(seat7_hole_card1))
        except:
            pass
        else:
            seat7_is_self = True
        seat7_hole_card1_suit = seat7[70:103, 58:103, :]
        seat7_hole_card1_suit = pytesseract.image_to_string(seat7_hole_card1_suit, config='--psm 6')[:-2]
        seat7_hole_card2 = seat7[20:54, 116:148, :]
        seat7_hole_card2 = pytesseract.image_to_string(seat7_hole_card2, config='--psm 6')[:-2]
        seat7_hole_card2_suit = seat7[67:100, 133:178, :]
        seat7_hole_card2_suit = pytesseract.image_to_string(seat7_hole_card2_suit, config='--psm 6')[:-2]
        if seat7_hole_card1 == '10':
            seat7_hole_card1 = 'T'
        if seat7_hole_card2 == '10':
            seat7_hole_card2 = 'T'
        if seat7_hole_card1_suit == '. 4':
            seat7_hole_card1_suit = 'H'
        if seat7_hole_card1_suit == '~ 4':
            seat7_hole_card1_suit = 'D'
        if seat7_hole_card1_suit == 'cfo':
            seat7_hole_card1_suit = 'C'
        if seat7_hole_card1_suit == '@':
            seat7_hole_card1_suit = 'S'
# |||||||||||||||||||||||||||||||||||||||||||||||
        if seat7_hole_card2_suit == 'ee':
            seat7_hole_card2_suit = 'C'
        if seat7_hole_card2_suit == '@':
            seat7_hole_card2_suit = 'S'
        if seat7_hole_card2_suit == '~}':
            seat7_hole_card2_suit = 'D'
        if seat7_hole_card2_suit == 'Y':
            seat7_hole_card2_suit = 'H'
    if seat7_is_vacant is False:
        if seat7_is_self is True:
            Seat7_Player = CPUPlayer3(seat7_chips, "Self")
        else:
            Seat7_Player = Player(seat7_chips, "Seat 7")
    else:
        Seat7_Player = None
    if seat7_is_self is True:
        seat7_hand = (seat7_hole_card1, seat7_hole_card1_suit), (seat7_hole_card2, seat7_hole_card2_suit)
        Seat7_Player.HAND = seat7_hand
    return Seat7_Player


def find_seat_8(filename):
    img = cv2.imread(filename)
    seat8 = img[459:669, 149:369, :]
    seat8_is_vacant = seat8[104:131, 72:149, :]
    seat8_is_vacant = pytesseract.image_to_string(seat8_is_vacant, config='--psm 8')[:-2]
    seat8_is_self = False
    if seat8_is_vacant == 'Vacant':
        seat8_is_vacant = True
    else:
        seat8_is_vacant = False
    if seat8_is_vacant is False:
        seat8_chips = seat8[110:150, 55:200, :]
        seat8_chips = pytesseract.image_to_string(seat8_chips, config='--psm 6')[:-2]
        is_float = seat8_chips.find('.')
        if is_float == -1:
            seat8_chips = int(seat8_chips.replace(',', ''))
        else:
            seat8_chips = float(seat8_chips.replace(',', ''))
        seat8_hole_card1 = seat8[18:54, 39:77, :]
        seat8_hole_card1 = pytesseract.image_to_string(seat8_hole_card1, config='--psm 6')[:-2]
        if seat8_hole_card1 != '':
            seat8_is_self = True
        seat8_hole_card1_suit = seat8[70:103, 58:103, :]
        seat8_hole_card1_suit = pytesseract.image_to_string(seat8_hole_card1_suit, config='--psm 6')[:-2]
        seat8_hole_card2 = seat8[19:54, 114:150, :]
        seat8_hole_card2 = pytesseract.image_to_string(seat8_hole_card2, config='--psm 6')[:-2]
        seat8_hole_card2_suit = seat8[70:103, 131:176, :]
        seat8_hole_card2_suit = pytesseract.image_to_string(seat8_hole_card2_suit, config='--psm 6')[:-2]
        if seat8_hole_card1 == '10':
            seat8_hole_card1 = 'T'
        if seat8_hole_card2 == '10':
            seat8_hole_card2 = 'T'
        if seat8_hole_card1_suit == '@':
            seat8_hole_card1_suit = 'S'
        if seat8_hole_card1_suit == 'cfo':
            seat8_hole_card1_suit = 'C'
        if seat8_hole_card1_suit == '. 4':
            seat8_hole_card1_suit = 'H'
        if seat8_hole_card1_suit == '. A':
            seat8_hole_card1_suit = 'H'
        if seat8_hole_card1_suit == '~ 4':
            seat8_hole_card1_suit = 'D'
# ||||||||||||||||||||||||||||||||||||||||||||||
        if seat8_hole_card2_suit == '@':
            seat8_hole_card2_suit = 'S'
        if seat8_hole_card2_suit == 'cfo':
            seat8_hole_card2_suit = 'C'
        if seat8_hole_card2_suit == '~ 4':
            seat8_hole_card2_suit = 'D'
        if seat8_hole_card2_suit == '. 4':
            seat8_hole_card2_suit = 'H'
    if seat8_is_vacant is False:
        if seat8_is_self is True:
            Seat8_Player = CPUPlayer3(seat8_chips, "Self")
        else:
            Seat8_Player = Player(seat8_chips, "Seat 8")
    else:
        Seat8_Player = None
    if seat8_is_self is True:
        seat8_hand = (seat8_hole_card1, seat8_hole_card1_suit), (seat8_hole_card2, seat8_hole_card2_suit)
        Seat8_Player.HAND = seat8_hand
    return Seat8_Player


def find_seat_9(filename):
    img = cv2.imread(filename)
    seat9 = img[187:397, 185:405, :]
    seat9_is_vacant = seat9[104:131, 72:149, :]
    seat9_is_vacant = pytesseract.image_to_string(seat9_is_vacant, config='--psm 8')[:-2]
    seat9_is_self = False
    if seat9_is_vacant == 'Vacant':
        seat9_is_vacant = True
    else:
        seat9_is_vacant = False
    if seat9_is_vacant is False:
        seat9_chips = seat9[110:150, 55:200, :]
        seat9_chips = pytesseract.image_to_string(seat9_chips, config='--psm 6')[:-2]
        is_float = seat9_chips.find('.')
        if is_float == -1:
            seat9_chips = int(seat9_chips.replace(',', ''))
        else:
            seat9_chips = float(seat9_chips.replace(',', ''))
        seat9_hole_card1 = seat9[18:54, 39:77, :]
        seat9_hole_card1 = pytesseract.image_to_string(seat9_hole_card1, config='--psm 6')[:-2]
        if seat9_hole_card1 != '':
            seat9_is_self = True
        seat9_hole_card1_suit = seat9[70:103, 58:103, :]
        seat9_hole_card1_suit = pytesseract.image_to_string(seat9_hole_card1_suit, config='--psm 6')[:-2]
        seat9_hole_card2 = seat9[17:51, 113:145, :]
        seat9_hole_card2 = pytesseract.image_to_string(seat9_hole_card2, config='--psm 6')[:-2]
        seat9_hole_card2_suit = seat9[67:100, 133:178, :]
        seat9_hole_card2_suit = pytesseract.image_to_string(seat9_hole_card2_suit, config='--psm 6')[:-2]
        if seat9_hole_card1 == '10':
            seat9_hole_card1 = 'T'
        if seat9_hole_card2 == '10':
            seat9_hole_card2 = 'T'
        if seat9_hole_card1_suit == '. a':
            seat9_hole_card1_suit = 'D'
        if seat9_hole_card1_suit == '.':
            seat9_hole_card1_suit = 'H'
        if seat9_hole_card1_suit == 'r J':
            seat9_hole_card1_suit = 'S'
        if seat9_hole_card1_suit == 'cfo':
            seat9_hole_card1_suit = 'C'
# ||||||||||||||||||||||||||||||||||||||||||||||
        if seat9_hole_card2_suit == '~Y':
            seat9_hole_card2_suit = 'H'
        if seat9_hole_card2_suit == 'oe':
            seat9_hole_card2_suit = 'C'
        if seat9_hole_card2_suit == '~':
            seat9_hole_card2_suit = 'D'
        if seat9_hole_card2_suit == '@':
            seat9_hole_card2_suit = 'S'
    if seat9_is_vacant is False:
        if seat9_is_self is True:
            Seat9_Player = CPUPlayer3(seat9_chips, "Self")
        else:
            Seat9_Player = Player(seat9_chips, "Seat 9")
    else:
        Seat9_Player = None
    if seat9_is_self is True:
        seat9_hand = (seat9_hole_card1, seat9_hole_card1_suit), (seat9_hole_card2, seat9_hole_card2_suit)
        Seat9_Player.HAND = seat9_hand
    return Seat9_Player


def creating_seats(filename):
    dealer_index = find_dealer(filename)
    seats = [find_seat_1(filename), find_seat_2(filename), find_seat_3(filename), find_seat_4(filename),
             find_seat_5(filename), find_seat_6(filename), find_seat_7(filename), find_seat_8(filename),
             find_seat_9(filename)]
    seats_ordered = seats[dealer_index:]
    seats_ordered = seats_ordered + seats[:dealer_index]
    empty_seats = seats_ordered.count(None)
    for i in range(0, empty_seats):
        seats_ordered.remove(None)
    for i in range(0, len(seats_ordered)):
        if seats_ordered[i].NAME == 'Self':
            self_index = i
            self_chips = seats_ordered[i].CHIPS
            self_hand = seats_ordered[i].HAND
    seats_ordered = [Seat(player) for player in seats_ordered]
    return seats_ordered, self_index, self_chips, self_hand


filename = r'C:\Users\peter\OneDrive\Pictures\Screenshots\Screenshot (160).png'
if __name__ == '__main__':
    print(find_seat_6(filename))