import streamlit as st
import pandas as pd
from io import StringIO

st.title('탭/파일')

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("CSV 바로읽기")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
 
   df_pop = pd.read_csv('./data/test.csv')
   st.write(df_pop)
   
with tab2:
   st.header("CSV 업로드")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

   uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

with tab3:
   st.header("CSV 멀티업로드")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
   uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
