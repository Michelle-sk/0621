import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기", page_icon="🎀", layout="centered")

# 💖 커스텀 스타일
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        text-align: center;
        color: #ff66b2;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #ff99cc;
        text-align: center;
        margin-bottom: 30px;
    }
    .job-box {
        background-color: #fff0f5;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 2px 2px 15px #fbb6ce;
    }
    </style>
""", unsafe_allow_html=True)

# 🎀 타이틀
st.markdown('<div class="title">💖 MBTI로 알아보는 나의 미래 직업 💼</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">너의 MBTI는? ✨ 네 성격에 꼭 맞는 직업을 추천해줄게! 🎯</div>', unsafe_allow_html=True)

# 🎯 MBTI 선택
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("👇 여기에 너의 MBTI를 골라줘!", mbti_types, index=0)

# 🌈 직업 추천 + 설명 데이터
mbti_jobs = {
    "ISTJ": [("📊 회계사", "숫자에 강하고 꼼꼼한 성격을 살려 기업의 재무를 관리하는 직업이에요."),
