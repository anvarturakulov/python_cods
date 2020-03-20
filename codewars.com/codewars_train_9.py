""" You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items. We want to create
the text that should be displayed next to such an item.
Implement a function likes :: [String] -> String, which must take in
input array, containing the names of people who like an item. It must return
 the display text as shown in the examples

 likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others
like this"
For 4 or more names, the number in and 2 others simply increases.
"""

def likes(s):

    if len(s) == 0:
        return "no one likes this"
    elif len(s) == 1:
        return str(s[0])+ " likes this"
    elif len(s) == 2:
        return str(s[0])+ " and "+ str(s[1]) + " like this"
    elif len(s) == 3:
        return str(s[0])+", "+str(s[1])+" and "+str(s[2])+" like this"
    else:
        return str(s[0])+", "+str(s[1]) + " and "+str(len(s)-2)+ " others like this"


def test_likes():
    s = ["Peter"]
    print("Test 1 is OK" if likes(s) == "Peter likes this" else "Test 1 is Fail")

    s = ["Jacob", "Alex"]
    print("Test 1 is OK" if likes(s) == "Jacob and Alex like this" else "Test 2 is Fail")

    s = ["Max", "John", "Mark"]
    print("Test 1 is OK" if likes(s) == "Max, John and Mark like this" else "Test 3 is Fail")

    s = ["Alex", "Jacob", "Mark", "Max"]
    print("Test 1 is OK" if likes(s) == "Alex, Jacob and 2 others like this" else "Test 4 is Fail")

test_likes()

