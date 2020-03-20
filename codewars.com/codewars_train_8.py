"""This time we want to write calculations using functions
    and get the results. Let's have a look at some examples:
    seven(times(five())) # must return 35
    four(plus(nine())) # must return 13
    eight(minus(three())) # must return 5
    six(divided_by(two())) # must return 3 """



def operation(obj,number):
    if obj == "": return number

    if      obj[0] == "/" : return number//int(obj[2])
    elif    obj[0] == "*" : return number*int(obj[2])
    elif    obj[0] == "+" : return number+int(obj[2])
    else:                   return number-int(obj[2])


def zero(obj=""):
    return operation(obj, 0)

def one(obj=""):
    return operation(obj, 1)

def two(obj=""):
    return operation(obj, 2)

def three(obj=""):
    return operation(obj, 3)

def four(obj=""):
    return operation(obj, 4)

def five(obj=""):
    return operation(obj, 5)

def six(obj=""):
    return operation(obj, 6)

def seven(obj=""):
    return operation(obj, 7)

def eight(obj=""):
    return operation(obj, 8)

def nine(obj=""):
    return operation(obj, 9)

def plus(obj):
    return "+,"+str(obj)


def minus(obj):
    return "-,"+str(obj)

def times(obj):
    return "*,"+str(obj)

def divided_by(obj):
    return "/,"+str(obj)

def test_train():
    print("Test 1 is Ok" if seven(times(five()))== 35 else "Test 1 is Fail")

    print("Test 2 is Ok" if four(plus(nine())) == 13 else "Test 2 is Fail")

    print("Test 3 is Ok" if eight(minus(three())) == 5 else "Test 3 is Fail")

    print("Test 4 is Ok" if six(divided_by(two())) == 3 else "Test 4 is Fail")

test_train()

