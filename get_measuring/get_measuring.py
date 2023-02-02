import psycopg2
from urllib.parse import urlencode, quote_plus, unquote
import urllib.request, bs4
import requests
import folium as g
import pandas as pd
import numpy as np
import pyproj

school = input()

# 학교 id 조회
con_string = "host='localhost' dbname ='postgres' user='postgres' password='9407740'"
con = psycopg2.connect(con_string)

cur = con.cursor()
sql = "SELECT id, name, latitude, longitude from school_info where name LIKE'%"
sql += school
sql += "%'"
cur.execute(sql)
school_list = cur.fetchall()

# tm 좌표 조회
sql = "SELECT id, tm_x,  tm_y from school_tm where id='"
sql += school_list[0][0]
sql += "'"

cur.execute(sql)
school_tm_list = cur.fetchall()

school_tmX = school_tm_list[0][1]
school_tmY = school_tm_list[0][2]

# 근접측정소 조회
url = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'
key = unquote('-------')

key = requests.utils.unquote(key)
queryParams = '?' + urlencode({
            quote_plus('ServiceKey') : key,
            quote_plus('tmX') : school_tmX,
            quote_plus('tmY') : school_tmY,
            quote_plus('returnType') : 'xml'
            })

request_api = requests.get(url + queryParams).text.encode('utf-8')
station_info = bs4.BeautifulSoup(request_api, 'lxml-xml')

station_name = station_info.find_all("stationName")
station_name = [station_name[i].text for i in range(len(station_name))]
tm_dis = station_info.find_all("tm")
tm_dis = [tm_dis[i].text for i in range(len(tm_dis))]

print(station_name)
print(tm_dis)

pm10 = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
]

pm25 = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
]

dataTime = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
            "0", "0"]

location = [[0, 0], [0, 0], [0, 0]]

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
url_location = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'

for i in range(len(station_name)):
    queryParams = '?' + urlencode({
        quote_plus('ServiceKey'): key,
        quote_plus('numOfRows'): '30',
        quote_plus('pageNo'): '1',
        quote_plus('stationName'): station_name[i],
        quote_plus('dataTerm'): 'DAILY',
        quote_plus('ver'): '1.2'
    })

    queryParams1 = '?' + urlencode({
        quote_plus('ServiceKey'): key,
        quote_plus('returnType'): 'xml',
        quote_plus('numOfRows'): '10',
        quote_plus('pageNo'): '1',
        quote_plus('stationName'): station_name[i]
    })

    # 측정소 데이터 가져오기
    request_api = requests.get(url + queryParams).text.encode('utf-8')
    measuring_data_info = bs4.BeautifulSoup(request_api, 'lxml-xml')
    tmp = measuring_data_info.find_all("pm10Value")
    pm10[i] = [j.text for j in tmp]
    tmp = measuring_data_info.find_all("pm25Value")
    pm25[i] = [j.text for j in tmp]

    # 측정소 위경도 가져오기
    location_request_api = requests.get(url_location + queryParams1).text.encode('utf-8')
    ll_data_info = bs4.BeautifulSoup(location_request_api, 'lxml-xml')
    location[i][0] = ll_data_info.find("dmX").text
    location[i][1] = ll_data_info.find("dmY").text

tmp = measuring_data_info.find_all("dataTime")
dataTime = [j.text for j in tmp]

print(pm10)
print(pm25)
print(dataTime)