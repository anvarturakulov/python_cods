
def hoar_sort_array(a:list):
    if len(a) <= 1:
        return
    barrier = a[0]

    left = []
    middle = []
    rigth = []
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            rigth.append(x)
    hoar_sort_array(left)
    hoar_sort_array(rigth)

    k = 0
    for x in left+middle+rigth:
        a[k] = x
        k   += 1

def test_hoar_sort_array():
    b =        [5,4,7,3,9,6,4,2,34,5,6,78]
    b_sorted = [2,3,4,4,5,5,6,6,7,9,34,78]
    hoar_sort_array(b)
    print("Test 1 is OK" if b == b_sorted else "Test 1 is Fail")

    b =        [1,2,3,4,5,6,7,8,1]
    b_sorted = [1,1,2,3,4,5,6,7,8]
    hoar_sort_array(b)
    print("Test 2 is OK" if b == b_sorted else "Test 2 is Fail")

    b =        [9,8,7,6,5,4,3,2,1]
    b_sorted = [1,2,3,4,5,6,7,8,9]
    hoar_sort_array(b)
    print("Test 3 is OK" if b == b_sorted else "Test 3 is Fail")

test_hoar_sort_array()