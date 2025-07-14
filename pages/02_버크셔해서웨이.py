import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Streamlit 기본 설정
st.set_page_config(page_title="BRK.A 주가 추이", page_icon="📈")

st.title("📈 버크셔 해서웨이 A (BRK.A) - 5년 주가 추이")
st.write("이 그래프는 2019년부터 2024년까지의 버크셔 해서웨이 A 주가 흐름을 시각화한 예시입니다.")

# 샘플 날짜 (연간)
dates = [
    datetime(2019, 1, 1),
    datetime(2020, 1, 1),
    datetime(2021, 1, 1),
    datetime(2022, 1, 1),
    datetime(2023, 1, 1),
    datetime(2024, 1, 1),
]

# 샘플 종가 데이터 (실제 BRK.A 가격대 반영한 예시)
prices = [
    313000,  # 2019
    340000,  # 2020
    390000,  # 2021
    480000,  # 2022
    460000,  # 2023
    540000   # 2024
]

# Plotly 그래프 생성
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=dates,
    y=prices,
    mode='lines+markers',
    name='BRK.A 주가',
    line=dict(color='royalblue', width=3),
    marker=dict(size=8)
))

# 그래프 레이아웃 설정
fig.update_layout(
    title="버크셔 해서웨이 A (BRK.A)의 연도별 주가",
    xaxis_title="연도",
    yaxis_title="주가 (USD)",
    template="plotly_white"
)

# Streamlit에 그래프 표시
st.plotly_chart(fig)
