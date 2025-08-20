import streamlit as st
import pandas as pd 
import plotly.express as px
import io
import seaborn as sns 

file = st.file_uploader(
    '파일선택'
    , type='csv'
    , accept_multiple_files=False
)

if file is not None:
    df = pd.read_csv(file)
    
    #데이터info생성
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)   
    
    # 데이터프레임 생성
    st.dataframe(df)
    
    #데이터 전처리 
    
    #데이터차트 시각화 
    fig2 = px.histogram(
    data_frame=df
    , x= df.columns[1]
    , y= df.columns[2]
    , width=400
    , height= 400
    )
    st.plotly_chart(fig2)

###########################################3

dt_list = sns.get_dataset_names()
dt_name_list = [
  "아나그램(단어 퍼즐) 실험 데이터",
  "앤스콤 4분할 데이터셋 (시각화 중요성 예시)",
  "주의력(Attention) 실험 데이터",
  "뇌 신경망 연결 데이터",
  "자동차 교통사고 데이터",
  "다이아몬드 가격 및 특성 데이터",
  "점(dot) 자극 실험 반응 데이터",
  "다우존스 주가지수 데이터",
  "운동 실험 데이터 (심박수, 식단 등)",
  "항공 여객 수 데이터 (1949~1960)",
  "fMRI 뇌 반응 데이터",
  "올드 페이스풀 간헐천 데이터",
  "접착제 성능 실험 데이터",
  "국가별 보건 지출 및 기대수명 데이터",
  "붓꽃(Iris) 품종 데이터",
  "자동차 연비(MPG) 데이터",
  "펭귄(Palmer Penguins) 생태 데이터",
  "외계 행성(Exoplanet) 발견 데이터",
  "해빙(Sea Ice) 면적 변화 데이터",
  "뉴욕 택시 운행 데이터",
  "식당 팁(Tips) 데이터",
  "타이타닉호 생존자 데이터"
]

# selectbox 만들기
option = st.selectbox(
    label='데이터 선택',
    options=dt_list,
    index=None,
    placeholder='데이터를 선택해주세요'
)
st.text('you selected: {}'.format(option))

# 선택한 데이터프레임 가져오기
if option is not None:
    dt1 = sns.load_dataset(format(option))
    st.dataframe(dt1)

    # 데이터타입 분류 
    x_options = dt1.select_dtypes(include=['int64','float64', 'object','datetime64']).columns # x는 연속형, 범주형 또는 날짜형
    y_options = dt1.select_dtypes(include=['int64','float64','object']).columns #y는 연속형
    hue_options = dt1.select_dtypes(include=['object','bool']).columns # 불리언 또는 범주형
    plotly_charts = [
    # 기본 차트
    "Scatter Plot (산점도)",
    "Line Chart (선 그래프)",
    "Bar Chart (막대 그래프)",
    "Histogram (히스토그램)",
    "Box Plot (박스 플롯)",
    "Violin Plot (바이올린 플롯)",
    "Area Chart (영역 차트)",
    "Pie Chart (파이 차트)",
    "Donut Chart (도넛 차트)",
    "Funnel Chart (퍼널 차트)",
    "Bullet Chart (불릿 차트)",

    # 시계열 / 통계
    "Time Series Line Chart (시계열 선 그래프)",
    "Stacked Area Chart (누적 영역 차트)",
    "Stacked Bar Chart (누적 막대 그래프)",
    "Density Heatmap (밀도 히트맵)",
    "2D Histogram (2차원 히스토그램)",
    "2D Density Contour (밀도 등고선)",

    # 분포 관련
    "ECDF Plot (누적 분포 함수)",
    "KDE Plot (커널 밀도 추정)",
    "Sunburst Chart (선버스트 차트)",
    "Treemap (트리맵)",
    "Icicle Chart (아이시클 차트)",

    # 지도 시각화
    "Choropleth Map (지역별 색상 지도)",
    "Scatter Mapbox (위치 산점도 지도)",
    "Bubble Map (버블 지도)",
    "Density Mapbox (밀도 지도)",
    "Geo Scatter Plot (위도/경도 산점도)",

    # 고급 차트
    "3D Scatter Plot (3차원 산점도)",
    "3D Surface Plot (3D 표면 그래프)",
    "3D Line Plot (3차원 선 그래프)",
    "3D Mesh Plot (3D 메쉬 그래프)"
    ]
    
    print('*'*30)
    print(x_options)

    # 데이터 축 선택
    ax_x = st.selectbox(
        label='x축 선택'
        ,options=x_options
        ,index=None
        ,placeholder='x축을 선택해주세요'
    )

    ax_y = st.selectbox(
        label='y축 선택'
        ,options=y_options
        ,index=None
        ,placeholder='y축을 선택해주세요'
    )

    ax_hue = st.selectbox(
        label='hue 선택'
        ,options=hue_options
        ,index=None
        ,placeholder='hue 데이터 선택해주세요' 
    )

    select_plotly = st.selectbox(
        label ='chart 선택'
        ,options = plotly_charts
        ,index = None
        ,placeholder = '차트를 선택해주세요' 
    )
    
    pl = select_plotly
    # 위젯을 활용한 interactive 그래프 표현
    fig = px.select_plotly(
        data_frame=dt1
        ,x=ax_x
        ,y=ax_y
        ,color = ax_hue
        ,width= 500
        ,height= 500
    )
    st.plotly_chart(fig)