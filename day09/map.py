# 기본 내장함수:
# map(how , target ): target 을 바꿔주기
# numList = [i for i in range(101)]
# [100,101,102,....200]
# result = list(map(lambda i : i+100, numList))
# print(result)

# filter : target 을 필터링해줌
# 짝수만 걸러줘
# result1 = list(filter(lambda  x:x%2==0 ,numList  ))
# print(result1)

# 5글자 이하만 골라내기


#fruits = [ "apple","banana","cherry","kiwi"]
# filter(lambda x:len(x) <=5 , fruits)


# 알파벳 a가 포함되어 있는 것 살리기
# fruits = [ "apple","banana","cherry","kiwi"]
# filter(lambda x: "a" in x, fruits)

# map -> 유저아이디로 바꾸기
emailList = ["abc@naver.com", "mega@gmail.com","korea@daum.net"]
print(map(filter(lambda x: x.split("@"))[0],emailList))

