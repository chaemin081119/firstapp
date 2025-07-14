import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# Streamlit 설정
st.set_page_config(page_title="미국 흑인 인구 지도", page_icon="🗺️")
st.title("🗺️ 미국 주별 흑인 인구 비율 지도")

st.write("이 지도는 Folium을 사용하여 각 주별 흑인 인구 비율을 시각화합니다.")

# 미국 중심 좌표
m = folium.Map(location=[37.8, -96], zoom_start=4)

# GeoJSON 로드
with open("us_states_black_population.json", "r") as f:
    data = json.load(f)

# Choropleth 레이어 추가
folium.Choropleth(
    geo_data=data,
    name="choropleth",
    data=data,
    columns=["properties.name", "properties.black_pct"],
    key_on="feature.properties.name",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="흑인 인구 비율 (%)",
).add_to(m)

# Tooltip 추가
folium.GeoJsonTooltip(fields=["name", "black_pct"],
                      aliases=["주", "흑인 인구 비율 (%)"],
                      sticky=False).add_to(folium.GeoJson(data).add_to(m))

# 지도 표시
st_folium(m, width=800, height=600)
