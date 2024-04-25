#data-type : int ,str ,float ,bool ,
# list , set : 집합 (중복안됨)
a = {1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7}
burgerking = {"새우와퍼","불고기와퍼","치즈와퍼","스테이크와퍼"}
momstouch = {"새우와퍼","치즈와퍼","싸이버거","블고기와퍼"}
x = burgerking.intersection(momstouch)
print(x)

#==================
{'새우와퍼', '치즈와퍼'}
#=======================
# 합집합(|)
union = burgerking | momstouch

#교집합 (&)
intersection = burgerking & momstouch




# add [추가]
# burgerking.add("에그와퍼")
#삭제
# burgerking.remove("새우와퍼") # 구문법 없는 요소 빼면 에러
# burgerking.discard("새우와퍼")
#전체삭제
# burgerking.clear()

news ="""The European Commission said Tuesday that it carried out “unannounced inspections” at the premises of a company making and selling security equipment in Europe, which it suspects may have benefited unduly from state subsidies. It did not name the company."""
wordList = news.split()
noDuplitionwords = list(set(wordList))
noDuplitionwords.sort()
print(noDuplitionwords)
