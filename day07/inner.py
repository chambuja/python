# "hello".upper() => HELLO
# [].append()
#length
#len: 문자열 또는 리스트의 길이를 알려주는 기능
print(len("hello"))
#
# print(len("python"))
# print(len([2,3,4,6,8,9]))
#
# #max , min
# print(max([2,3,5,7,11,43]))
# print(min([2,4,5,67,83]))
#
#
# #영어기사 스크랩해오고
# # 단어길이가 6글자이상인
# # 단어들만 출력하기
# news ="""
# European Union officials have raided the offices of Chinese security equipment maker Nuctech as part of a probe into subsidies, exposing rising tensions between the bloc and one of its biggest trading partners."""
# words = news.split()
# for x in words:
#     if len(x)>= 6:
#         print(x)

# ====================================================================================
# fruit = ["apple","banana","kiwi","mango","strawberry","pineapple","melon"]
# print(fruit)
# for x in fruit:
#     if len(x) <= 5 and "a"in x or "e" in x:
#         print(x.upper())
#     else:
#         print(len(x))
#=============> 결과============
# ['apple', 'banana', 'kiwi', 'mango', 'strawberry', 'pineapple', 'melon']
# APPLE
# 6
# 4
# MANGO
# STRAWBERRY
# PINEAPPLE
# MELON
#==================================================================
