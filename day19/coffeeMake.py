import  sqlite3  # 경량화된 파이썬 미니버젼 라이브러리
connection = sqlite3.connect('test.db')  # 변수 connection 만듬
cusror = connection.cursor()

# 문자열 3개  => 커피관련 속성민들기
# sql = """
# INSERT INTO COFFEE(id, coffeeName ,coffeePrice , coffeeKcal)
# VALUES ( 1 ,'AMERICANO' , 2400 , 10 );
#
#  """
# cusror.execute(sql)
# connection.commit()
# connection.close()  # test.db파일이 디렉토리에 생성됨
#

# DB Browser for SQLite 에서 데이터 사용가능 (무료)

# 문제 bOOKS라는 테이블을 생성하싱오
# id ,title ,, author , published_year 는 정수형 in_stock 은 블리언 값(0또는 1로저장) 으로 정의해야 합니다.

sql = """ 
CREATE TABLE Books(
    id INTEGER PRIMARY KEY,
    title TEXT , 
    author  TEXT ,
    published_year TEXT,
    in_stock BOOLEAN 
 )
 """
cusror.execute(sql)
connection.commit()
connection.close()  # Books.db파일이 디렉토리에 생성됨

sql = """
INSERT INTO Books(id, title ,author ,published_year, in_stock)
VALUES ( 1 ,'henrypoter' , 'kimeunsuk' ,2024 , True );
 """
cusror.execute(sql)
connection.commit()
connection.close()