# quiz 핸드폰 번호 가리기
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼때 고객드릐 전화번호의
# 일부를 가립니다. 전화번호가 문자열 phone_numbers로 주어졌을때 전화번호의 뒷자리를
#제외한 나머지 숫자를 전부*로 가린 묹자열을 리턴하는 함수 완성
# return : "*******4444"
# phone_numbers = "01033334444"
# 해법 : 전체길이에서 나머지 문자열을 남겨두자로 접근
# def solution(phone_number, ):
# [list(x.split("") for x in range(phone_number)]
# tartet = "01033334444"
# answer = ""
# def solution(target):
#     # tartet = "01033334444"
#     answer = ""
#     for index,item  in enumerate(list(target)):
#         if len(target) -index <= 4:
#             answer += item
#         else:
#             answer += "*"
#     return  answer
# print(solution(tartet))  #*******4444

# 영어가 싫어요
# 영어가 싫은 강사님은 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
# 문자열 numbers가 매개변수로 주어질때  numbers를 정수로 바꾸어 return 하는 함수
#
def solution1(numberStr):
    numberDict = {
    "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7,"eight":8,
    "nine":9,"ten":10
    }
    for x in list(numberDict.keys()):
        if x in numberStr:
            # numberStr =  "onetwothreefourfivesixseveneightnineten"
            numberStr = numberStr.replace(x, str(numberDict[x]))
    return numberStr
print(solution1(numberStr))




