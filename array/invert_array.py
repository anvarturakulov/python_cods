def invert_array(a:list,n:int):
    """
        Обрашение массива (поворот задам наперед)
        в рамках индекса от {0} до {N-1}
    """
    for k in range(n//2):
        a[k], a[n-k-1] = a[n-k-1], a[k]

def test_invert_array():
    a1 = [1,2,3,4,5]
    print(a1)
    invert_array(a1,5)
    print(a1)
    if a1 == [5,4,3,2,1]:
        print("test 1 - OK")
    else:
        print("test 1 - Fail")

    a2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(a2)
    invert_array(a2, 8)
    print(a2)
    if a2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("test 2 - OK")
    else:
        print("test 2 - Fail")

test_invert_array()