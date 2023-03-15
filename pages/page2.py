import PublicDataReader as pdr
import streamlit as st

st.title('시군구코드 조회')

#주소
sigunguName = st.text_input(
'주소입력', '성남시')
st.write('')

st.write('시군구/읍면동 : ', sigunguName)
code = pdr.code_bdong()
code.loc[(code['시군구명'].str.contains(sigunguName, na=False)) &
          (code['읍면동명'].isna())]
