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

# 🌈 직업 추천 데이터
mbti_jobs = {
    "ISTJ": ["📊 회계사", "⚖️ 판사", "🏫 교사"],
    "ISFJ": ["👩‍⚕️ 간호사", "🧑‍🏫 초등교사", "👩‍🍳 제과제빵사"],
    "INFJ": ["📚 심리상담사", "🎨 일러스트레이터", "✍️ 작가"],
    "INTJ": ["💻 데이터 과학자", "🧠 인공지능 연구원", "🚀 우주과학자"],
    "ISTP": ["🔧 기계 엔지니어", "🏎️ 자동차 정비사", "👮‍♀️ 경찰"],
    "ISFP": ["🎶 뮤지션", "🎨 패션디자이너", "📸 포토그래퍼"],
    "INFP": ["📝 시나리오 작가", "🧘 요가강사", "🎭 배우"],
    "INTP": ["🔬 연구원", "👩‍💻 프로그래머", "🎮 게임 개발자"],
    "ESTP": ["🕵️ 형사", "🎤 방송기자", "🛫 승무원"],
    "ESFP": ["🎤 연예인", "🎬 영화감독", "💄 뷰티유튜버"],
    "ENFP": ["💡 창업가", "🎤 방송작가", "🎉 이벤트플래너"],
    "ENTP": ["🧪 발명가", "📱 앱개발자", "🗣️ 변론가"],
    "ESTJ": ["🏢 기업 CEO", "🧑‍⚖️ 법률가", "🏦 은행원"],
    "ESFJ": ["🏥 병원 코디네이터", "👩‍🏫 교사", "🎀 플로리스트"],
    "ENFJ": ["🌍 국제기구활동가", "👩‍🏫 진로상담가", "🎤 방송MC"],
    "ENTJ": ["📈 경영 컨설턴트", "🚀 스타트업 CEO", "🧠 전략기획가"]
}

# 🌟 추천 직업 표시
if selected_mbti:
    st.markdown(f'<div class="job-box"><h3>✨ {selected_mbti} 유형에게 추천하는 직업은...</h3>', unsafe_allow_html=True)
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")
    st.markdown('</div>', unsafe_allow_html=True)
