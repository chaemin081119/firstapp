import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CO₂ Emissions Dashboard", layout="wide")

st.title("🚗 CO₂ Emissions Dashboard")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 기본 통계
    st.subheader("📊 데이터 미리보기")
    st.dataframe(df.head())

    # 선택 필터
    manufacturers = df["Make"].unique()
    selected_make = st.multiselect("제조사 선택", manufacturers, default=manufacturers[:5])

    filtered_df = df[df["Make"].isin(selected_make)]

    # 평균 CO2 배출량 시각화
    co2_by_make = (
        filtered_df.groupby("Make")["CO2 Emissions(g/km)"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    st.subheader("🏭 제조사별 평균 CO₂ 배출량")
    fig = px.bar(
        co2_by_make,
        x="Make",
        y="CO2 Emissions(g/km)",
        color="CO2 Emissions(g/km)",
        color_continuous_scale="Reds",
        title="제조사별 평균 CO₂ 배출량 (g/km)",
    )
    st.plotly_chart(fig, use_container_width=True)

    # 연료 종류별 분석
    st.subheader("⛽ 연료 종류별 CO₂ 배출량 분포")
    fig2 = px.box(
        filtered_df,
        x="Fuel Type",
        y="CO2 Emissions(g/km)",
        color="Fuel Type",
        title="연료 종류별 CO₂ 배출량",
    )
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("왼쪽 사이드바에서 CSV 파일을 업로드하세요.")
