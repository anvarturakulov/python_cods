def insert_sort(a):
    """  Сортировка списка а вставками """
    n = len(a)
    for top in range(1,n):
        k = top
        while k > 0 and a[k] < a[k-1]:
            a[k], a[k-1] = a[k-1], a[k] #  a = [4, 2 , 5, 1, 3]
            k -= 1

def choise_sort(a):
    """ сортировка списка а выбором """
    n = len(a)
    for pos in range(n-1):
        for k in range(pos +1, n):
            if a[k] < a[pos]:
                a[pos] , a[k] = a[k], a[pos]

def buble_sort(a):
    """ сортировка списка а методом пузирька"""
    n = len(a)
    for bypass in range(1,n):
        for k in range(0, n-bypass):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]

def count_sort(a):
    """ сортировка списка методом подсчета"""
    f = [0]*10
    for x in a:
        f[x] += 1
    a = []
    for k in range(len(f)):
        for i in range(0,f[k]):
            a.append(k)
    return a

def test_sort(sort_algoritm):
    print("Тестируем: ",sort_algoritm.__doc__)
    print("test case #1 ,", end="")
    a = [4, 2 , 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algoritm(a)
    print("Ok" if a == a_sorted else "Fail")

    print("test case #2 ,", end="")
    a = list(range(10,20))+list(range(0,10))
    a_sorted = list(range(20))
    sort_algoritm(a)
    print("Ok" if a == a_sorted else "Fail")

    print("test case #3 ,", end="")
    a = [4, 2 , 2, 1, 3]
    a_sorted = [1, 2, 2, 3, 4]
    sort_algoritm(a)
    print("Ok" if a == a_sorted else "Fail")


def test_sort_count(sort_algoritm):
    print("Тестируем: ", sort_algoritm.__doc__)
    print("test case #4 ,", end="")
    a = [8,9,2,4,7,6,5,1,4,7,9,5,5,5,8,7,9,7,5,1,2,4,4,5,4,8]
    a_sorted = [1,1,2,2,4,4,4,4,4,5,5,5,5,5,5,6,7,7,7,7,8,8,8,9,9,9]
    a = sort_algoritm(a)
    print("Ok" if a == a_sorted else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(buble_sort)
    test_sort_count(count_sort)

