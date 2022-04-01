a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)

c = sum(a)
d = sum(b)
if c > d:
    print('summa tuple a bigger', c)
else:
    print('summa tuple b bigger', d)

e = a.index(min(a))
print(e)
