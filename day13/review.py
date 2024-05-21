# 문자열 뒤집기
#문제 : 문자열 my_string 이 매개변수로 주어짐
# my_string 을 거꾸로 뒤집은 문자열을 return 하도록 함수를 완성해주세요
# my_string.  "haron" "bread"
# my_string."haron"
# 문제에 대한 정의를 하러 가자
my_string = "haron"
def reversedWord(my_string):
    wordList = list(my_string)
    wordList.reverse() # [h,a,r,o,n]
    revsedWord = "".join(wordList)
    return revsedWord

#===============

# 미완성된 할 일 찾기
#문제: todo_list 에 있는 할 일 중 finished 배열을 통해 아직 끝내지 못한
# 일들을 찾아 순서대로 배열에 담아 반환함수만들기
#toDoList = ["problemsolving", "practiceguiter","swim" , "practicestudy"]


# =======

class Animal:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

    def eat(self):
        print("냠냠냠")

    def sound(self):
        pass

    def introduce(self):
        print(f"이름:{self.name} 종:{self.bread}")

class Dog(Animal):
    def sound(self):
        print("멍멍")

class Cat(Animal):

    def sound(self):
        print("냐옹")

a = Dog("킹율","이탈리안하우수스")
b = Cat("떼컬룩","치즈냥이")

a.eat()
a.sound()
a.introduce()
b.eat()
b.sound()
b.introduce()

#================퀴즈 ====
# 관리자.  편집자, 뷰어라는각각 사용자가 존재
# 모두 접근하기라는 함수를 가지고 있습니다.
# 모두 username 이라는 속성도 가지고 있습니다.

# 관리자 -유저만들기
# 편집자 -편집하기
# 뷰어 - 조회하기

class User:
    def __init__(self,username):
        self.username = username

    def access(self):
        print("접근을 허용합니다.")


class Editor(User):

    def editer(self):
        print("편집을 합니다.")
        pass

class Viewer(User):
    def view(self):
        print("조회를 합니다.")
        pass

a =