
def search_substring(a,b):
    a_len = len(a)
    k = 0
    i = 0
    while (len(b)-i)>0:
        if b[i:i+a_len] == a:
            k += 1
        i += 1
    
    return k

def test_search_substring():
    a = "abacd"
    b = "fdeabacddfgdgabacddgdgabacddfsfgabacdhfghabacdsdfgabacd"
    print("Test 1 is Ok" if search_substring(a,b) == 6 else "Test is 1 is Fail")

    a = "abacd"
    b = "kdjkdjfdiuojlsgjlsd;gfj;sdfbvsdgbnfgsd;lgsd;lgjowieuroqwiuer"
    print("Test 2 is Ok" if search_substring(a, b) == 0 else "Test is 2 is Fail")

test_search_substring()