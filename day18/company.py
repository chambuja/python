# 300명
import pandas
from faker import Faker
import random
f = Faker('ko_kr')

ageList = [20,30,40,50,60]
salaryList = [ 3000 + x * 500 for x in range(14)]
departmentList = ["영업부", "사업부" , "개발부", "경영부", "인사부", "생산부"]

# 'name':[f.name() for x in range(300)] ,   # 300명
#     'age' : [20,30,40,50,60],
#     'salary': 3000~10000  500단위,
#     'department': ["영업부", "사업부" , "개발부", "경영부", "인사부", "생산부"],
#     'year_at_company': 1~15,
#     'job_statisfaction': 1~10,
#     'foerformance_score':1~100
data = {
    'name':[f.name() for x in range(300)] ,   # 300명
    'age' : [random.choice(ageList) for x in range(300)],
    'salary': [random.choice(salaryList) for x in range(300)],
    'department': [random.choice(departmentList) for x in range(300)],
    'year_at_company':[ random.randint(1,15) for x in range(300)],
    'job_statisfaction':[ random.randint(1,10) for x in range(300)],
    'performance_score':[ random.randint(1,100) for x in range(300)]

}

df = pandas.DataFrame(data)
df.to_csv('company.csv',index = False, encoding ='cp949')
print(df)
# def makeName():
#     return random.choice(List("advkdkekdfkekfkjfdkjfklwlck")) + random.choice(list("adkjrjekjdkjfkjvktjdskjdwhld"))
# data = {
import datetime
import pandas
from faker import Faker
import random
f = Faker('ko_kr')
majorList = [ "국문","일문","영문","중문","철학","노어","문헌정보","경제","경영"]

data = {
     "name":[f.name() for x in range(1000)],
    "grade":[random.randint(1,5) for x in range(1000)],
    "major":[random.choice(majorList) for x in range(1000)],
    "score":[round(random.uniform(1,4.5),2) for x in range(1000)]
}

df = pandas.DataFrame(data)
df.to_csv('university.csv',index=False,encoding='cp949')
#===========================================================
# f = Faker('ko_kr')
# coffeeList = [ "아메리카노","라떼","홍차","녹차","딸기주스","민트" ]
# payList = ["카카오페이","토스", "카드","삼성카드","네이버페이","현금"]
# data = {
#      "name":[f.name() for x in range(5000)],
#     "menu":[random.choice(coffeeList) for x in range(5000)],
#     "pay":[random.choice(payList) for x in range(5000)],
#     "togo": [random.choice(["포장","매장"]) for x in range(5000)]
# }
#
# def get_ramdom_time():
#    open =  datetime.datetime.strftime("07:00","%H:%M")
#    close =  datetime.datetime.strftime("22:00", "%H:%M")
#    total = int((close-open).total_seconds()/ 60) #전체 몇분
#    random_minutes = random.randint(0,total)
#    return open + datetime.timedelta(minutes=random_minutes)
#
# print(get_ramdom_time().strftime
#
# df = pandas.DataFrame(data)
# df.to_csv('mega.csv',index=False,encoding='cp949')
#
#
# import pandas as pd
# arr = [1 for x in range(101)]
# series = pandas.series(arr)
#
# data ={
#     "movies":["혹성탈출", "범죄도시4", "설계자", "퓨리오사"],
#     "popcorn":["오리지널팝콘", "어니언팝콘","캬라멜팝콘","치즈팝콘"],
#     "beverage":["콜라","제로콜라","쥬스","스파쿨"]
# }
#
# pf = pandas.DataFrame(data)
# print(pf)
#
# # 학생이름 학년 전공 평균학점 10명
#
# data = {
#     "name":["인석","광현","명수","재민"],
#     "grade":[3 ,4, 6, 5],
#     "major":["영어","수학","국어","물리"],
#     "score":[30 ,40 ,29 ,55]
# }
# pf = pandas.DataFrame(data)
# print(pf)
#
#
# # 1000명일때
# majorList = [ "국문","일문","영문","중문","철학","노어","문헌정보","경제","경영"]
# list("advkdkekdfkekfkjfdkjfklwlck") + random.choice(list("adkjrjekjdkjfkjvktjdskjdwhld"))
#
# def makeName():
#     return random.choice(List("advkdkekdfkekfkjfdkjfklwlck")) + random.choice(list("adkjrjekjdkjfkjvktjdskjdwhld"))
# data = {
#      "name":[makeName() for x in range(1000)],
#     "grade":[random.randint(1,5) for x in range(1000)],
#     "major":[random.choice(majorList) for x in range(1000)],
#     "score":[round(random.uniform(1,4.5),2) for x in range(1000)]
#
# }
# import math
#
# pf = pandas.DataFrame(data)
# print(round(random.uniform(1,4.5),2) for x in range(1000))
#
