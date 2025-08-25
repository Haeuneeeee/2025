import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="대한민국 여행지도", layout="wide")
st.title("🗺️ 대한민국 여행 지도")
st.write("도시를 클릭하면 유명 명소, 먹거리, 놀거리가 리스트로 나옵니다.")

# 도시 좌표
cities = {
    "서울": [37.5665, 126.9780],
    "부산": [35.1796, 129.0756],
    "제주": [33.4996, 126.5312],
    "전주": [35.8242, 127.1479],
    "강릉": [37.7519, 128.8761],
    "대전": [36.3504, 127.3845],
    "대구": [35.8714, 128.6014],
    "광주": [35.1595, 126.8526],
}

# 여행 정보
travel_info = {
    "서울": {"명소":["경복궁","남산타워"],"먹거리":["불고기","비빔밥"],"놀거리":["한강 자전거 타기","명동 쇼핑"]},
    "부산": {"명소":["해운대","광안리 해수욕장"],"먹거리":["밀면","돼지국밥"],"놀거리":["해변 산책","국제시장 쇼핑"]},
    "제주": {"명소":["한라산","성산일출봉"],"먹거리":["흑돼지","갈치조림"],"놀거리":["오름 등반","서핑"]},
    "전주": {"명소":["전주한옥마을","경기전"],"먹거리":["전주비빔밥","콩나물국밥"],"놀거리":["한옥마을 한복체험"]},
    "강릉": {"명소":["경포대","안목해변 커피거리"],"먹거리":["초당두부","강릉커피"],"놀거리":["서핑","바다 열차 타기"]},
    "대전": {"명소":["엑스포과학공원","한밭수목원"],"먹거리":["성심당 빵","칼국수"],"놀거리":["과학관 체험","대전 아쿠아리움"]},
    "대구": {"명소":["팔공산","동성로"],"먹거리":["막창","동인동 찜갈비"],"놀거리":["동성로 쇼핑","이월드"]},
    "광주": {"명소":["무등산","국립아시아문화전당"],"먹거리":["광주 떡갈비","상추튀김"],"놀거리":["문화전당 전시관람","충장로 쇼핑"]},
}

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)
for city, coord in cities.items():
    folium.Marker(
        location=coord,
        popup=f"{city} 클릭!",
        tooltip=city,
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)

map_data = st_folium(m, width=800, height=500)

# 클릭 이벤트 처리
if map_data["last_object_clicked_popup"]:
    selected_city = map_data["last_object_clicked_popup"].replace(" 클릭!", "")
    
    st.subheader(f"📍 {selected_city} 유명한 명소")
    st.write("\n".join(travel_info[selected_city]["명소"]))

    st.subheader("🍜 먹거리")
    st.write("\n".join(travel_info[selected_city]["먹거리"]))

    st.subheader("🎉 놀거리")
    st.write("\n".join(travel_info[selected_city]["놀거리"]))
