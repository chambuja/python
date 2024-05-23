# user : 태어난 년도
# 12간지 띠 알려주는 기능구현
# birthday = int(input("태어난 년도입력 : "))
# year_cycle = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말","양","원숭이", "닭","개","돼지"]
# saju =[]
# for x in range():
#     if birthday
#         saju.
# def saju(self):


def yearToZodiac(year):
zodiac = {
            0:"원숭이",
            1:"닭",
            2:"돼지",
            3:"개",
            4:"쥐",
            5:"소",
            6:"호랑이",
            7:"토끼",
            8:"용",
            9:"뱀",
            10:"말",
            11:"양"
    }
for x in range(12) :
    zodiac.items().

#     # 쥐띠 - 84
#     #=====================
#     a = list(str(12345)) # [1,2,3,4,5]
#     a.reverse()
#     b = list(map(lambda x: int(x), a))
#     return b

#=================
# def makeReversedNumber(x)
#     return list(map(lambda  x : int(x), reversed(list(str(x)))))
# #===============================================
# def solution(num):
#     return([x for x in range(num + 1) if x %2 ==1])

# ==============
#import random
#random.randint(1930,2025)
# random.choice(["콜라","사이다", "환타", "스프라이트"])
#random.shuffle(b) 불규칙적으로 선택
b = ["콜라", "사이다", "환타", "스프라이트"]
c = [6,2,1,1,] # "6" 비율을 말함
d = random.choices(b,weight, 10 )



# 띠함수를 이용하여
# 100개의 수를 입력하고
import random
a = [yearToZodiac(random.randint(1930,2025)) for x in range(100)]
print(a)

