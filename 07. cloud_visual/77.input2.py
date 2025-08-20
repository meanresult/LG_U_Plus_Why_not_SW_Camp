import streamlit as st 

# check box 

def on_change2() :
    st.text('안녕하세요')
    
active = st.checkbox('I agree')
st.checkbox('안녕하세요', on_change=on_change2)

if active:
    st.text('welcome 신땡컹')
    
# 함수, on_change=checkbox_write 
def checkbox_write():
    st.write('뭐먹을래?')
    
st.checkbox('배고파', on_change=checkbox_write)


## 세션-상태 값에 저장
# if 'checkbox_state' not in st.session_state:
#     st.session_state.checkbox_state = False
    
# def checkbox_writel():
#     st.session_state.checkbox_state :
#         st.write('응....')
        
# st.checkbox('진짜 누를래?', on_change=checkbox_writel)

st.divider()

#토글 버튼
selected = st.toggle('밥먹어야지!')
if selected:
    st.text('뭐먹을래')
else:
    st.text('좀 참아')
    

#selectbox 선택지

option = st.selectbox(
    '점심메뉴고르기',
    options=['김밥', '떡볶이', '라면', '돈까스'],
    index=None,
    placeholder='네개 중 하나만 골라'
)

st.text(f'오늘의 점심메뉴는: {option}')
    
    
# radio - 한개만 선택 

genre = st.radio(
    '무슨 영화를 좋아하세요', ['멜로', '스릴러', '코미디'],
    captions=['봄날은 간다', '트리거', '웬즈데이']
)
st.text(f'당신이 좋아하는 장르는 {genre}')

# multiselect

menus  = st.multiselect(
    '먹고싶은 거 다골라',
    ['김밥', '떡볶이', '라면', '돈까스']
)
st.text(f'내가 선택한 메뉴는 {menus}')

#slider

score = st.slider('내 점수 선택', 0,100,19) # start, end, init-value
st.text(f'score:{score}')

from datetime import time
st_time, end_time = st.slider(
    '공부시간선택'
    , min_value= time(0)
    , max_value= time(23)
    , value=(time(8), time(18))
    , format='HH:mm'
)

st.text(f'공부시간:{st_time} ~ {end_time}' )

# text_input

txt1 = st.text_input('영화제목', placeholder='제목을 입력하세요')
txt2 = st.text_input('비밀번호', placeholder='비밀번호를 입력하세요', type='password')

st.text(f'텍스트 입력결과 : {txt1}, {txt2}')

# 파일업로더
# 업로드한 파일은 사용자의 세션에 있습니다. 화면을 갱신하면 사라집니다.
# 서버에 저장하려면 별도로 구현해야 하바니다.
# 데이터베이스에 저장하는 도구는 
import pandas as pd 

file = st.file_uploader(
    '파일선택'
    , type='csv'
    , accept_multiple_files=False
)

if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
with open(file.name, 'wb') as out:
    out.write(file.getbuffer())
