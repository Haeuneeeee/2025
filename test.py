import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(page_title="대한민국 여행 지도", layout="wide")
st.title("🗺️ 대한민국 여행 지도")
st.write("깃발을 클릭하면 🎆 폭죽과 함께 해당 지역의 추천 명소가 나와요!")

# 지역 데이터
regions = {
    "서울": {"coords": [37.5665, 126.9780], "places": ["경복궁", "남산타워", "명동", "광장시장", "한강공원"]},
    "부산": {"coords": [35.1796, 129.0756], "places": ["해운대", "광안리 해수욕장", "자갈치 시장", "태종대"]},
    "제주": {"coords": [33.4996, 126.5312], "places": ["성산일출봉", "한라산", "협재해수욕장", "우도", "용머리해안"]},
    "전주": {"coords": [35.8242, 127.1480], "places": ["전주 한옥마을", "경기전", "남부시장 야시장", "풍남문"]},
    "강릉": {"coords": [37.7519, 128.8761], "places": ["경포대", "안목해변", "주문진 수산시장", "정동진"]},
    "대전": {"coords": [36.3504, 127.3845], "places": ["유성온천", "엑스포과학공원", "한밭수목원", "대청호"]},
    "대구": {"coords": [35.8714, 128.6014], "places": ["동성로", "팔공산", "서문시장", "앞산공원"]},
    "광주": {"coords": [35.1595, 126.8526], "places": ["무등산", "양림동 역사문화마을", "국립아시아문화전당", "충장로"]},
}

# 대한민국 중심 좌표
map_center = [36.5, 127.8]
m = folium.Map(location=map_center, zoom_start=7)

# 깃발 아이콘 추가
for city, data in regions.items():
    folium.Marker(
        location=data["coords"],
        popup=f"<b>{city}</b>",
        tooltip=city,
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)

# 지도 표시
map_result = st_folium(m, width=900, height=600)

# 클릭 이벤트 처리
if map_result["last_object_clicked_tooltip"]:
    city = map_result["last_object_clicked_tooltip"]
    st.markdown(f"""
        <div style='font-size:24px; font-weight:bold; color:#FF4B4B;'>🎆 {city} 여행 추천 🎆</div>
    """, unsafe_allow_html=True)

    # 폭죽 효과 (랜덤 색상으로 터지듯 보이게)
    for _ in range(10):
        st.markdown(
            f"<div style='color: rgb({random.randint(100,255)}, {random.randint(100,255)}, {random.randint(100,255)}); font-size:20px;'>✨ 팡!</div>",
            unsafe_allow_html=True
        )

    # 추천 장소 출력
    st.subheader(f"{city}의 유명한 곳")
    for place in regions[city]["places"]:
        st.write(f"✅ {place}")
