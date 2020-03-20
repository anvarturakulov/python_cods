def array_search(a: list, n: int, x: int):
    """
        Осуществаляет поиск числа {х} в массиве {а}
        от {0} до {n-1} индекса включительно.
        возвращает индекс элимента {х} в массиве {а}
        или -1, если такого нет
        Если в массиве несколько одинаковых элементов
        равных {х}, то вернуть первый индекс по счету
    """
    for k in range(5):
        if a[k] == x:
            return k
    return -1


def test_array_search():
    a1 = [1,2,3,4,5]
    m = array_search(a1,5,8)
    if m == -1:
        print("test 1 - OK")
    else:
        print("test 1 - Fail")

    a2 = [1,4,7,9,10]
    m = array_search(a2,5,4)
    if m == -1:
        print("test 1 - Fail")
    else:
        print("test 1 - Ok")

    a3 = [10, 20, 30, 10, 10]
    m = array_search(a3, 5, 10)
    if m == -1:
        print("test 1 - Fail")
    else:
        print("test 1 - Ok")

test_array_search()


