n = int(input())
mas = []
ch = []
k = 0
for i in range(n):
    a = int(input())
    mas.append(a)
for a in mas:
    if a not in ch:
        ch.append(a)
        k += 1
print(k)
    
    
