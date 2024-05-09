# function : 명령어 묶음
# 내장 함수 : print, input, len, sum, int, list, dict, zip, enumerate, ....
# def name(args): args= # 매개변수
# 로직
# return value
# 디폴트 매개 변수
def hello(x):   # (x = "icecream") # 디폴트 매개 변수
    return f"{x} hello"
# lambda # 함수가 지나티게 길때 간단히 표현하는 방식
lambda x : x+1

# 콜백함수 [# 매개변수에 함수를 넣는것 ]

# map (how, what)
print(list(map(lambda x: x+5,[1,2,3,4,5])))

# filter (how, what): what 을 how로 걸르기
print(list(filter(lambda x: x % 2  == 0 , [1,2,3,4,5])))
