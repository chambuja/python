import datetime
import os
# print(os.getlogin())

# desktop_path =os.path.join((os.environ['USERPROFILE']),'Desktop') #"C:\Users\admin\PycharmProjects\2024_04_python"
# folder_name = "오늘은 목요일 "
# folder_path = os.path.join(desktop_path,folder_name)
# os.mkdir(folder_path)    # ==> 바탕 화면에 "오늘은 목요일 디렉 토리 생성"

# ====================
# import os
#
# desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')  # "C:\Users\admin\PycharmProjects\2024_04_python"
# # 바탕 화면 경로와 폴더 이름 합치기
# folder_path = os.path.join(desktop_path, "과장님_부당업무지시폴더")
# # 폴더 만들기
# os.mkdir(folder_path)
#
# # 날짜 가져 오기
# start_date = datetime.date.today()
#
# for x in range(365):
#     date_folder = start_date + datetime.timedelta(days=x)
#     path = os.path.join(folder_path, date_folder.strftime("%M-%m-%d"))
#     os.mkdir(path)
#======================================================================

# 폴더 :용띠의해_5월_23일_목요일
import os
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')  # "C:\Users\admin\PycharmProjects\2024_04_python"
# 바탕 화면 경로와 폴더 이름 합치기
folder_path = os.path.join(desktop_path, "부장님_부당업무지시폴더")
# 폴더 만들기
os.mkdir(folder_path)
start_date = datetime.date.today()

 for x in range(365):
    date_folder = start_date + datetime.timedelta(days=x)
    year_zodiac = yearToZodiac(int(date_folder.strftime("%Y")))
    folder_path
    date_folder.strftime("%M-%m-%d"))
    os.mkdir(path)


















