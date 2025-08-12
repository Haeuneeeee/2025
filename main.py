import streamlit as st

# MBTI별 키워드 정의
mbti_traits = {
    "I": "내향적, 혼자만의 시간 선호",
    "E": "외향적, 사람들과의 교류 선호",
    "S": "현실적, 구체적 정보 중시",
    "N": "직관적, 가능성과 아이디어 중시",
    "T": "이성적, 논리와 분석 중시",
    "F": "감성적, 공감과 관계 중시",
    "J": "계획적, 체계와 규칙 선호",
    "P": "즉흥적, 융통성과 자유 선호"
}

# 모든 MBTI 유형
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

def compatibility_score(mbti1, mbti2):
    """두 MBTI 궁합 점수와 설명 생성"""
    score = 0
    reasons = []

    for i in range(4):
        if mbti1[i] != mbti2[i]:
            score += 1  # 다른 성향일 때 점수
            reasons.append(f"{mbti1[i]} vs {mbti2[i]} → 서로 다른 성향이 보완 작용")
        else:
            reasons.append(f"{mbti1[i]} vs {mbti2[i]} → 비슷한 성향이 공감 형성")

    # 궁합 판정
    if score >= 3:
        result = "💖 잘 맞음"
    elif score == 2:
        result = "😊 보통"
    else:
        result = "⚡ 안 맞음"

    # 설명 문장화
    detail = []
    for i in range(4):
        detail.append(
            f"{mbti1[i]}형({mbti_traits[mbti1[i]]})과 {mbti2[i]}형({mbti_traits[mbti2[i]]})의 조합"
        )
    explanation = " / ".join(detail)

    return result, explanation

st.title("💌 MBTI 궁합 테스트")
st.write("모든 MBTI 조합에 대한 궁합과 이유를 확인하세요!")

col1, col2 = st.columns(2)

with col1:
    mbti1 = st.selectbox("첫 번째 MBTI", mbti_list)
with col2:
    mbti2 = st.selectbox("두 번째 MBTI", mbti_list)

if st.button("궁합 확인하기"):
    result, explanation = compatibility_score(mbti1, mbti2)
    st.subheader(f"{mbti1} ❤️ {mbti2}")
    st.markdown(f"**{result}**\n\n{explanation}")

st.markdown("---")
st.subheader("📜 모든 MBTI 궁합표")

# 전체 궁합표 생성
for m1 in mbti_list:
    for m2 in mbti_list:
        result, explanation = compatibility_score(m1, m2)
        st.markdown(f"**{m1} ❤️ {m2}** → {result}  \n{explanation}")
