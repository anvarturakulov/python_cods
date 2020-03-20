""" Your task is to make a function
that can take any non-negative integer
as a argument and return it with its
digits in descending order. Essentially,
rearrange the digits to create the highest
possible number."""
def sort(s):
    l = len(s)
    for pos in range(l-1):
        for k in range(pos+1,l):
            if s[k] > s[pos]:
                s[k], s[pos] = s[pos], s[k]
    ss = ""
    for x in s:
        ss = ss + x
    return int(ss)

def descending_order(num):
    # Bust a move right here
    return sort(list(str(num)))

def test_descending_order():
    n = 21445
    n_test = 54421
    print("Test 1 is OK " if n_test == descending_order(n) else "Test 1 is Fail")

    n = 145263
    n_test = 654321
    print("Test 2 is OK " if n_test == descending_order(n) else "Test 2 is Fail")

    n = 145263
    n_test = 654321
    print("Test 3 is OK " if n_test == descending_order(n) else "Test 3 is Fail")

test_descending_order()

