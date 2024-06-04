# 데이터베이스[영구적]
# 데이터를 저장하는 물리적인 공간

# [메모장] -> [엑셀] (수정/1억줄 미만]
# [데이터베이스 ] (무한정 수정 가능)


#메모리[끄면 날라감 ] [휘발성]
# 테이터를 저장하는 일시적 물리적공간

# mysql , mongodb , mssql ,  oracle, ...? lib 가져와야 함
import  sqlite3  # 경량화된 파이썬 미니버젼 라이브러리
connection = sqlite3.connect('test.db')  # 변수 connection 만듬
cusror = connection.cursor()

# 문자열 3개  => 커피관련 속성민들기
sql = """ 
CREATE TABLE COFFEE(
    id INTEGER PRIMARY KEY ,
    coffeeName  TEXT ,
    coffeePrice INTEGER,
    coffeeKcal INTEGER
 )
 """
cusror.execute(sql)
connection.commit()
connection.close()  # test.db파일이 디렉토리에 생성됨


# DB Browser for SQLite 에서 데이터 사용가능 (무료)
