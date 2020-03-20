""" In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a
number. Given n, take the sum of the digits of n. If that
value has more than one digit, continue reducing in this
way until a single-digit number is produced. This is only
applicable to the natural numbers.
"""

def digital_root1(n:int):

    if len(str(n)) <= 1:
        return
    s = str(n)
    x = 0
    for i in s:
        x += int(i)
    digital_root1(x)


def digital_root(n):
    if len(str(n)) <= 1:
        return n
    s = str(n)

    while len(s) > 1:
        x = 0
        for i in s:
            x += int(i)
        s = str(x)

    return int(s)


def test_digital_root():

    print("Test 1 is Ok " if  digital_root(16) == 7 else "Test 1 is Fail")

    print("Test 2 is Ok " if digital_root(942) == 6 else "Test 2 is Fail")

    print("Test 3 is Ok " if digital_root(132189) == 6 else "Test 3 is Fail")

    print("Test 4 is Ok " if digital_root(493193) == 2 else "Test 4 is Fail")

test_digital_root()