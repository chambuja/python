# dict
# (기본타입)
# person = {
#     'name': "엄준식",
#     'age' : 29,
#     'town':"동탄",
#     'coffeeList': ["아메리카노","라떼","주스"],
#     'academy': {
#         "first":"java",
#         "second": "c-language",
#         "third": "python",
#     }
#
# }
#
# print(f"이름:{person["name"]} 동네:{person["town"]} 좋아하는 커피 3번째: {person["coffeeList"][2]}")
# print(f"세변째수업:{person["academy"]["third"]}")

#데이터 생성
person["gender"] = "woman"  # k - v 데이터 만들기

#데이터 삭제

del person("town")
print(person)
#
print(person.keys())
print(person.value())
