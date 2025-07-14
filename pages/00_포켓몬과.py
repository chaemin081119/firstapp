import streamlit as st

# MBTI별 포켓몬 추천 데이터
mbti_pokemon = {
    "INTJ": {
        "pokemon": "뮤츠 (Mewtwo)",
        "reason": "지능적이고 전략적인 성격의 INTJ는 강력하고 냉철한 뮤츠와 닮았습니다. 자신의 목적에 집중하며 독립적으로 행동하는 점이 유사합니다."
    },
    "INTP": {
        "pokemon": "프시겔 (Alakazam)",
        "reason": "탐구심이 강한 INTP는 천재적인 두뇌를 가진 프시겔과 어울립니다. 분석력과 논리적 사고가 닮았어요."
    },
    "ENTJ": {
        "pokemon": "리자몽 (Charizard)",
        "reason": "강력한 리더십을 지닌 ENTJ는 카리스마 넘치는 리자몽과 잘 어울립니다. 목표 지향적이고 추진력이 강하죠."
    },
    "ENTP": {
        "pokemon": "팬텀 (Gengar)",
        "reason": "장난기 많고 창의적인 ENTP는 재치 있고 유쾌한 팬텀과 잘 맞습니다. 즉흥적이지만 매력적인 성격이에요."
    },
    "INFJ": {
        "pokemon": "루기아 (Lugia)",
        "reason": "이상주의적이고 조용한 카리스마를 지닌 INFJ는 평화를 중시하는 루기아와 닮았습니다. 고요한 힘을 가진 존재입니다."
    },
    "INFP": {
        "pokemon": "이브이 (Eevee)",
        "reason": "순수하고 상상력이 풍부한 INFP는 다양한 가능성을 가진 이브이와 어울립니다. 변화와 성장을 중시하죠."
    },
    "ENFJ": {
        "pokemon": "가디안 (Gardevoir)",
        "reason": "타인을 보호하고 이끄는 ENFJ는 헌신적이고 따뜻한 가디안과 잘 맞습니다. 공감 능력이 뛰어나요."
    },
    "ENFP": {
        "pokemon": "피카츄 (Pikachu)",
        "reason": "활발하고 에너지 넘치는 ENFP는 모두의 친구인 피카츄와 잘 어울립니다. 밝고 긍정적인 에너지를 가졌죠."
    },
    "ISTJ": {
        "pokemon": "케이시 (Porygon)",
        "reason": "체계적이고 신중한 ISTJ는 규칙에 충실한 인공 포켓몬 케이시와 유사합니다. 논리적인 성향이 강해요."
    },
    "ISFJ": {
        "pokemon": "해피너스 (Blissey)",
        "reason": "배려심 깊고 헌신적인 ISFJ는 상처를 치유하는 해피너스와 잘 어울립니다. 주변을 따뜻하게 만드는 존재예요."
    },
    "ESTJ": {
        "pokemon": "코리갑 (Rhyperior)",
        "reason": "강한 책임감과 현실 감각을 가진 ESTJ는 듬직한 코리갑과 어울립니다. 안정감과 추진력을 동시에 갖췄어요."
    },
    "ESFJ": {
        "pokemon": "라프라스 (Lapras)",
        "reason": "친절하고 협동적인 ESFJ는 모두를 태우고 이동해주는 라프라스와 잘 어울립니다. 신뢰와 포용력의 상징입니다."
    },
    "ISTP": {
        "pokemon": "갸라도스 (Gyarados)",
        "reason": "조용하지만 상황에 따라 폭발적인 힘을 발휘하는 ISTP는 갸라도스와 유사합니다. 예측불가능한 매력이 있어요."
    },
    "ISFP": {
        "pokemon": "브이젤 (Buizel)",
        "reason": "감성적이고 자유로운 ISFP는 자연과 조화를 이루는 브이젤과 잘 맞습니다. 유연하고 부드러운 성격이에요."
    },
    "ESTP": {
        "pokemon": "전룡 (Ampharos)",
        "reason": "즉흥적이고 활동적인 ESTP는 밝고 강한 존재감의 전룡과 잘 어울립니다. 주변을 밝히는 에너지가 있어요."
    },
    "ESFP": {
        "pokemon": "불꽃숭이 (Chimchar)",
        "reason": "생기 넘치고 모두를 즐겁게 하는 ESFP는 활발한 불꽃숭이와 유사합니다. 주변을 웃게 만드는 매력을 가졌죠."
    }
}

# Streamlit 웹앱 시작
st.set_page_config(page_title="MBTI x 포켓몬 추천기", page_icon="🎮")

st.title("🎮 MBTI별 어울리는 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면, 성격에 가장 어울리는 포켓몬과 그 이유를 알려드릴게요!")

# 사용자에게 MBTI 선택 받기
mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", sorted(mbti_list))

# 추천 포켓몬과 설명 출력
if selected_mbti:
    pokemon = mbti_pokemon[selected_mbti]["pokemon"]
    reason = mbti_pokemon[selected_mbti]["reason"]
    st.subheader(f"✨ {selected_mbti}와 어울리는 포켓몬은?")
    st.markdown(f"### 🐾 {pokemon}")
    st.write(reason)
