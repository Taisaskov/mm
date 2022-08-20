def ispr(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
mas = []
a = 3
for i in range(2,10000):
    if ispr(i):
        mas.append(i)
mn = set()
for i in range(3,8000,2):
    flag = 0
    for n in mas:
        for z in range(1,100):
            if i == (n + 2*(z**2)):
                mn.add(i)
                flag = 1
                break
            if flag == 1:
                break
        if flag == 1:
                break
for i in range(5,6000,2):
    if (i not in mas) and (i not in mn):
        print(i)
        break
