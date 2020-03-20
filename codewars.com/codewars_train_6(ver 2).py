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

def tickets(people):
    n25=n50=n100=0
    for k in people:
        if      k==25:              n25+=1
        elif    k==50:              n25-=1
        elif    k==100 and n50>0:   n25-=1; n50-=1
        elif    k==100 and n50==0:  n25-=3

        if n25<0 or n50<0:
            return 'NO'
    return 'YES'