a = [1,2,3,4,5,6,7,11,18,19]
b = []
# Добавление элемента
for x in a:
    if x % 2 == 0:
        b.append(x**2)

# Другая задача по доавбление элемента
b= []
for k in range(len(a)-1,-1,-1):
    b.append(a[k])

#Другой способ добавления элемента
b = []
b = [x for x in a if x % 2 == 0]

#Другой способ добавления элемента
b = []
b = [x if x % 2 ==0 else 0 for x in a]

#Другой пример
a = [(-1)*x if x%2==0 else x for x in range(10)]
print(a)
b = [0 if x<0 else x for x in a]
print(b)






