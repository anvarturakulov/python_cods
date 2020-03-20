
""" ATM machines allow 4 or 6 digit
PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string,
return true, else return false."""

def validate_pin(pin):
    a = ["0","1","2","3","4","5","6","7","8","9"]
    res = True;
    for k in pin:
        if k not in a:
            return False
    if len(pin) != 4 and len(pin) != 6:
        return False
    return res

def test_validate_pin():
    p1 = "1234"
    print("Test 1 - Ок" if validate_pin(p1) else "Test 1 - Fail")
    p2 = "12345"
    print("Test 2 - Ок" if validate_pin(p2) else "Test 2 - Fail")
    p3 = "a234"
    print("Test 3 - Ок" if validate_pin(p3) else "Test 3 - Fail")

test_validate_pin()
