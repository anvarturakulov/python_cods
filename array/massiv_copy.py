def array_copy(n):
    a = [0]*n
    b = [0]*n
    c = []
    for k in range(n):
        b[k] = a[k]
    print("b = ",b)
    for k in range(n):
        a[k] = k + 1
    print("a = ",a)
    c = list(a)
    for k in range(n):
        c[k] *= 2
    print("c = ",c)
    print("a = ",a)

n = 10
array_copy(n)

