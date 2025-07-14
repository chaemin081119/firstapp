import streamlit as st
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="미국 흑인 인구 비율 추이", page_icon="📊")

st.title("📊 1800년부터 2020년까지 미국 흑인 인구 비율")
st.write("아래는 미국 전체 인구 대비 흑인 인구 비율의 역사적 변화입니다.")

# 연도별 샘플 데이터 (출처: US Census, 요약)
years = [
    1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870,
    1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950,
    1960, 1970, 1980, 1990, 2000, 2010, 2020
]

black_population_percentage = [
    18.9, 19.0, 18.4, 18.1, 16.8, 15.8, 14.1, 13.0,
    12.8, 11.9, 11.6, 10.7, 9.9, 9.7, 9.8, 10.0,
    10.5, 11.1, 11.7, 12.1, 12.3, 12.6, 12.4
]

# Plotly 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=years,
    y=black_population_percentage,
    mode='lines+markers',
    name='흑인 인구 비율 (%)',
    line=dict(color='darkgreen', width=3),
    marker=dict(size=7)
))

# 레이아웃 설정
fig.update_layout(
    title="미국 흑인 인구 비율 변화 (1800–2020)",
    xaxis_title="연도",
    yaxis_title="흑인 인구 비율 (%)",
    template="plotly_white"
)

# Streamlit에 그래프 출력
st.plotly_chart(fig)
