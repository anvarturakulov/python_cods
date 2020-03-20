"""You are going to be given a word. Your job is to return
 the middle character of the word. If the word's length is odd,
 return the middle character. If the word's length is even,
 return the middle 2 characters.   """

def get_middle(s):
    l = len(s)
    if   l < 2     : return s
    elif l % 2 == 1: return s[l//2]

    return s[l//2-1]+s[l//2]

def test_get_middle():
    s = "test"
    s_result = "es"
    print("Test 1 is OK " if get_middle(s) == s_result else "Test 1 is Fail")

    s = "testing"
    s_result = "t"
    print("Test 2 is OK " if get_middle(s) == s_result else "Test 2 is Fail")

    s = "middle"
    s_result = "dd"
    print("Test 3 is OK " if get_middle(s) == s_result else "Test 3 is Fail")

    s = "A"
    s_result = "A"
    print("Test 4 is OK " if get_middle(s) == s_result else "Test 4 is Fail")

test_get_middle()