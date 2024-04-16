# 뉴스기사단너 검색프로그램
#뉴스기사를 스크랩해 온 후, 사용자로부터 입력받은 단어가 그 기사내에 존재하는지 여부를 나타내는 프로그램을 만들어보세요

news = """실손의료보험 비급여항목에 대한 관리 부실과 도덕적 해이는 보험금 누수에만 그치지 않고 필수의료 부족을 유발하는 의료시장 왜곡과 선량한 보험가입자의 보험료 인상으로 이어지는 것 등이 큰 문제로 지적돼 왔다."""
print("경제" in news )


word = input("물음에 답하세요: ")
result = word in news
print(f"검색하신 단어는  {result}")

# 비밀번호 검증 프로그램
# 사용자로부터 비밀번호 설정을 입력받아. 해당 비밀번호가 느낌표(!)를
#
password = input("비밀 번호 입력:")
result = "!" in password and "IT" in password
print(f"비밀번호가 요구사항을 {result}")
