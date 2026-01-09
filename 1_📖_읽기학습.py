"""
읽기 학습 페이지
"""
import streamlit as st
from utils.ui_components import apply_custom_css, require_api_key, celebration, encouragement
from utils.gemini_client import get_word_explanation, check_api_key
from utils.game_logic import get_current_reading_word, next_reading_word, add_star

# 페이지 설정
st.set_page_config(
    page_title="읽기 학습",
    page_icon="📖",
    layout="wide"
)

apply_custom_css()

# API 키 확인
if not check_api_key():
    require_api_key()

# 제목
st.markdown("<h1 style='text-align: center;'>📖 읽기 학습</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px;'>단어를 배워봐요! 😊</p>", 
            unsafe_allow_html=True)

# 현재 단어 가져오기
word_data = get_current_reading_word()
word = word_data["word"]
emoji = word_data["emoji"]
description = word_data["description"]

# 단어 카드 표시
st.markdown(f"""
<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #FFF9E6, #FFE66D); 
            border-radius: 30px; margin: 30px; border: 5px solid #FFB6C1;">
    <h1 style="font-size: 120px; margin: 20px;">{emoji}</h1>
    <h1 style="font-size: 80px; margin: 20px; color: #2D3436;">{word}</h1>
    <p style="font-size: 28px; color: #666;">{description}</p>
</div>
""", unsafe_allow_html=True)

# AI 설명 가져오기
if "word_explanation" not in st.session_state or st.session_state.get("current_word") != word:
    with st.spinner("하늬 선생님이 설명해주고 있어요..."):
        explanation = get_word_explanation(word, emoji)
        st.session_state.word_explanation = explanation
        st.session_state.current_word = word

if "word_explanation" in st.session_state:
    st.markdown(f"""
    <div style="background: #E8F5E9; padding: 25px; border-radius: 20px; margin: 20px;">
        <h3 style="color: #2D3436;">💡 하늬 선생님 설명:</h3>
        <p style="font-size: 22px;">{st.session_state.word_explanation}</p>
    </div>
    """, unsafe_allow_html=True)

# 정답 확인
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>이 단어를 읽을 수 있나요? 😊</h3>", 
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ 읽을 수 있어요!", use_container_width=True, key="btn_correct"):
        celebration()
        add_star(1)
        st.session_state.word_explanation = None
        next_reading_word()
        st.rerun()

with col2:
    if st.button("🔄 다시 보기", use_container_width=True, key="btn_retry"):
        st.rerun()

# 다음 단어 버튼
st.markdown("---")
if st.button("➡️ 다음 단어", use_container_width=True, key="btn_next"):
    st.session_state.word_explanation = None
    next_reading_word()
    st.rerun()

# 홈으로 돌아가기
st.markdown("---")
if st.button("🏠 홈으로 돌아가기", use_container_width=True, key="btn_home"):
    st.switch_page("app.py")
