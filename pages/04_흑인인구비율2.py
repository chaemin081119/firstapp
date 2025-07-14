import streamlit as st
import folium
import json
import pandas as pd
from streamlit_folium import st_folium

st.set_page_config(page_title="미국 흑인 인구 비율 지도", page_icon="🗺️")
st.title("🗺️ 미국 주별 흑인 인구 비율 (2020 기준)")

# 1. 흑인 인구 비율 데이터 (2020, 출처: U.S. Census Bureau 요약)
black_pct_data = {
    "Alabama": 26.8, "Alaska": 3.3, "Arizona": 5.2, "Arkansas": 15.7, "California": 6.5,
    "Colorado": 4.6, "Connecticut": 10.6, "Delaware": 22.2, "District of Columbia": 44.2,
    "Florida": 16.9, "Georgia": 31.1, "Hawaii": 1.6, "Idaho": 1.0, "Illinois": 14.1,
    "Indiana": 9.6, "Iowa": 4.1, "Kansas": 6.1, "Kentucky": 8.5, "Louisiana": 32.2,
    "Maine": 1.7, "Maryland": 31.1, "Massachusetts": 8.6, "Michigan": 13.6, "Minnesota": 7.0,
    "Mississippi": 37.9, "Missouri": 11.5, "Montana": 0.6, "Nebraska": 5.2, "Nevada": 10.3,
    "New Hampshire": 1.9, "New Jersey": 15.1, "New Mexico": 2.6, "New York": 17.6,
    "North Carolina": 21.4, "North Dakota": 3.4, "Ohio": 12.4, "Oklahoma": 7.8, "Oregon": 2.2,
    "Pennsylvania": 11.2, "Rhode Island": 6.5, "South Carolina": 26.5, "South Dakota": 3.0,
    "Tennessee": 16.7, "Texas": 12.2, "Utah": 1.5, "Vermont": 1.5, "Virginia": 20.0,
    "Washington": 4.4, "West Virginia": 3.6, "Wisconsin": 6.3, "Wyoming": 1.2
}

# 2. 원본 GeoJSON 파일 로드
with open("us-states.json", "r") as f:
    geojson_data = json.load(f)

# 3. 각 feature에 흑인 인구 비율 붙이기
for feature in geojson_data["features"]:
    state_name = feature["properties"]["name"]
    black_pct = black_pct_data.get(state_name, None)
    feature["properties"]["black_pct"] = black_pct

# 4. Pandas 데이터프레임 준비
df = pd.DataFrame([
    {"State": name, "Black Population %": pct}
    for name, pct in black_pct_data.items()
])

# 5. Folium 지도 생성
m = folium.Map(location=[37.8, -96], zoom_start=4)

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

folium.GeoJson(
    geojson_data,
    name="주 정보",
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "black_pct"],
        aliases=["주", "흑인 인구 비율 (%)"],
        localize=True
    )
).add_to(m)

# 6. Streamlit에 출력
st_folium(m, width=800, height=600)
