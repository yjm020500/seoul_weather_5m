# 5분마다 한 번씩 서울의 기온 정보를 csv형태로 저장
import requests
import csv
from datetime import datetime #시계열 데이터 다루는 라이브러리
import os

MY_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Seoul"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={MY_API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

#서울 기온 하나
temp = data["main"]["temp"]
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #현재 시각 찍기

csv_filename = "seoul_weather.csv"
header = ["time", "temp"]

# "seoul_weather.csv"가 없다면 새로 생성
# 만약 있다면 갱신
file_exist = os.path.isfile(csv_filename)

with open(csv_filename, "a", newline="") as file: #추가 모드
    writer = csv.writer(file)
    
    #만약 csv가 없다면 헤더도 없다
    if not file_exist:
        writer.writerow(header)

    writer.writerow([time, temp]) #파일에 data 쓰기

    print("서울 기온 저장 완료")
