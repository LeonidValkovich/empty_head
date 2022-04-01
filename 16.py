# длина пароля 3 символа

from string import printable  # из модуля string импортируем переменную printable

print(printable)  # пароль: b1 b2 b3
for b1 in printable:
    for b2 in printable:
        for b3 in printable:
            print(b1, b2, b3)
