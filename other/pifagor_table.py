
def table_pifagor(n:int):
    f =  [[0]*(n) for i in range (n)]
    for i in range(n):
        f[i][0] = i+1
        f[0][i] = i+1
    for i in range(1,n):
        for k in range(1,n):
            f[i][k] = f[i][0]*f[0][k]
    return f

def print_pifagor():
    n = 9
    f = table_pifagor(n)
    for i in range(n):
        s = []
        for k in range(n):
            ss = str(f[i][k])
            if len(ss)==1:
                ss = " "+ss
                s.append(ss)
            else:
                s.append(ss)
        if i == 1: print("-"*42)
        print(*s,sep="   ")

print_pifagor()