# x: 1, "abc@naver.com" ,

# def test(x):
#     return 1
#     print(x)
# ==========================
def a(x):
    print("a함수 실행 ")
    x()
def b():
    print("b함수 실행")
a(b)
# ==================================
# 게임 몬스터 프로그램

def getGold():
    print("골드확득")

def getFood():
    print("음식획득")

killing_monster("슬라임,getGold")
killing_monster("늑대","getfood")


