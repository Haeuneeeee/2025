import streamlit as st
import time

# 지역 데이터
regions = {
    "서울": ["경복궁", "남산타워", "홍대 거리", "광장시장"],
    "부산": ["해운대", "광안리", "자갈치시장", "태종대"],
    "제주": ["한라산", "성산일출봉", "협재 해수욕장", "우도"]
}

st.title("🗺️ 대한민국 여행 지도")

# 깃발 버튼들
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚩 서울"):
        st.balloons()
        st.subheader("🎆 서울에서 유명한 것")
        for place in regions["서울"]:
            time.sleep(0.5)  # 하나씩 나오게 하기
            st.write(f"- {place}")

with col2:
    if st.button("🚩 부산"):
        st.balloons()
        st.subheader("🎆 부산에서 유명한 것")
        for place in regions["부산"]:
            time.sleep(0.5)
            st.write(f"- {place}")

with col3:
    if st.button("🚩 제주"):
        st.balloons()
        st.subheader("🎆 제주에서 유명한 것")
        for place in regions["제주"]:
            time.sleep(0.5)
            st.write(f"- {place}")


