import streamlit as st

# MBTI 성향별 설명
mbti_traits_short = {
    "I": "혼자만의 시간을 좋아해요",
    "E": "사람들과 어울리는 걸 좋아해요",
    "S": "현실적이고 구체적인 걸 선호해요",
    "N": "아이디어와 가능성을 중시해요",
    "T": "논리와 분석을 중시해요",
    "F": "감성과 공감을 중시해요",
    "J": "계획적이고 규칙을 좋아해요",
    "P": "즉흥적이고 자유로운 걸 좋아해요"
}

# 모든 MBTI 유형
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

def compatibility_analysis(m1, m2):
    """궁합 결과와 귀여운 문장 설명 반환"""
    diff_count = sum([m1[i] != m2[i] for i in range(4)])

    # 궁합 결과
    if diff_count >= 3:
        result = "💖 잘 맞음"
        style = "서로 다른 매력을 가진 두 사람이 만나 완벽하게 균형을 이루는 사이예요!"
    elif diff_count == 2:
        result = "😊 보통"
        style = "비슷한 점도 있고 다른 점도 있어서, 노력하면 좋은 친구가 될 수 있어요!"
    else:
        result = "⚡ 안 맞음"
        style = "성향이 너무 비슷하거나 달라서 조금 부딪힐 수 있지만, 이해하면 좋아져요!"

    # 성향 설명
    traits = []
    for i in range(4):
        if m1[i] != m2[i]:
            traits.append(f"{m1[i]}형은 {mbti_traits_short[m1[i]]}, {m2[i]}형은 {mbti_traits_short[m2[i]]}. 서로의 차이를 재밌게 느낄 수 있어요.")
        else:
            traits.append(f"둘
