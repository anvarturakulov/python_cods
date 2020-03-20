def array_transfer_element(a:list,n:int,side="left"):
    """
        Сдвиг элементов N мерного массива А
        по навравлениею на лево или на право
        направление сдвига определяется параметром
        side. Если параметр side равно 'left' сдвиг
        происходит на лево и иначе при значение 'right'
        на право

    """
    temp1 = 0;
    if side =="left":
        for k in range(n-1):
            if k == 0:
                temp1 = a[k]
            a[k] = a[k+1]
        a[n-1] = temp1
    else:
        for k in range(n-1,0,-1):
            if k == n-1:
                temp1 = a[k]
            a[k] = a[k-1]
        a[0] = temp1



def test_array_transfer_element():
    a1 = [0,1,2,3,4]
    array_transfer_element(a1,5,"left")
    if a1 == [1,2,3,4,0]:
        print("Test 1 is Ok")
    else:
        print("Test 1 is Fail")

    a2 = [0,1,2,3,4]
    array_transfer_element(a2,5,"right")
    if a2 == [4, 0, 1, 2, 3]:
        print("Test 2 is Ok")
    else:
        print("Test 2 is Fail")

test_array_transfer_element()
