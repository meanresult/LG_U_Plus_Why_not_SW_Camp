import streamlit as st
from PIL import Image

####################사이드바에 위젯 배치하기
st.title('앱 페이지 구성하기 실습')

st.sidebar.header('메뉴')
selected = st.sidebar.selectbox(
    '메뉴 선택',
    ['메인', '분석', '설정']
)

if st.sidebar.button('선택'):
    st.sidebar.write('낚시지롱~')
    
#슬라이드바 추가 0~100, 50
st.sidebar.slider(
    label= '슬라이드바',
    min_value= 0,
    max_value= 100,
    value= 50,
    step=10,
    key=2
)


########################### 함수영역
# tab추가
def make_anal_tab():
    st.header('탭추가')

    tab1, tab2, tab3 = st.tabs(['차트', '데이터', '설정'])
    with tab1:
        st.subheader('차트 탭')
        st.bar_chart({'데이터':[1,2,3,4,5]})
        
    with tab2:
        st.subheader('데이터 탭')
        st.bar_chart({'기준':['a','b','c','d','e'],'값':[1,2,3,4,5]})
        

    #3번재 탭 : 체크박스(활성화여부) 슬라이더(업데이트 주기 sec)
    with tab3:
        st.subheader('설정 탭')
        st.checkbox(
            label = '자동업데이트 활성화여부'
        )
        st.slider(
            label='슬라이더1'
            , max_value=100
            , min_value=10
            , key=3
            )
########################### 메인영역

if selected == '메인':
    st.subheader('*메인페이지')
    st.write('환영합니다')
    
    # 화면 이어서 넣기
    # col1, col2 = st.columns(2)
    
    # with col1:
    img = Image.open('image/image1.jpg')
    st.image(img, width=1000, caption=None)
    
    # with col2:
    #     img = Image.open('image/image1.jpg')
    #     st.image(img, width=1000, caption=None)
    
elif selected == '분석':
    st.subheader('분석 보고서')
    st.write('여기서 데이터를 선택하실 수 있습니다')
    make_anal_tab()
    

elif selected == '설정':
    st.subheader('설정변경')
    

    
######################### [공통]확장영역 추가 

st.header('익스펜더 추가')
with st.expander('숨긴 영역'):
    st.write('여기는 보이지 않습니다. 클릭해야 보입니다')
    img = Image.open('image/image1.jpg')
    st.image(img, width=1000, caption=None)


    