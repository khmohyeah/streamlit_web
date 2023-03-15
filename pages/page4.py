from PublicDataReader import TransactionPrice
import streamlit as st

st.title('공공데이터 API')

service_key = ""

st.write('인코딩 : UExrnbEJ2ijrWB%2F%2BYOtLk491LQbJRhQYvIy3gJAP9cxc9kiEvclmb7Y%2BqFfmLNFdbR%2FwVWUA6HUtcfZvIC4Haw%3D%3D')
st.write('디코딩 : UExrnbEJ2ijrWB/+YOtLk491LQbJRhQYvIy3gJAP9cxc9kiEvclmb7Y+qFfmLNFdbR/wVWUA6HUtcfZvIC4Haw==')

service_key = st.text_input(
'서비스키', 'UExrnbEJ2ijrWB/+YOtLk491LQbJRhQYvIy3gJAP9cxc9kiEvclmb7Y+qFfmLNFdbR/wVWUA6HUtcfZvIC4Haw==')

api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="아파트",         # 부동산 상품 종류(아파트, 오피스텔, 단독다가구 등)
    trade_type="매매",              # 부동산 거래 유형(매매, 전월세)
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="아파트",         # 부동산 상품 종류(아파트, 오피스텔, 단독다가구 등)
    trade_type="매매",              # 부동산 거래 유형(매매, 전월세)
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()