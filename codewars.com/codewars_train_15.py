
def remove_markers(string,markers):
    new_string = ''
    i = 0;
    s = str(string)

    while (i < len(s)) and (s[i] not in markers):
        new_string += s[i]
        i += 1
    return new_string

def solution(string,markers):
    """ Complete the solution so that it strips all text that follows any of a set
    of comment markers passed in. Any whitespace at the end of the line should
    also be stripped out.
    Example:
    Given an input string of:
    apples, pears # and bananas
    grapes
    bananas !apples

    The output expected would be:
    apples, pears
    grapes
    bananas
    """

    st = string
    list_first = st.split('\n')
    list_second = []

    for a in list_first:
        list_second.append(remove_markers(a,markers).rstrip())
    st = ''
    for i in range(len(list_second)):
        st = st + list_second[i] +('\n' if (i != len(list_second)-1) else '')
    return st

