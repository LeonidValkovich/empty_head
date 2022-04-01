a = float(input('enter first number: '))
b = float(input('enter second number: '))
c = float(input('enter third number: '))

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if c > a and c > b:
        if a > b:
            print(a)
        else:
            print(b)
