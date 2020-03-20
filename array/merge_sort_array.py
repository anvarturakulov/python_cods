
def merge(a:list,b:list):

    c = [0] * (len(a)+len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c

def merge_sort(a):
    middle = len(a) // 2
    if len(a) <= 1:
        return
    left  = [a[i] for i in range(0,middle)]
    rigth = [a[i] for i in range(middle,len(a))]

    merge_sort(left)
    merge_sort(rigth)

    c = merge(left,rigth)
    for i in range(len(a)):
        a[i] = c[i]

b = [1,3,2,5,1,6,4,4,8,9,10]
merge_sort(b)
print(b)