import streamlit as st

# MBTI 별 직업 추천 사전
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "연구원"],
    "INTP": ["이론 물리학자", "소프트웨어 개발자", "UX 디자이너"],
    "ENTJ": ["경영 컨설턴트", "CEO", "프로젝트 매니저"],
    "ENTP": ["벤처 창업가", "광고 기획자", "기술 분석가"],
    "INFJ": ["상담사", "작가", "사회운동가"],
    "INFP": ["예술가", "심리상담가", "작사가"],
    "ENFJ": ["HR 매니저", "교사", "커뮤니케이션 전문가"],
    "ENFP": ["마케팅 전문가", "방송인", "콘텐츠 크리에이터"],
    "ISTJ": ["회계사", "관리자", "품질관리 전문가"],
    "ISFJ": ["간호사", "사회복지사", "사서"],
    "ESTJ": ["군 장교", "행정관", "공장 관리자"],
    "ESFJ": ["초등 교사", "이벤트 플래너", "고객 서비스 관리자"],
    "ISTP": ["기계 엔지니어", "파일럿", "보안 전문가"],
    "ISFP": ["패션 디자이너", "사진작가", "플로리스트"],
    "ESTP": ["세일즈 매니저", "스포츠 트레이너", "기업가"],
    "ESFP": ["배우", "엔터테이너", "여행 가이드"]
}

# Streamlit 웹앱 시작
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠")

st.title("🧠 MBTI 기반 직업 추천 웹앱")
st.write("당신의 MBTI를 선택하면, 어울리는 직업 3가지를 추천해드립니다.")

# 사용자에게 MBTI 선택 받기
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", sorted(mbti_list))

# 추천 직업 보여주기
if selected_mbti:
    st.subheader(f"✨ {selected_mbti}에게 어울리는 직업 추천:")
    for i, job in enumerate(mbti_jobs[selected_mbti], 1):
        st.write(f"{i}. {job}")
