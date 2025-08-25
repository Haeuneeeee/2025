import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_extras.let_it_rain import rain

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 지역 정보
locations = {
    "서울": [37.5665, 126.9780],
    "부산": [35.1796, 129.0756],
    "제주": [33.4996, 126.5312],
    "전주": [35.8242, 127.1480],
    "강릉": [37.7519, 128.8761],
    "대전": [36.3504, 127.3845],
    "대구": [35.8714, 128.6014],
    "광주": [35.1595, 126.8526]
}

famous_places = {
    "서울": ["경복궁", "남산타워", "광화문"],
    "부산": ["해운대", "광안리", "자갈치 시장"],
    "제주": ["한라산", "성산일출봉", "협재 해수욕장"],
    "전주": ["한옥마을", "비빔밥", "경기전"],
    "강릉": ["경포대", "안목 커피거리", "정동진"],
    "대전": ["엑스포과학공원", "유성온천", "대전오월드"],
    "대구": ["동성로", "서문시장", "팔공산"],
    "광주": ["무등산", "5.18 민주광장", "충장로"]
}

# 깃발 버튼 표시
for city, coord in locations.items():
    folium.Marker(
        location=coord,
        popup=folium.Popup(f"<b>{city}</b>", max_width=200),
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)

st_map = st_folium(m, width=700, height=500)

# 선택된 지역 출력 + 폭죽 효과
if st_map["last_object_clicked_popup"]:
    city = st_map["last_object_clicked_popup"]
    st.subheader(f"🎉 {city}의 유명한 장소 🎉")
    
    for place in famous_places[city]:
        st.write(f"✨ {place}")
    
    # 반짝이 효과 (rain 사용)
    rain(
        emoji="✨",
        font_size=40,
        falling_speed=5,
        animation_length="infinite"
    )
