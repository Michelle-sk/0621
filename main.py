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
             ("⚖️ 판사", "공정함과 책임감을 바탕으로 사회 정의를 실현하는 직업이에요."),
             ("🏫 교사", "체계적이고 책임감 있게 지식을 전달하는 교육 전문가예요.")],

    "ENFP": [("💡 창업가", "창의적인 아이디어로 새로운 사업을 시작하는 도전적인 직업이에요."),
             ("🎤 방송작가", "아이디어와 글쓰기를 통해 방송 콘텐츠를 만드는 창의적인 직업이에요."),
             ("🎉 이벤트플래너", "행사를 기획하고 진행하는 에너지 넘치는 직업이에요.")],

    "ISFP": [("🎶 뮤지션", "감성을 음악으로 표현하는 예술적인 직업이에요."),
             ("🎨 패션디자이너", "감각적인 스타일을 옷으로 표현하는 창의적인 직업이에요."),
             ("📸 포토그래퍼", "순간을 포착해 감정을 전하는 사진 예술가예요.")],

    # (추가 MBTI 유형은 동일한 방식으로 확장 가능)
}

# 🌟 직업 추천 결과 출력
if selected_mbti in mbti_jobs:
    st.markdown(f'<div class="job-box"><h3>✨ {selected_mbti} 유형에게 추천하는 직업은...</h3>', unsafe_allow_html=True)
    for job, description in mbti_jobs[selected_mbti]:
        with st.expander(job):
            st.write(description)
    st.markdown('</div>', unsafe_allow_html=True)
