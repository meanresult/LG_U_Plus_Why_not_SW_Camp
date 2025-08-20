import streamlit as st
st.title('스트림릿 안녕하세요')
st.write('hello ttankkong')

st.divider()

name = st.text_input('이름:   ')
if name :
    st.write(f'안녕하세요..{name}')
    

import pandas as pd

df = pd.read_csv('data/ABNB_stock.csv')
df

# 렌더링함