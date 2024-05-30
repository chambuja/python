# 문자열 섞기
# my_str  매개변수 n 이 주어질때
# mt_str 을 길이 n씩 잘라서 저장한 배열을 Return 하도록 solution 함수완성

# my_str = "abc1Addfggg4556b" # "abcdef123"
arr = "abc1Addfggg4556b"
a = list(arr)
print(a)
n = 6

def solution(my_str,n):
    arr = []
    word = ""
    for  index,item in enumerate(my_str,1):
        word += item
        if index % n ==0:
            arr.append(word)
            word = ""
    arr.append(word)
    return  arr
print(arr)

# JadenCase 문자열 만들기
#jaden Case 란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 단, 첫 문자가 알파벳이 아닐때에는 이어지는 알파벳은 소무자로 쓰면됩니다.(첫번째 입출력 예참고)
# 문자열 s가 주어졌을 때, s를 jadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해 주세요
# s = "3people un Followed me" # "for the last week"
#
# def solution1 (s):
#     return  "".join([x.capitalize() + " " for x in s.split(" ")])
# print(solution1())



