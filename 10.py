a = [0, 4, 4, 0, 2, 4, 3, 1, 0, 2, 4, 3, 3, 2, 1]
c = [0] * 6
for i in a:
    c[i] += 1
print(c)
for i in range(6):
    if c[i] > 0:
        print((str(i) + ' ') * c[i], end='')
