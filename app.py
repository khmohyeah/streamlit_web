import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

#페이지 기본 설정
st.set_page_config(
    page_icon="○",
    page_title="스트림릿배포하기",
    layout="wide",
)

#페이지 헤더, 서브헤더 제목 설정
st.header("스트림릿 오신걸 환영합니다.")
st.subheader("스트림릿 기능 맛보기")

#페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
cols = st.columns((1,1,2))
cols[0].metric("10/11", "15ºC", "2")
cols[0].metric("10/11", "15ºC", "2")
cols[0].metric("10/11", "15ºC", "2")
cols[1].metric("10/11", "15ºC", "2")
cols[1].metric("10/11", "15ºC", "2")
cols[1].metric("10/11", "15ºC", "2")

#라인 그래프 데이터 생성(Width, Pandas)
chart_data = pd.DataFrame(
    np.random.rand(20, 3), 
    columns=['a', 'b', 'c']
)

cols[2].line_chart(chart_data)