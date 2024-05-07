# 커피메뉴 판매및 총 집계 프로그램 개발 의뢰
# enumerate :[열거하다]  {index},{item}

coffeeList = [{"name": "아메리카노", "price": 2000}, {"name": "라떼", "price": 2500}, {"name": "바닐라라떼", "price": 3000}]
while True:
    coffeeNumber = int(input("1.커피판매 2.커피추가 3.프로그램 종료"))
    if coffeeNumber == 1:
        for index,item in enumerate(coffeeList):
            print(f"{index}. {item['name']} {item['price']}원")
        coffeeNumber = int(input("번호 입력:"))
    elif coffeeNumber == 2:
        newCoffeeName = input("커피이름:")
        newCoffeePrice = int(input("커피가격:"))
        newCoffeeMenu = {'name': newCoffeeName, 'pricd': newCoffeePrice}
        print(newCoffeeMenu)
        coffeeList.append(newCoffeeMenu)
        print(f"{newCoffeeName}이 추가 되었습니다!")
    elif coffeeNumber == 3:
        print("프로그램종료")
        break


coffeeList = [{"name": "아메리카노", "price": 2000},{"name":"라떼", "price": 2500 , "name":"바닐라라떼","price":3000}]
while True:
    coffeeNumber = int(input("1.커피판매 2.커피추가 3.프로그램 종료:"))
    if coffeeNumber ==1:
        for index,item in enumerate(coffeeList):
            print()
    # while True:
    #     x = int(input("숫자 0을 넣어야 멈춤:"))
    #     if x ==0:
    #         break
    #     elif x ==1:
    #         print("아이스 아메리카노")
    #     elif x == 2:
    #         print("아이스 라떼")
