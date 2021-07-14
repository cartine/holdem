def changecardsinhand(m1, m2):
    if m2 != 1:
        m2 -= 1
    elif m1 != 1:
        m1 -= 1
        m2 = m1
    else:
        raise Exception("If this program was written correctly, this wouldn't have happened.")
    return m1, m2


def four_of_a_kind(what_there_are_four_of, u1, u2, u3, u4, u5, count):
    m1 = 13
    m2 = 13
    while True:
        # if your cards are the same
        if m1 == what_there_are_four_of or m2 == what_there_are_four_of:
            if m1 != 1:
                m1, m2 = changecardsinhand(m1, m2)
            else:
                break
        else:
            print(count, '.   ', u1, u2, u3, u4, u5, '    ', m1, m2)
            count += 1
            if m1 != 1:
                m1, m2 = changecardsinhand(m1, m2)
            else:
                break

    return count


def three_of_a_kind(what_there_are_three_of, u1, u2, u3, u4, u5, count):
    m1 = 13
    m2 = 13
    while True:
        # if your cards are different
        if m1 != m2:
            print(count, '.   ', u1, u2, u3, u4, u5, '    ', m1, m2)
            count += 1
            if m1 != 1:
                m1, m2 = changecardsinhand(m1, m2)
            else:
                break
        # if your cards are the same
        else:
            # if your cards are the same as the three of a kind
            if m1 == what_there_are_three_of:
                if m1 != 1:
                    m1, m2 = changecardsinhand(m1, m2)
                else:
                    break
            # if your cards are different then the three of a kind
            else:
                print(count, '.   ', u1, u2, u3, u4, u5, '    ', m1, m2)
                count += 1
                if m1 != 1:
                    m1, m2 = changecardsinhand(m1, m2)
                else:
                    break
    return count


def thisisnotafunction():
    # This generates all possible hands of cards in the middle and
    # cards in your hand in which suits dont matter because there is less than three suits in the middle
    u1 = 13
    u2 = 13
    u3 = 13
    u4 = 13
    u5 = 13
    count = 0

    while True:
        # prevents five of a kind
        if u1 != u2 or u2 != u3 or u3 != u4 or u4 != u5:

            # if there is  four of a kind
            if (u1 == u2 and u2 == u3 and u3 == u4) or (u1 == u2 and u2 == u3 and u3 == u5) or (
                    u1 == u2 and u2 == u5 and u5 == u4) or (u1 == u5 and u5 == u3 and u3 == u4):
                count = four_of_a_kind(u1, u1, u2, u3, u4, u5, count)

            # if there is  four of a kind
            elif (u5 == u2 and u2 == u3 and u3 == u4):
                count = four_of_a_kind(u2, u1, u2, u3, u4, u5, count)



            # if there is a Three of a kind
            elif (u1 == u2 and u2 == u3) or (u1 == u2 and u2 == u4) or (u1 == u2 and u2 == u5) or (
                    u1 == u3 and u3 == u4) or (u1 == u3 and u3 == u5) or (u1 == u4 and u4 == u5):
                count = three_of_a_kind(u1, u1, u2, u3, u4, u5, count)

            # if there is a Three of a kind
            elif (u2 == u3 and u3 == u4) or (u2 == u3 and u3 == u5) or (u2 == u4 and u4 == u5):
                count = three_of_a_kind(u2, u1, u2, u3, u4, u5, count)

            # if there is a Three of a kind
            elif (u5 == u3 and u3 == u4):
                count = three_of_a_kind(u5, u1, u2, u3, u4, u5, count)

            # if there is less than a three of a kind
            else:
                m1 = 13
                m2 = 13
                while True:
                    print(count, '.   ', u1, u2, u3, u4, u5, '    ', m1, m2)
                    count += 1
                    if m1 != 1:
                        m1, m2 = changecardsinhand(m1, m2)
                    else:
                        break

        if u5 != 1:
            u5 = u5 - 1

        else:
            if u4 != 1:
                u4 = u4 - 1
                u5 = u4

            else:
                if u3 != 1:
                    u3 = u3 - 1
                    u4 = u3
                    u5 = u3

                else:
                    if u2 != 1:
                        u2 = u2 - 1
                        u3 = u2
                        u4 = u2
                        u5 = u2

                    else:
                        if u1 != 1:
                            u1 = u1 - 1
                            u2 = u1
                            u3 = u1
                            u4 = u1
                            u5 = u1

                        else:
                            break

    print(count)


if __name__ == '__main__':
    thisisnotafunction()