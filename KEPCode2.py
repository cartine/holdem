# This generates all possible hands of cards in the middle and
# cards in your hand in which suits dont matter because there is less than three suits in the middle
u1 = 13
u2 = 13
u3 = 13
u4 = 13
u5 = 13
m1 = 13
m2 = 13
count = 0

while True:
    # prevents five of a kind
    if u1 != u2 or u2 != u3 or u3 != u4 or u4 != u5:
        m1 = 13
        m2 = 13

        # if there is  four of a kind
        if (u1 == u2 and u2 == u3 and u3 == u4) or (u1 == u2 and u2 == u3 and u3 == u5) or (
                u1 == u2 and u2 == u5 and u5 == u4) or (u1 == u5 and u5 == u3 and u3 == u4):
            while True:
                # if your cards are the same
                if m1 == u1 or m2 == u1:
                    if m2 != 1:
                        m2 -= 1
                    elif m1 != 1:
                        m1 -= 1
                        m2 = m1
                    else:
                        break
                else:
                    print(u1, u2, u3, u4, u5, '    ', m1, m2)
                    count += 1
                    if m2 != 1:
                        m2 -= 1
                    elif m1 != 1:
                        m1 -= 1
                        m2 = m1
                    else:
                        break

        # if there is  four of a kind
        elif (u5 == u2 and u2 == u3 and u3 == u4):
            while True:
                # if your cards are the same
                if m1 == u5 or m2 == u5:
                    if m2 != 1:
                        m2 -= 1
                    elif m1 != 1:
                        m1 -= 1
                        m2 = m1
                    else:
                        break
                else:
                    print(u1, u2, u3, u4, u5, '    ', m1, m2)
                    count += 1
                    if m2 != 1:
                        m2 -= 1
                    elif m1 != 1:
                        m1 -= 1
                        m2 = m1
                    else:
                        break



        # if there is a Three of a kind
        elif (u1 == u2 and u2 == u3) or (u1 == u2 and u2 == u4) or (u1 == u2 and u2 == u5) or (
                u1 == u3 and u3 == u4) or (u1 == u3 and u3 == u5) or (u1 == u4 and u4 == u5):
            while True:
                # if your cards are different
                if m1 != m2:
                    print(u1, u2, u3, u4, u5, '    ', m1, m2)
                    count += 1
                    if m2 != 1:
                        m2 -= 1
                    elif m1 != 1:
                        m1 -= 1
                        m2 = m1
                    else:
                        break
                # if your cards are the same
                else:
                    # if your cards are the same as the three of a kind
                    if m1 == u1:
                        if m2 != 1:
                            m2 -= 1
                        elif m1 != 1:
                            m1 -= 1
                            m2 = m1
                        else:
                            break
                    # if your cards are different then the three of a kind
                    else:
                        print(u1, u2, u3, u4, u5, '    ', m1, m2)
                        count += 1
                        if m2 != 1:
                            m2 -= 1
                        elif m1 != 1:
                            m1 -= 1
                            m2 = m1
                        else:
                            break

        # if there is a Three of a kind
        elif (u2 == u3 and u3 == u4) or (u2 == u3 and u3 == u5) or (u2 == u4 and u4 == u5):
            while True:
                # if your cards are different
                if m1 != m2:
                    print(u1, u2, u3, u4, u5, '    ', m1, m2)
                    count += 1
                    if m2 != 1:
                        m2 -= 1
                    elif m1 != 1:
                        m1 -= 1
                        m2 = m1
                    else:
                        break
                # if your cards are the same
                else:
                    # if your cards are the same as the three of a kind
                    if m1 == u2:
                        if m2 != 1:
                            m2 -= 1
                        elif m1 != 1:
                            m1 -= 1
                            m2 = m1
                        else:
                            break
                    # if your cards are different then the three of a kind
                    else:
                        print(u1, u2, u3, u4, u5, '    ', m1, m2)
                        count += 1
                        if m2 != 1:
                            m2 -= 1
                        elif m1 != 1:
                            m1 -= 1
                            m2 = m1
                        else:
                            break

        # if there is a Three of a kind
        elif (u5 == u3 and u3 == u4):
            while True:
                # if your cards are different
                if m1 != m2:
                    print(u1, u2, u3, u4, u5, '    ', m1, m2)
                    count += 1
                    if m2 != 1:
                        m2 -= 1
                    elif m1 != 1:
                        m1 -= 1
                        m2 = m1
                    else:
                        break
                # if your cards are the same
                else:
                    # if your cards are the same as the three of a kind
                    if m1 == u5:
                        if m2 != 1:
                            m2 -= 1
                        elif m1 != 1:
                            m1 -= 1
                            m2 = m1
                        else:
                            break
                    # if your cards are different then the three of a kind
                    else:
                        print(u1, u2, u3, u4, u5, '    ', m1, m2)
                        count += 1
                        if m2 != 1:
                            m2 -= 1
                        elif m1 != 1:
                            m1 -= 1
                            m2 = m1
                        else:
                            break

        # if there is less than a three of a kind
        else:
            while True:
                print(u1, u2, u3, u4, u5, '    ', m1, m2)
                count += 1
                if m1 == 1:
                    break
                elif m2 != 1:
                    m2 -= 1
                else:
                    m1 -= 1
                    m2 = m1

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
