def check_sort_array(a,ascending=True):
    """ Проверка отсортированности списка"""
    s = 2*int(ascending)-1
    for top in range(1,len(a)):
        if not(s*a[top] > s*a[top-1]):
            return False
    return True

def test_check_array():
    b = [1,4,6,7,8,9,1]
    print("Test  is OK" if check_sort_array(b,True) == False else "Test is Fail")

    b = [1,4,6,7,8,9]
    print("Test  is OK" if check_sort_array(b,True) else "Test is Fail")

    b = [8,7,6,5,4,3]
    print("Test  is OK" if check_sort_array(b, False) else "Test is Fail")

test_check_array()