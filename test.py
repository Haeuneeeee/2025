import streamlit as st
import folium
from streamlit_folium import st_folium

# 지역별 추천 데이터 (간단 예시)
region_data = {
    "서울": {
        "명소": ["경복궁", "남산타워", "광장시장"],
        "추천": ["한강 자전거 타기", "홍대 거리 산책"]
    },
    "부산": {
        "명소": ["해운대", "광안리 해수욕장", "자갈치 시장"],
        "추천": ["광안대교 야경 보기", "부산 어묵 먹기"]
    },
    "제주": {
        "명소": ["성산일출봉", "한라산", "협재 해수욕장"],
        "추천": ["우도 자전거 여행", "제주 흑돼지 맛보기"]
    },
    "경주": {
        "명소": ["불국사", "석굴암", "첨성대"],
        "추천": ["보문호수 산책", "전통 한옥 체험"]
    }
}

st.title("🇰🇷 대한민국 지역 추천 앱")
st.write("지도를 클릭하면 해당 지역의 명소와 추천할 만한 활동을 알려드려요!")

# 지도 중심: 서울
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 각 지역에 마커 표시
locations = {
    "서울": [37.5665, 126.9780],
    "부산": [35.1796, 129.0756],
    "제주": [33.4996, 126.5312],
    "경주": [35.8562, 129.2247]
}

for region, coords in locations.items():
    folium.Marker(
        location=coords,
        popup=region,
        tooltip=f"{region} 클릭"
    ).add_to(m)

# Streamlit에서 지도 표시
map_data = st_folium(m, width=700, height=500)

# 유저가 클릭한 지역 확인
if map_data and map_data.get("last_object_clicked_popup"):
    clicked_region = map_data["last_object_clicked_popup"]
    if clicked_region in region_data:
        st.subheader(f"📍 {clicked_region} 추천 정보")
        st.markdown("**유명한 곳:**")
        for place in region_data[clicked_region]["명소"]:
            st.write(f"- {place}")
        st.markdown("**추천할 만한 활동:**")
        for activity in region_data[clicked_region]["추천"]:
            st.write(f"- {activity}")
