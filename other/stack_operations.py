
_stack = []

def push(x):
    _stack.append(x)

def pop():
    if len(_stack)>0:
        return _stack.pop()

def clear():
    _stack.clear()

def is_empty():
    if len(_stack)>0:
        return False
    return True

def check_brackets_correct(s:str):
    """
    Проверка правильности поставки круглых и квадратных скобок

    >>> check_brackets_correct("asdff([()])")
    True
    >>> check_brackets_correct("asdff([()]])")
    False
    >>> check_brackets_correct("asdff[([()])]sasas")
    True
    """
    for bracket in s:
        if bracket not in "([)]":
            continue
        if bracket in "[(":
            push(bracket)
        else:
            assert bracket in ")]" , "Ожидалось закрывающая скобка "+str(bracket)
            if is_empty():
                return False
            left = pop()
            assert left in "([" , "Ожидалось открывающая скобка "+str(bracket)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if bracket != right:
                return False

    return is_empty()

def reverse_polish_notation(s:list):
    """ Алгоритм вычесления выражений в постфиксной нотации
    [5,2,+] == >> 5 +2 , [2,7,+,5,*] == >> (2+7)*5,
    [2,7,5,*,+] == >> 2+7*5
    >>> reverse_polish_notation([5,2,"+"])
    7
    >>> reverse_polish_notation([2,7,'+',5,'*'])
    45
    >>> reverse_polish_notation([2,7,5,'*','+'])
    37

    """
    if len(s) ==0: return 0

    for element in s:
        if not str(element).isdigit():
            if not is_empty():
                y = pop()
                x = pop()
                assert element in '+-*/', "Ожидалось операторы вычисления" + str(element)
                if   element == '+': push(x+y)
                elif element == '-': push(x-y)
                elif element == '/': push(x/y)
                else: push(x*y)
        else:
            push(element)
    if not is_empty():
        return pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

