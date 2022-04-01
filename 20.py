a = []
n = int(input('vvedide kolichestvo strok: '))                # количество строк
m  = int(input('vvedide kolichestvo stolbcov: '))               # количество столбцов

#for i in range(n):
#    a.append([0]*m)
#for i in a:
#    print(i)

for i in range(n):
    b = []
    for i in range(m):
        b.append(int(input('vvedite znachenia v matricy: ')))
    a.append(b)
for i in a:
    print(i)