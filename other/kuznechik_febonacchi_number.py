
def traj_num(n):
    k = [0,1]+[0]*(n)
    for i in range(2,n+1):
        k[i] = k[i-2]+k[i-1]
    return k[n]

def cost_trajectory(n,price:list):
    """ Бежит кузнечик по числовому вектору
    он может пригать +1, или +2, есть стоимость пребывания точки.
    Задача определить минималный стоимость
     дойти кузнечику до точки n
     Входные данные n и список price цены пребывания точки,
     изначательно кузнечик стоит на первом точке"""

    c = [0,price[1],price[1]+price[2]]+ [0]*(n-2)
    print(*c)
    for i in range(3,n+1):
        c[i] = price[i]+ min(c[i-1],c[i-2])
    return c

name_place = []
price = [0,100,50,100,50,100,50,10]
c = cost_trajectory(7,price)
print(price)
print(c)
