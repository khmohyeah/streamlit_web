import streamlit as st
import pandas as pd
import numpy as np
import datetime
import geopy
from geopy.geocoders import Nominatim

st.title('아파트매매실거래가정보 : 경기도 20220301~20230228')

# 엑셀에서 데이터 조회
df = pd.read_csv('./data/경기도아파트실거래가_20220301_20230228.csv', encoding='cp949')

# 전체 목록 표시
st.subheader("전체")
if st.checkbox('전체 Show raw data'):
    st.write(df)

# 선택 목록 표시
st.subheader("선택")

# 조회조건 레이아웃
cols = st.columns((1,1,3))

# 조회기간 From~To
fromDt = cols[0].date_input("FROM", datetime.date(2022, 3, 1))
toDt = cols[1].date_input("TO", datetime.date(2023, 2, 28))

fromDt = str(fromDt).replace("-", "")[0:6]
toDt = str(toDt).replace("-", "")[0:6]

# 시군구 선택 
option = cols[2].selectbox('시군구를 선택하세요', df['시군구'].unique())

# 필터처리
df2 = df.loc[(df['시군구'] == option) 
             & (df['계약년월ORG'] >= int(fromDt))
             & (df['계약년월ORG'] <= int(toDt))
            ]
if st.checkbox('선택 Show raw data'):
    st.write(df2)

# 차트 데이터
arrDangi = df2['단지명'].unique()
arrYymm = df2['계약년월'].unique()
arrAddress = df2['도로명'].unique()
chart_data = pd.DataFrame(arrYymm)
chart_data.columns = ['계약년월']

# 차트데이터 초기화
for i in range(arrDangi.size):
    chart_data.insert(i+1, arrDangi[i], 0)  # 단지추가
chart_data = chart_data.set_index('계약년월')

# 최대값 데이터
chart_data1 = chart_data.copy()

# 최소값 데이터
chart_data2 = chart_data.copy()

#차트데이터 값셋팅
for index, row in df2.iterrows():
    chart_data[row['단지명']][row['계약년월']] = chart_data[row['단지명']][row['계약년월']] + 1

# 단지 옵션
options = st.multiselect('단지를 선택하세요', arrDangi, arrDangi)

# 데이터 표시
if st.checkbox('월별 거래건수 Show raw data'):
    st.dataframe(chart_data)

# 차트 표시
st.subheader("월별 거래건수 차트")
chart_data = pd.DataFrame(chart_data, columns=options)
st.line_chart(chart_data)

############# 최대값 #############

#차트데이터 값셋팅
for index, row in df2.iterrows():
    if int(chart_data1[row['단지명']][row['계약년월']]) < int(row['거래금액(만원)']) :
        chart_data1[row['단지명']][row['계약년월']] = row['거래금액(만원)']

# 데이터 표시
if st.checkbox('월별 거래금액(최대값) Show raw data'):
    st.dataframe(chart_data1)

# 차트 표시
st.subheader("월별 거래금액(최대값) 차트")
chart_data1 = pd.DataFrame(chart_data1, columns=options)
st.line_chart(chart_data1)

# 지도 표시
def geocoding(address) : 
    crd = ""
    geolocoder = Nominatim(user_agent='South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    if geo != None :
        crd = {"lat" : str(geo.latitude), "lon" : str(geo.longitude)}
    return crd



st.subheader("지도보기")
with st.expander("Open Map") :
    #지도 위에 표시될 점 좌표 값을 위도경도에 담습니다 .
    map_data = pd.DataFrame(columns=['lat', 'lon'])
    for i in range(arrAddress.size):
        crd = geocoding(arrAddress[i])
        if crd != "" :
            map_position = pd.DataFrame(
                {'lat': [float(crd['lat'])], 'lon': [float(crd['lon'])]})
            map_data = pd.concat([map_data, map_position])

    # Map 생성 
    # myMap.save('index.html')
    st.map(map_data)