# 퀴즈
# 정수배열 arr 와 자연수 k
# arr[]
#k= int(input("수자입력: ")
# k가 홀수라면 if x %2 ==1 x*k   else  x + k
arr1 = [1,2,3,100,99,98]
k= int(input("숫자입력: "))
# result =[]
def solution1(arr1,k):
    return [x *k if k %2 ==1 else x+k for x in arr1]
print(solution1(arr1,2)) #[3, 4, 5, 102, 101, 100]

print(solution1(arr1,3))#[3, 6, 9, 300, 297, 294]



# # A강조하기 ============
# 문자열 myString   "a" ==> 전부 "A"
# "A가 아닌 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는
 solution1함수 만들기
mySring = "absrtact algebra"
def solution1(myString):
    return "".join(['A' if x =='a' else x.lower for x in myString])
print(mySring)
    if x =="a":
        mySring.upper()

    elif x !=="a":
        myString

#===============================
# a = [05-24,05-25,.....06-24] #리스트만들기
# b = a[YY-MM]

# import  datetime
#
# def solution3(x):
#
#     today = datetime.date.today()
#     future_time = today + datetime.timedelta(days=x)
#     return future_time.strftime("%m-%d")
# a = [solution3(x) for x in range(31)]
# print(a)
#
#
# b = a.split(a[YY-MM])
# print(b)
#
# a.list[]


# #==========================================
#
# class Solution {
#     public int[] solution(int[] arr, int k) {
#     int[] answer = new int[arr.length];
#
#     for (int i=0; i < arr.length; i++){
#         if (k % 2 == 0){
#             answer[i]=arr[i]+k;
#         } else {
#             answer[i]=arr[i] * k;
#         }
#         }
#
#         return answer;
#     }
# }

