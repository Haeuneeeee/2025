import streamlit as st

# 미리 정의한 궁합 데이터 (예시)
# 각 MBTI 조합에 대한 궁합 점수와 설명
compatibility_data = {
    ("INTJ", "ENFP"): ("💖 잘 맞음", "서로 부족한 점을 채워주는 완벽한 상극-상보형 조합"),
    ("INFP", "ENTJ"): ("💖 잘 맞음", "비전과 실행력이 만나 시너지를 내는 관계"),
    ("ISTP", "ESFJ"): ("😊 보통", "성향이 다르지만 노력하면 좋은 관계 가능"),
    ("ESTJ", "ISFP"): ("😊 보통", "실용과 감성이 적절히 어우러짐"),
    ("INFJ", "ENTP"): ("💖 잘 맞음", "창의성과 직관이 만나 끊임없이 영감을 주는 조합"),
}

# 모든 MBTI 유형
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

st.title("💌 MBTI 궁합 테스트")
st.write("두 사람의 MBTI를 선택하고 궁합을 확인해보세요!")

col1, col2 = st.columns(2)

with col1:
    mbti1 = st.selectbox("첫 번째 사람의 MBTI", mbti_list)
with col2:
    mbti2 = st.selectbox("두 번째 사람의 MBTI", mbti_list)

if st.button("궁합 확인하기"):
    pair = (mbti1, mbti2)
    reverse_pair = (mbti2, mbti1)

    if pair in compatibility_data:
        result, desc = compatibility_data[pair]
    elif reverse_pair in compatibility_data:
        result, desc = compatibility_data[reverse_pair]
    else:
        result, desc = ("🤝 데이터 없음", "아직 등록되지 않은 조합이에요. 직접 궁합을 판단해보세요!")

    st.subheader(f"{mbti1} ❤️ {mbti2}")
    st.markdown(f"**{result}**\n\n{desc}")
