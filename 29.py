salary = {'director': 120800.0,
          'secretary': 101150.25,
          'locksmith': 188200.00}
print(salary)

key = 'secretary'
if key in salary:
    del salary[key]
    print(salary)

# del salary['secretary']
# print(salary)
