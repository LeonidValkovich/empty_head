a = (1, 2, 3, 4, 5, 6)
b = [1, 2, 3, 4, 5, 6]

print(a.__sizeof__())
print(b.__sizeof__())

print(type(a))
print(type(b))

c = list(a)
print(type(c))
print(c)