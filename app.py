import streamlit as st
import sqlite3
import pandas as pd
import os.path

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
    st.sidebar.subheader('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)
        file_name = './img/'+user_info[0]+'.png'

        if os.path.exists(file_name):
            st.sidebar.image(file_name)
            st.sidebar.write(user_info[4], '님 환영합니다.')
        else:
            st.write(user_info[4], '님 환영합니다.')
if menu == '회원가입':
    st.subheader('회원가입')
    if menu == '회원가입':

        st.info('다음 양식을 모두 입력 후 제출합니다.')
        uid = st.text_input('아이디', max_chars=10)
        uname = st.text_input('성명', max_chars=10)
        upw = st.text_input('비밀번호', type='password')
        upw_chk = st.text_input('비밀번호 확인', type='password')
        uage = st.text_input('생년월일')
        ugender = st.radio('성별', options=['남', '여'], horizontal=True)

        ubtn = st.button('회원가입')
        if ubtn:
            if upw != upw_chk:
                st.error('비밀번호가 일치하지 않습니다.')
                st.stop()

            cur.execute(f"INSERT INTO users(id, pwd, gender, age, name) "
                        f"VALUES('{uid}', '{upw}', '{ugender}', {uage}, '{uname}')")
            st.success('회원가입에 성공했습니다.')
            con.commit()
if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql('SELECT name,age,gender FROM users', con)
    st.dataframe(df)
    st.sidebar.write('회원목록')
