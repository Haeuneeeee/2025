import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(page_title="대한민국 여행 지도", layout="wide")

st.title("🗺️ 대한민국 여행 추천 지도")

# 지역 데이터 (좌표, 추천 리스트)
regions = {
    "서울": {
        "coords": [37.5665, 126.9780],
        "places": ["경복궁", "남산타워", "광장시장"],
        "activities": ["한강에서 자전거 타기", "홍대 카페 탐방", "전통시장 투어"]
    },
    "부산": {
        "coords": [35.1796, 129.0756],
        "places": ["해운대", "광안리", "태종대"],
        "activities": ["자갈치 시장에서 먹방", "송도 케이블카 타기", "국제시장 구경"]
    },
    "제주": {
        "coords": [33.4996, 126.5312],
        "places": ["한라산", "성산일출봉", "협재 해수욕장"],
        "activities": ["올레길 걷기", "귤 따기 체험", "잠수함 투어"]
    },
    "전주": {
        "coords": [35.8242, 127.1480],
        "places": ["전주 한옥마을", "경기전", "남부시장"],
        "activities": ["한옥마을 한복 체험", "막걸리 골목 투어", "전주비빔밥 먹기"]
    },
    "강릉": {
        "coords": [37.7519, 128.8761],
        "places": ["경포대", "안목해변", "오죽헌"],
        "activities": ["안목 커피거리 산책", "경포호 자전거 타기", "동해 드라이브"]
    }
}

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 깃발 아이콘 추가
for name, info in regions.items():
    folium.Marker(
        location=info["coords"],
        popup=name,
        tooltip=name,
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)

# 지도 출력
map_data = st_folium(m, width=800, height=600)

# 폭죽 + 지역 정보 출력
if map_data["last_object_clicked_popup"]:
    region_name = map_data["last_object_clicked_popup"]

    st.markdown(
        f"<h2 style='color:#ff4b4b;'>🎆 {region_name} 여행 추천 🎆</h2>",
        unsafe_allow_html=True
    )

    st.markdown("**📍 유명한 곳**")
    for place in regions[region_name]["places"]:
        st.write(f"- {place}")

    st.markdown("**✨ 추천 활동**")
    for act in regions[region_name]["activities"]:
        st.write(f"- {act}")

    # 폭죽 이펙트 (랜덤 색상 이모지 뿌리기)
    firework_colors = ["🧨", "🎇", "✨", "🎆", "💥"]
    fireworks = "".join(random.choices(firework_colors, k=30))
    st.markdown(f"<p style='font-size:30px;'>{fireworks}</p>", unsafe_allow_html=True)
