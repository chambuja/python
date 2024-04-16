#compare_logic
#compare[비교]
#>, < ,<=, >= , ==[같니?] , != [다르니?
a = 10
b = 20
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a != b)

# logic[논리] 연산자 : bool타입에 사용되는 연산자
#and , or, not
c = 5
d = 3
# and : 모든 조건이 참이면 "참"
print(c> d and c==5 and d==3) # True
# or  : 하나라도 조건이 참이면 "참"
print(c>d or c==6 or d==3) # true

#not : 조건의 반대를 반환
print(not (c>d)) # Fales


x = 5
result = (x>3) and x == 5 #True
#드모르간 법칙 적용
Result1 = not (x<=3) and x != 5  #수학적으로  # True

# 멤버쉽 연산자 [in]
coffee = "americano"
print('a' in coffee) # True
print('ameri' in coffee) # True
text = input("단어 입력")# 두문장 이상으잉 글
news = """윤 대통령, 성찰 없었다…민심은 틀렸다는데 “국정 옳았다” """
print("성찰" in news )

#슬라이싱 연산자 [ : }\

car = "tesla"
print(car[0:3]) # tes
print(car[1:3]) # es

#인덱스 연산자 [ []  ]
code = "python"
print(code[0]) #p
print(code[3]) #h


