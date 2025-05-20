import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠", layout="centered")

# 🎉 제목
st.title("💼 MBTI 직업 추천기 🧠")
st.markdown("당신의 **MBTI**를 입력하면 어울리는 직업을 알려드릴게요! 🚀\n\n> 이 앱은 재미로 만들어졌습니다. 😄")

# 🌟 사용자 입력
mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP, ENTJ 등)", max_chars=4).upper()

# 🧠 MBTI - 직업 매칭 데이터
mbti_jobs = {
    "INTJ": ["전략 컨설턴트 🧠", "데이터 과학자 📊", "소프트웨어 엔지니어 👨‍💻"],
    "INTP": ["연구원 🔬", "이론 물리학자 🌌", "프로그래머 💻"],
    "ENTJ": ["CEO 🏢", "프로젝트 매니저 📈", "변호사 ⚖️"],
    "ENTP": ["기획자 🧩", "창업가 🚀", "광고 기획자 📺"],
    "INFJ": ["심리상담사 🧘", "작가 ✍️", "NGO 활동가 🌍"],
    "INFP": ["예술가 🎨", "시인 📜", "사회복지사 ❤️"],
    "ENFJ": ["교사 📚", "인사 담당자 🤝", "마케터 📣"],
    "ENFP": ["스타트업 창업자 🚀", "디자이너 🖌️", "배우 🎭"],
    "ISTJ": ["회계사 📊", "경찰관 👮", "군인 🪖"],
    "ISFJ": ["간호사 👩‍⚕️", "도서관 사서 📚", "초등교사 🍎"],
    "ESTJ": ["공무원 🏛️", "프로젝트 매니저 📋", "엔지니어 🧱"],
    "ESFJ": ["간호사 👩‍⚕️", "행사 기획자 🎉", "CS 매니저 💁"],
    "ISTP": ["기계공 🛠️", "파일럿 ✈️", "탐험가 🧭"],
    "ISFP": ["사진작가 📸", "플로리스트 🌷", "요리사 🍳"],
    "ESTP": ["영업 전문가 💼", "구조대원 🚒", "스턴트 배우 🎬"],
    "ESFP": ["MC 🎤", "배우 🎭", "모델 👠"]
}

# 🎯 결과 출력
if mbti:
    if mbti in mbti_jobs:
        st.success(f"✨ {mbti} 유형에게 어울리는 직업은...")
        for job in mbti_jobs[mbti]:
            st.markdown(f"- {job}")
        st.balloons()  # 🎈 풍선 효과
    else:
        st.error("😢 알 수 없는 MBTI 유형이에요. 다시 확인해 주세요 (예: INFP, ENTJ 등)")
