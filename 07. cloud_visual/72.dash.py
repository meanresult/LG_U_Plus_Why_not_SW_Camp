from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# 앱 생성
app = Dash(__name__)

# 레이아웃 정의
app.layout = html.Div([
    html.H4('Interactive scatter plot with Iris dataset'),
    dcc.Graph(id="scatter-plot"),
    html.P("Filter by petal width:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=2.5, step=0.1,
        marks={0: '0', 2.5: '2.5'},
        value=[0.5, 2]
    ),
])


@app.callback(
    Output("scatter-plot", "figure"),
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    df = px.data.iris() # replace with your own data source
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length",
        color="species", size='petal_length',
        hover_data=['petal_width'])
    return fig

# 서버 실행
app.run(debug=True)

#python app.py


# 📌 Dash란?
# Plotly 기반 웹 애플리케이션 프레임워크
# 파이썬 코드만으로도 웹 페이지처럼 동작하는 대시보드를 만들 수 있음
# Flask(웹 서버) + Plotly(시각화) + React.js(프론트엔드)를 조합해서 내부적으로 동작
# → 하지만 사용자는 복잡한 웹 개발을 몰라도 됨

# 📊 Dash의 주요 특징
# 파이썬만 알면 된다
# HTML, CSS, JavaScript 몰라도 웹 애플리케이션을 만들 수 있음
# 대화형(Interactive) 지원
# 버튼 클릭, 드롭다운 선택, 슬라이더 조정 등 사용자 입력에 따라 그래프가 실시간으로 변함
# Plotly와 완벽 통합
# Plotly 그래프를 그대로 대시보드에 넣을 수 있음
# BI 도구 대체 가능0
# 기업에서 쓰는 Tableau, Power BI처럼 데이터를 시각화·공유하는 용도로 활용 가능