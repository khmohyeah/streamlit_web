import streamlit as st
import numpy as np

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )


st.dataframe(np.random.randn(20, 3))
st.write(np.random.randn(20, 3))


users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
         {'mail': 'hintoncynthia@hotmail.com',
             'name': 'Madison Martinez', 'sex': 'F'},
         {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
         {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
         {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]

st.dataframe(users)
st.write(users)
