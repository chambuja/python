#class
# class Dog:
#     def __init__(self):
#         self.name = "월트"
#         self.breed = "달마시안"
#     def barking(self):
#         print("명멍!")
# a = Dog("월트")
# a.barking()
# print(a)

# Book클래스 만들기
# 제목 , 작가를 가지는 클래스
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display_info(self):
        return f"책 제목:{self.title} 작가:{self.author}"
    # display_info -> return str 책 제목:{} 작가:{}
    def test(self):

    def find(self):
        

b = Book("해리포터", "롤링")
print(b.display_info())


