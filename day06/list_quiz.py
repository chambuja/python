#1. 유저에게 다섯개ㅔ의 정수입력받고,
# 각각 요소를 3배로 만든다음 출력하기
#
# a = int(input(" 정수입력:"))
# b = int(input(" 정수입력:"))
# c = int(input(" 정수입력:"))
# d = int(input(" 정수입력:"))
# e = int(input(" 정수입력:"))
# a1 = a*3
# b1 = b*3
# c1 = c*3
# d1 = d*3
# e1 = e*3
# list1 = [a1,b1,c1,d1,e1]
# print(list1)

# 유저에게 다른 정수 다섯개 정수입력
# 리스트화 한다음에, 가장 큰수를 뽑아낸 ㄴ

a = int(input(" 정수입력:"))
b = int(input(" 정수입력:"))
c = int(input(" 정수입력:"))
d = int(input(" 정수입력:"))
e = int(input(" 정수입력:"))
list2 = [a,b,c,d,e]
list3 = list2.sort()
print(list3[0])

#================================================
for x in range(5):
    num = int(input(" 정수입력:"))
    numberList.append(num)
    print(numberList)

newNumberList = []
for x in newNumberList:
    newNumberList.append(x*3)
    print(newNumberList)
newNumberList

#==================
#리스트화 한 다음에, 가장 큰 수를 뽑아내는 프로그램
numberList =[]
for in range(5):
    num = int(input("정수 입력:"))
    numberList.sort()
    numberList.reverse()
    print(numberList[0])



