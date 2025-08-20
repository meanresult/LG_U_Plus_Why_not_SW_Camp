import streamlit as st

st.title('Title')
st.header('header')
st.subheader('subheader')

st.write('write문장입니다.')
st.text('text문장입니다.')

st.divider()

st.markdown(
    '''
    :green[땡컹아 생일축하해]   
    **굵게** *이탤릭체*
    '''
)

st.code(
'''
    st.title('Title')
    st.header('header')
    st.subheader('subheader')
''',
language='python'
)

st.divider()

st.button('Hello') # secondary type
st.button('Hello', type='tertiary')
st.button('Hello', type='primary', icon='🚖',disabled=False, key=9)
st.button('Hello', type='primary', icon='🚖',disabled=False, key=10)

# 레이블이랑 타입이 동일하면 동일한 객체로 판단되어 ID를 주거나 레이블을 바꿔야 함)

############################## button click
def button_write():
    st.write('버튼이 클릭되었습니다')

st.button('Reset', type='primary', icon='🚖')
st.button('activate', on_click=button_write)

clicked = st.button('activate2', type='primary')
if clicked:
    st.write('버튼2가 클릭되엇습니다')
##############################

st.header('같은 버튼 여러개 만들기')
#key=
#activate button 5개 만들기

for i in range(1,6):
    st.button('activate', type='primary', key=i+1)

##############################

st.divider()

