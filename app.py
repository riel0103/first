import streamlit as st
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pw):
    cur.execute(f"SELECT * "
                f"FROM users "
                f" WHERE id='{id}' and pwd= '{pw}'")
    return cur.fetchone()

menu = st.sidebar.selectbox('MENU', options=['로그인', '회원가입', '회원목록'])

if menu == '로그인':
    st.subheader('로그인')

    login_id = st.text_input('아이디', placeholder='아이디를 입력하세요.')
    login_pw = st.text_input('비밀번호', placeholder='비밀번호를 입력하세요.', type='password')

    login_btn = st.button('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)
        st.write(user_info[4], '님 환영합니다.')
    st.sidebar.subheader('로그인')
if menu == '회원가입':
    st.subheader('회원가입')
    st.sidebar.write('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    st.sidebar.write('회원목록')