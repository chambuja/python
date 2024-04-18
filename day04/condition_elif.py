#conmdition_elif
num = int(input(""))

if num >= 90 :
    print("A등급")
elif num >= 80:
    print("B 등급")
elif num >= 70:
    print("C 등급")
else:
    print()

# 국 영 수 점수를 3개 입력받고
# 평균이 90 점 이상 'A' , 80점이상 'B' , 70점 이상 'C', 60점이상 'D'
# 나머지는 F러 나타내는 프로그램 작성하기

kor = int(input("국어점수 입력 :"))
eng = int(input("영어점수 입력 :"))
moth = int(input("수학점수 입력 :"))
avg = (kor + eng + moth) / 3

if avg >= 90 :
    print("A등급")
elif avg >= 80 :
    print("B 등급")
elif avg >= 70 :
    print("C 등급")
elif avg >= 60 :
    print("D 등급")
else:
    print("F")

# nested condition : 'if문 안에 if문을 한번 더 사용할 수 있다.
# if 문의 depth 는 2번까지만 지향하는 걸로 !
score = int(input("점수입력 : "))
if score > 60 :
    if score == 100 :
        print("만점입니다.")
    else:
        print("합격입니다.")



