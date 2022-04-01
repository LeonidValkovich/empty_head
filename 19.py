# вложенные списки

a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]

# b = ['hello', 'hi', 'world']
# print(len(a))
# print(a[2][3])
# print(a[0][3])
# print(a[2][2][1])
# print(b[2][1:3])

# for i in a:
#    for j in i:
#       print(j, end = ' ')
#  print()

for i in range(3):
    for j in range(4):
        print(a[i][j], end=' ')
    print()

for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(a[i][j], end=' ')
    print()
