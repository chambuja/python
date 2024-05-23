#import datetime  지금 시간을 알려주는 라이브러리
import datetime

a = datetime.datetime.now()
print(a)  # ==> 2024-05-23 20:17:42.911441

b = datetime.datetime.now().strftime("%y-%m-%d")
print(b)  # ==> 24-05-23

c = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
print(c)  # ==> 24-05-23 20:20:45

d = datetime.date.today()
print(d) # ==> 2024-05-23

#e = datetime.time.strftime("%H:%M:%S")

# 두 날짜나 시간 사이의 기간표기법
today = datetime.date.today()
g= next_week = today + datetime.timedelta
print(g)

f = datetime.timedelta(days =7)
print(f)  # ==> 7 days, 0:00:00


