import streamlit as st

st.markdown('## This is markdown')
st.markdown('Streamlit is **_really_ cool**.')

st.caption('This is a string that explains something above.')

code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')
