""" Usually when you buy something,
 you're asked whether your credit
 card number, phone number or answer
 to your most secret question is still correct.
 However, since someone could look over your
 shoulder, you don't want that shown on your
 screen. Instead, we mask it.
 Your task is to write a function maskify,
 which changes all but the last four characters
 into '#'."""
# variant # 1
#def maskify(cc):
#    s = ""
#    if len(cc) > 4:
#        for k in range(len(cc)):
#            if k < (len(cc)-4):
#                s += "#"
#            else:
#                s += cc[k]
#        return s
#    else:
#        return cc

def maskify(cc):
    l = len(cc)
    if len(cc) < 4 :
        return cc
    else:
        return (l-4)*"#"+cc[l-4:]

def test_maskify():
    s = "4556364607935616"
    s_result = "############5616"
    print("Test 1 is Ok " if maskify(s) == s_result else "Test 1 is Fail")

    s = "64607935616"
    s_result = "#######5616"
    print("Test 2 is Ok " if maskify(s) == s_result else "Test 2 is Fail")

    s = "1"
    s_result = "1"
    print("Test 3 is Ok " if maskify(s) == s_result else "Test 3 is Fail")

    s = ""
    s_result = ""
    print("Test 4 is Ok " if maskify(s) == s_result else "Test 4 is Fail")

test_maskify()