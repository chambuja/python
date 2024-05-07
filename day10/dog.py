# coffee
# 침ㄴㄴ 앻:
class Dog:
    # 변수들
    def __init__(self, a ,b):
        self.name = a
        self.breed = b
        self.happiness =0
    def intro(self):
        print(f"{self.name}{self.breed}{self.happiness}")
    def eating(self):
        print("밥먹습니다.")
        self.happiness += 10
a = Dog("제니","푸들")
a.intro()
b = Dog("시츄","치와와")
b.intro()
c = Dog("율동","시바시바")
c.intro()
