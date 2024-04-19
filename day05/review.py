# 정수 평균 계산프로그램
# 사용자입력 10,20,30
# 프로그램 출력:
# " 평균은 20 입니다."
#
# num1 = int(input(" 첫번째 정수입력:"))
# num2 = int(input(" 첫번째 정수입력:"))
# num3 = int(input(" 첫번째 정수입력:"))
# avg = (num1+ num2 + num3 ) /3
#
# print(f"평균은 {avg}입니다. ")
#
#
# num1 = int(input(" 첫번째 정수입력:"))
# num2 = int(input(" 첫번째 정수입력:"))
# num3 = int(input(" 첫번째 정수입력:"))
# if num1 > num3 and num1 > num2:
#     print(num1)
#
#
# 입력한 정수의 배수 출력 프로그램
# 사용자 입력 : 20
# 프로그램 출력 : " 20의 배수 : 20, 40, 60, 60, 80, 100"

num = int(input("정수입력: "))
for x in range(101):
    if x % num == 0:
        print(x)

