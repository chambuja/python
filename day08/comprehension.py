#[ 0 ~ 100 ]리스트화 출력 출력

# numList =[]
# for x in range(101):
#     numList.append(x)
#     print(numList)
#
# a = [for x in range(101)]
#
# a = [x for x in range(101)]
# print(a)
#
#
# b = [x for x in "apple"]
# print(b)
#
# c = [x for x  in range (11) if x % 2 ==0 ]  # x가 짝수이면서  11번 반복리스트를 만들어라
# print(c)
# d = [x for x in range(101) if x % 2==1]  # x가 짝수이면서  101번 반복리스트를 만들어라
# print(d)
#
# #[ 0,4,16,64]
#
# e =[x**2 for x in range(101) if x % 2 == 0 ]
# print(e)
#
# f = [x+10 for x in range(11) if x % 2 ==1]
# print(f)
#

# # len => [5,6,4,5,6]
# # for x in fruits
#
# g = [len(x) for x in fruits if  "i"  in x ]
# print(g)

#조건부 컴프리헨션
h = [x +10 if x %2 ==1 else x +20 for x in range(101)]
print(h)

k = [x * 2 if x %2 ==1 else x**2 for x in range(15)]
print(k)

# 5글자 이하이면 글자의 길이로 나타내고, 아니면 대문자화하기
# fruits = [ "apple", "banana", "kiwi" , "grape","orange"]
i = [len(x) if len(x)<=5 else x.upper() for x in fruits]













