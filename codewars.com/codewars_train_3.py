""" Given an array of ones and zeroes,
 convert the equivalent binary value
 to an integer.
 Eg: [0, 0, 0, 1] is treated as 0001
 which is the binary representation of 1"""

def binary_array_to_number(arr):
    s = ""
    for k in arr:
        s = s + str(k)
    return int(s,2)


def test_binary_array_to_number():
    a = [0, 0, 0, 1]
    print("Test 1 - Ок" if binary_array_to_number(a) == 1  else "Test 1 - Fail")
    a = [0, 0, 1, 0]
    print("Test 2 - Ок" if binary_array_to_number(a) == 2 else "Test 2 - Fail")
    a = [0, 1, 0, 1]
    print("Test 3 - Ок" if binary_array_to_number(a) == 5 else "Test 3 - Fail")
    a = [1, 0, 0, 1]
    print("Test 4 - Ок" if binary_array_to_number(a) == 9 else "Test 4 - Fail")
    a = [0, 0, 1, 0]
    print("Test 5 - Ок" if binary_array_to_number(a) == 2 else "Test 5 - Fail")
    a = [0, 1, 1, 0]
    print("Test 6 - Ок" if binary_array_to_number(a) == 6 else "Test 6 - Fail")

test_binary_array_to_number()


