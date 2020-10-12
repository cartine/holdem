import random


if __name__ == '__main__':
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
    hands = random.sample(deck, 10)
    hand_1 = hands[:5]
    hand_2 = hands[5:]
    print(hand_1)
    print(hand_2)