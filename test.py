import streamlit as st

st.set_page_config(page_title="대한민국 지역 추천기", layout="wide")

# 지역별 데이터 준비
regions = {
    "서울": {
        "famous": "경복궁, 남산타워, 한강",
        "food": "불고기, 비빔밥",
        "activity": "한강 자전거 타기, 북촌 한옥마을 산책",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Gyeongbokgung_Palace_%28Keongbokgung%29_2014-09-16.jpg/800px-Gyeongbokgung_Palace_%28Keongbokgung%29_2014-09-16.jpg"
    },
    "부산": {
        "famous": "해운대, 광안리, 자갈치 시장",
        "food": "밀면, 돼지국밥",
        "activity": "해운대 바다 산책, 광안대교 야경 감상",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Haeundae_Beach_Busan_South_Korea.jpg/800px-Haeundae_Beach_Busan_South_Korea.jpg"
    },
    "제주": {
        "famous": "한라산, 성산일출봉, 협재 해수욕장",
        "food": "흑돼지, 갈치조림",
        "activity": "올레길 걷기, 동굴 탐험",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Jeju_Island_Seongsan_Ilchulbong.jpg/800px-Jeju_Island_Seongsan_Ilchulbong.jpg"
    },
    "전주": {
        "famous": "전주 한옥마을, 경기전",
        "food": "전주비빔밥, 콩나물국밥",
        "activity": "한옥마을 골목 산책, 전통놀이 체험",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Jeonju_Hanok_Village_in_Jeonju%2C_Korea.jpg/800px-Jeonju_Hanok_Village_in_Jeonju%2C_Korea.jpg"
    },
    "강릉": {
        "famous": "경포대, 주문진, 오죽헌",
        "food": "초당순두부, 감자옹심이",
        "activity": "동해 바다 드라이브, 커피 거리 산책",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Gyeongpo_Beach%2C_Gangneung.jpg/800px-Gyeongpo_Beach%2C_Gangneung.jpg"
    }
}

st.title("🗺️ 대한민국 지역 추천기")

# 지역 선택
region = st.selectbox("지역을 선택하세요:", list(regions.keys()))

# 선택한 지역 정보 표시
info = regions[region]

st.subheader(f"📍 {region} 추천 여행 정보")

col1, col2 = st.columns([2, 1])

with col1:
    st.image(info["image"], use_column_width=True)

with col2:
    st.markdown(f"**유명한 곳**: {info['famous']}")
    st.markdown(f"**대표 음식**: {info['food']}")
    st.markdown(f"**추천 활동**: {info['activity']}")

