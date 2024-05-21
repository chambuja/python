# 제일 작은수 제거하기
# arr : [4,3,2,1]   return [ 4,3,2]
# 배열이 빈배열인 경우엔 배열에 -1을 채워 리턴하세요
# arr = [4,3,2,1]
# for x in list(arr):
#     print(x)
#     a = x.list(arr)
#     a.revers()
#
# # def solution(arr):
#     if len(arr) == 1:
#         return  [-1]
#     else:
#         arr.remove(min(arr))
#         return arr

# ================
# a = "oxooxoxxox".split("x")
# b = list(filter(lambda  x: len(x)>0:))
# ===================
# def solution3(str):
# #     return  list(map(lambda x: len(x), filter(lambda )))
# #     if x in len()
# arr = ["nami","ahri", "jayce","garen", "ivern","vex", "jinx"]
# def solution4(arr):
#     return [ index for index,item in enumerate(arr) if index % 5==0 ]
#





#========================================
#x사이의 개수 주어진 문자열 myString 을 문자 "x"를

# def solution3():
#
# a = myString()
#

# def hello(x):   # (x = "icecream") # 디폴트 매개 변수
#     return f"{x} hello"
# # lambda # 함수가 지나치게 길때 간단히 표현하는 방식
# lambda x : x+1
#
# # 콜백함수 [# 매개변수에 함수를 넣는것 ]
#
# # map (how, what)
# print(list(map(lambda x: x+5,[1,2,3,4,5])))
#
# # filter (how, what): what 을 how로 걸르기
# print(list(filter(lambda x: x % 2  == 0 , [1,2,3,4,5])))



class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "소리내는중"
class Dog(Animal):
    def __init__(self,name , breed):
        super().__init__(name)
        self.breed