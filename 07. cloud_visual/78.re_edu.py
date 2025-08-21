import streamlit as st
import pandas as pd 
import plotly.express as px
import io
import seaborn as sns 
import re 

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
        "scatter (산점도)",
        "line (선 그래프)",
        "bar (막대 그래프)",
        "histogram (히스토그램)",
        "box (박스 플롯)",
        "violin (바이올린 플롯)",
        "area (영역 차트)",
        "pie (파이 차트)",
        "funnel (퍼널 차트)",
        "funnel_area (퍼널 영역 차트)",
        "sunburst (선버스트 차트)",

        # 시계열 / 통계
        "density_heatmap (밀도 히트맵)",
        "density_contour (밀도 등고선)",
        "ecdf (누적 분포 함수)",
        "imshow (이미지/히트맵)",
        "parallel_coordinates (평행 좌표 플롯)",
        "parallel_categories (평행 카테고리 플롯)",

        # 분포 / 계층
        "treemap (트리맵)",
        "icicle (아이시클 차트)",
        "strip (스트립 플롯)",
        "timeline (타임라인)",
        "scatter_matrix (산점도 행렬)",

        # 지도 시각화
        "choropleth (지역별 색상 지도)",
        "choropleth_mapbox (Mapbox 지역별 지도)",
        "scatter_geo (지리 산점도)",
        "scatter_mapbox (Mapbox 산점도)",
        "density_mapbox (Mapbox 밀도 지도)",
        "line_geo (지리 선 그래프)",
        "line_mapbox (Mapbox 선 그래프)"
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

    #선택한 차트 뒷 설명 제거
    if select_plotly is not None:
        re_chart = re.sub(r"\s*\(.*?\)", "",select_plotly)
 
        chart_func = getattr(px, re_chart) # 텍스트를 함수로 변환 
    
        # 위젯을 활용한 interactive 그래프 표현
        if chart_func is not None:
            fig = chart_func(
                data_frame=dt1
                ,x=ax_xss
                ,y=ax_y
                ,color = ax_hue
                ,width= 500
                ,height= 500
            )
            st.plotly_chart(fig)