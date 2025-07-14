import streamlit as st
import folium
import json
import pandas as pd
from streamlit_folium import st_folium

st.set_page_config(page_title="미국 흑인 인구 비율 지도", page_icon="🗺️")
st.title("🗺️ 미국 주별 흑인 인구 비율 (2020)")

# JSON 로드
try:
    with open("us_states_black_population.json", "r") as f:
        geojson_data = json.load(f)
except Exception as e:
    st.error("❌ JSON 파일을 불러오는 데 실패했습니다.")
    st.exception(e)
    st.stop()

# JSON에서 데이터 추출
data_list = []
for feature in geojson_data["features"]:
    state = feature["properties"]["name"]
    black_pct = feature["properties"]["black_pct"]
    data_list.append({"State": state, "Black Population %": black_pct})

# pandas DataFrame 생성
df = pd.DataFrame(data_list)

# 지도 생성
m = folium.Map(location=[37.8, -96], zoom_start=4)

# Choropleth 추가
folium.Choropleth(
    geo_data=geojson_data,
    name="choropleth",
    data=df,
    columns=["State", "Black Population %"],
    key_on="feature.properties.name",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="흑인 인구 비율 (%)",
).add_to(m)

# Tooltip 추가
folium.GeoJson(
    geojson_data,
    name="주 정보",
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "black_pct"],
        aliases=["주", "흑인 인구 비율 (%)"],
        localize=True
    )
).add_to(m)

# Streamlit에 지도 표시
st_folium(m, width=800, height=600)
