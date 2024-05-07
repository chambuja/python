# enumerate: [열거하다]
fruits = [ 'apple', 'orange','mango']
for x in fruits:
    print(x)
    print(f"{}")


for index, item  in enumerate(fruits):
    print(f"{index}.{item}")

coffees = ['{'name':'아메리카노'},{'name': '라떼'}]
for index,item in enumerate(coffees):
    print(f"{index},{item['name']}")

# 0,아메리카노 2000원
# 1. 라데 3000원


coffees1 = [{name':'아메리카노','price': 2000 } , {'name': '라떼', 'price':3000'}]
for index,item in enumerate(coffees1):
    print(f"{}")
