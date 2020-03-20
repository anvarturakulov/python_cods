""" The new "Avengers" movie has just been released! There are a
lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers"
ticket costs 25 dollars.

Vasya is currently working as a clerk.He wants to sell a ticket to every
single person in this line.

Can Vasya sell a ticket to every person and give change if he initially
has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give
change with the bills he has at hand at that moment. Otherwise return NO.
Examples:"""
def check(ss,p):
    if (p == 50) and (ss[0]>0):
        return True
    elif (p == 100) and (ss[0]>0):
        if (ss[0]>=3) or ((ss[0]+ss[1]>=2) and (ss[1]>=1)):
            return True
    elif p == 25:
        return True
    return False

def del_change_element(ss,p):
    if p == 50:
        ss[0] -= 1
    elif p == 100:
        if  ss[1] >= 1:
            ss[1] -= 1
            ss[0] -= 1
        elif ss[0] < 3 :
            print("Fail - ",ss[0])
        else:
            ss[0] -= 3

def new_element(ss,p):
    if p == 25:
        ss[0] += 1
    elif p == 50:
        ss[1] += 1
    else:
        ss[2] += 1



def tickets(people):
    ss = [0] * 3
    print(people)
    for p in people:
        if check(ss,p):
            new_element(ss,p)
            #print(ss)
            del_change_element(ss,p)
            #print(ss)
        else:
            return 'NO'
    return 'YES'

def test_tickets():
    t = [25, 25, 50]
    print(tickets(t))

    t = [25, 100]
    print(tickets(t))

    t = [25, 25, 50, 50, 100]
    print(tickets(t))

    t = [25,50]
    print(tickets(t))

    t = [25, 25, 25, 25, 50, 100, 50]
    print(tickets(t))

    t = [25, 25, 100]
    print(tickets(t))


test_tickets()

