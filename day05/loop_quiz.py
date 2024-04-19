# 1. 1~100 까지의 총합을 나타내는 프로그램
# total = 0
# for x in range(1,101):
#     total += x
#     print(x) #1~100

#2. 유저에게 과일을 입력 받고
# 모음을 제거한 단어로 나타내기!
# apple -> ppl, banana -> bnn , grape -> grp
# hint) for x in " "

# fruit = input("과일이름:")
# for x in fruit:
#     if x != 'e' and != 'a' and != 'u' and != 'i' and != 'o':
#         print(x)



# word = "apple"
# word1 = "banana"
# word2 = "grape"
#
# for x in list(apple, banana, grape)
#     if word
#

fruit = input("과일 이름:")
word = ""
for x in fruit:
    if not x in 'aeiou':
        word += x
print(word)




