import streamlit as st

#layout 요소
# columns 요소를 왼쪽에서 오른쪽으로 배치가 가능하게 해줌 ㅋㅋ 개꿀임

col1, col2, col3 = st.columns(3)
with col1: st.metric(
            '오늘의 날씨'
            , value='35도'
            ,delta='+3'
            ,delta_color='normal' # 정상
        )

with col2:  st.metric(
            '오늘의 미세먼지'
            , value='좋음 '
            ,delta='-나빠짐'
            ,delta_color='inverse' # 거꾸로
        )
with col3:  st.metric(
            '오늘의 습도'
            , value='적당히습함'
            ,delta='-습해짐' 
            ,delta_color='off' # 색상을 끔 
        )

## 구분자
st.markdown('---')

data = {
    '이름': ['한지훈', '신땡콩', '안재이'],
    '나이': [31, 32, 31]
}

import pandas as pd
df = pd.DataFrame(data)

st.code('st.dataframe(df)')
st.dataframe(df)

st.divider()

st.code('st.table(df)')
st.table(df)

st.code('st.json(data)')
st.json(data)


# datafile.csv 를 로드하고 table 출력하고 plotly 차트 만들기 개꿀 짱쉬움 ㅋㅋ 

ab_df = pd.read_csv('data/ABNB_stock.csv')
ab_df_head = ab_df.head(3)



st.table(ab_df_head)

import plotly.express as px 
fig = px.scatter(
    data_frame = ab_df
    , x='High'
    , y='Low'
    , width=400
    ,height=400
)
st.plotly_chart(fig)


co_df = pd.read_csv('data/Covid19-india.csv')
co_df_head = co_df.head(3)

st.dataframe(co_df)

fig2 = px.histogram(
    data_frame=co_df
    , x= 'region'
    , y= 'confirmed'
    , width=400
    , height= 400
)
st.plotly_chart(fig2)