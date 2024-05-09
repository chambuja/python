# 자료구조: 데이터를 어떻게 보관하고 다루는지에 대한  방법들
# list : 순서있고 중복가능
# set : 순서없고 중복 불가능
# dict : k[중복 안됨] -v [중복가능] 형태로 저장
# tuple:(사과, 바나나, 키위)  =>  [변경불가] , 수정불가능 "요소"


#심화 자료 구조:
# graph: 그래프 자료구조 [지도, 미니맵, 경로, 최적화]
# tree: 트리 자료구조 [단어 검색]



# ==== 각각의 리스트를 합하기=============
# name = ["아메리카노", "라떼","바닐라"]
# prices = [2000,2500,3000]
# menu = []
# for index,item in enumerate(name):
#     menu.append({"name":item ,"price": prices[index]})
# print(menu)
# ==========dict type 로 각가 리스트 합하기 ==============
# names = ["어메리카노", "라떼","바닐라"]
# prices = [2000,2500,3000]
# x = dict (zip(names,prices))
# print(x)
# ==========과일 가격 각각 리스트를 함하고 순서대로 표현하기 =========
# 과일이름 리스트[3]:
# 과일가격 리스트 [3]:
# zip으로 묶어서 k-v형태로 나타내세요
# fruits = ["kiwi", "banana", "mango"]
# prices1 = [ 2000, 3000, 4000]
# for index,(x,y) in enumerate(zip(fruits,prices1)):
#     print(f"{index}.{x} {y}")

# # ================
# for index,(x,y) in enumerate(zip(fruits,prices1)):
# print(f"{index}.{x} {y}")
# # ======================conprehention============
# fruits = ["kiwi", "banana", "mango"]
# prices = [ 2000, 3000, 4000]
# menu = [{"name": x, "price": y for (x,y) in }]
# for index , (x,y) in enumerate(zip(fruits, prices))
# # menu  = [{"name":x }]
# #
#
#












# name = ["아메리카노","라떼", "바닐라"]
# price = [ 2000,3000,3500]
# for index,(x,y) in enumerate(zip(name,price)):
#     print(f"{index},{x},{y}")





# [{"단어": "apple" , "글자수": 5} , {"단어": "banana" , "글자수" : 6}...]
# word = [ "student", "scool" , "man"]
# fruits = ["apple","mango", "grape"]
# num = [5,5,5]
# for index,(x,y,z) in enumerate(zip(word,fruits,num)):
#     print(f" {index},{x}{y}{z}")


text = "apple banana apple strawberry banana"
a = [{"단어": x } {"글자수": len(x) } for x in text.split(" ")]
print(a)




