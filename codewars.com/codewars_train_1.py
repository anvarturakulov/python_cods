
#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b.
#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:
#array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    r = []
    for x in a:
        if x not in b:
            r.append(x)
    return r

ef test_array_diff():
    a = [14, -11, -4]
    b = [5, 5, 14, -17, 11, -4, 1, 2, 8]
    test_result = [-11]
    print(array_diff(a,b))
    print("Ok test 1" if array_diff(a,b)==test_result else "Fail test 1")

    a = [16, 14, 4, 5, -8, 13, 3, -5, 11, 12, -11, 5, 9, -5, 5, 5, 19]
    b = [-9, -17, -18, 13, -8, 18, 16, -9, -7, 6, 18, -14, 6, -5]
    test_result = [14, 4, 5, 3, 11, 12, -11, 5, 9, 5, 5, 19]
    print(array_diff(a, b))
    print("Ok test 2" if array_diff(a, b) == test_result else "Fail test 2")

    a = [-7, 17, -14, 10, -14, -20, -2, 11, -13]
    b = [-16, 14, 17, -10, -14, 7, -6, -9, -5, -1, 3, -6, 14, 14, 3, 8, 7]
    test_result = [-7, 10, -20, -2, 11, -13]
    print(array_diff(a, b))
    print("Ok test 3" if array_diff(a, b) == test_result else "Fail test 3")

test_array_diff()

