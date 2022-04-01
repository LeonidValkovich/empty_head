# 1. сформируем пустой словарь
words = dict()  # words = {}

# 2. Ввести количество слов в словаре
count = int(input('количество слов с словаре: '))

# 3. Цикл добавления слов
i = 0

while i < count:
    print('Ввод слов: ')
    wrd = str(input('Слово: '))
    value = int(input('Значение: '))

    # если ключа wrd нет в словаре, то добавить пару [wrd:value]
    if wrd not in words:
        words[wrd] = value
    i += 1

# 4. вывести сформированный словарь
print(words)
