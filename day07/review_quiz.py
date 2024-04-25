# 문자열 문자 반복 프로그램:
# 입력 : "abc", n=2"
# 결과 aaabbbccc

# word = input(" 단어 입력 : ")
# count = int(input("반복 횟수 :"))
# newWord = ""
# for x in word:
#     newWord += x * 3
#     print(newWord)
# ================================
#  단어 입력 : ddee
# 반복 횟수 :3
# ddd
# dddddd
# ddddddeee
# ddddddeeeeee
# ================================


# 모음 대문자화 프로그램
#문자열을 입력받아 그문자열 내의 모든 모음 (a,e,i,o,u )
#만 다문자로 변환하는 프로그램다른문자들은 원래 상태유지


#  # 입출력예: CCCccc => cccCCC
#===========================================
# word = input("단어 입력:")
# newWord =""
# for x in word:
#      if x.isupper():
#          newWord += x.lower()
#          print(newWord)
#      else:
#          newWord += x.upper()
#
# 단어
# 입력: wwwffffSSS
# WWWFFFFs
# WWWFFFFss
# WWWFFFFsss
#=============================================
#  # 단어입력
#  # 자음은 대문자화 해서 출력
 word = input("단어입력:")
 newWord = ""
 for x in word :
     if x not in"aieou":
        newWord += x.lower()
         print(newWord)
    else:
        newWord += x.lower()


#
# word = input("단어입력:")
# isUpper = ""
# isLower =
# for x in newWord:
#     if x
#
#




