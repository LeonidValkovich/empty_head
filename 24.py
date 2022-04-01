import random

a = [random.randint(0, 5) for i in range(10)]
print(a)

b = [random.randint(-5, 0) for j in range(10)]
print(b)

c = a + b
print(c)
print(c.count(0))
