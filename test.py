import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="대한민국 지역 추천기", layout="wide")

# 지역별 추천 데이터
regions = {
    "서울": {
        "coords": [37.5665, 126.9780],
        "famous": ["경복궁", "남산타워", "한강"],
        "food": ["불고기", "비빔밥"],
        "activity": ["한강 자전거 타기", "북촌 한옥마을 산책"],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Gyeongbokgung_Palace_%28Keongbokgung%29_2014-09-16.jpg/800px-Gyeongbokgung_Palace_%28Keongbokgung%29_2014-09-16.jpg"
    },
    "부산": {
        "coords": [35.1796, 129.0756],
        "famous": ["해운대", "광안리", "자갈치 시장"],
        "food": ["밀면", "돼지국밥"],
        "activity": ["해운대 바다 산책", "광안대교 야경 감상"],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Haeundae_Beach_Busan_South_Korea.jpg/800px-Haeundae_Beach_Busan_South_Korea.jpg"
    },
    "제주": {
        "coords": [33.4996, 126.5312],
        "famous": ["한라산", "성산일출봉", "협재 해수욕장"],
        "food": ["흑돼지", "갈치조림"],
        "activity": ["올레길 걷기", "동굴 탐험"],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Jeju_Island_Seongsan_Ilchulbong.jpg/800px-Jeju_Island_Seongsan_Ilchulbong.jpg"
    },
    "전주": {
        "coords": [35.8151, 127.1406],
        "famous": ["전주 한옥마을", "경기전"],
        "food": ["전주비빔밥", "콩나물국밥"],
        "activity": ["한옥마을 골목 산책", "전통놀이 체험"],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Jeonju_Hanok_Village_in_Jeonju%2C_Korea.jpg/800px-Jeonju_Hanok_Village_in_Jeonju%2C_Korea.jpg"
    },
    "강릉": {
        "coords": [37.7519, 128.8761],
        "famous": ["경포대", "주문진", "오죽헌"],
        "food": ["초당순두부", "감자옹심이"],
        "activity": ["동해 바다 드라이브", "커피 거리 산책"],
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Gyeongpo_Beach%2C_Gangneung.jpg/800px-Gyeongpo_Beach%2C_Gangneung.jpg"
    }
}

st.title("🗺️ 대한민국 지역 추천기")
st.write("지도에서 원하는 지역의 원을 클릭하면 해당 지역의 추천 정보를 보여줍니다.")

# 지도 생성
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 지역별 클릭 가능한 큰 원 표시
for region_name, data in regions.items():
    folium.CircleMarker(
        location=data["coords"],
        radius=30,
        color='blue',
        fill=True,
        fill_opacity=0.4,
        popup=region_name
    ).add_to(m)

# 지도 표시
map_data = st_folium(m, width=700, height=500)

# 클릭된 지역 확인
selected_region = None
if map_data and map_data.get("last_object_clicked_popup"):
    selected_region = map_data["last_object_clicked_popup"]

if selected_region and selected_region in regions:
    info = regions[selected_region]
    st.subheader(f"📍 {selected_region} 추천 여행 정보")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(info["image"], use_container_width=True)
    with col2:
        st.markdown("**유명한 곳:**")
        for place in info["famous"]:
            st.write(f"- {place}")
        st.markdown("**대표 음식:**")
        for food in info["food"]:
            st.write(f"- {food}")
        st.markdown("**추천 활동:**")
        for act in info["activity"]:
            st.write(f"- {act}")
