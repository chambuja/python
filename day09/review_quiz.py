# 이메일 주소 분리 퀴즈
# 사용자로부터 메일을 받고 분리하는 거

# print(
# add = input("주소입력: ")
# dict {
#     "user": "itKorea",
#     "domain":"naver.com"
# }
#
# def splitEmail(email):
#     arr = email.splite
#     return.add
#
# 문자열 변환 마법 퀴즈
# 사용자로부터 문자열을 입력받고
# 입력된 문자열을 뒤집어 순서를 바꾸고,
# 다른 하나는 문자열의 문자들을 알파벳순서로 정렬합니다.
# ex) 입력 : "mega"
#     출력 : {reversed:"arem , sorted : "aemg"}
# sort 보여주기 목표!
def spellingMagic(word):
    spellingList = list(word) #[m,e,g,a]
    spellingList.sort() # [a,e,g,m]
    result = "".join(spellingList) # list =>str

    spellingList1 = list(word)
    spellingList1.reverse()
    result1 = "".join(spellingList1) # list => str
    return {"sorted":result, "reversed": result1}
print(spellingMagic("koreait"))
#
# spellingList1
# spellinglist("mega")
# def wordReverseSort(word)
#     word.reverse "word"
#     word.sort"word"
#     return

# ==========================
# n이정해젔을때 함수만들기

num = int(input("정수입력"))

if num %2 ==1


def oddEven()


