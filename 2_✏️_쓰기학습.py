"""
쓰기 학습 페이지
"""
import streamlit as st
from utils.ui_components import apply_custom_css, require_api_key, celebration, encouragement
from utils.gemini_client import check_api_key, get_ai_response
from utils.game_logic import add_star
from utils.constants import READING_WORDS
import random

# 페이지 설정
st.set_page_config(
    page_title="쓰기 학습",
    page_icon="✏️",
    layout="wide"
)

apply_custom_css()

# API 키 확인
if not check_api_key():
    require_api_key()

# 제목
st.markdown("<h1 style='text-align: center;'>✏️ 쓰기 학습</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px;'>글자를 따라 써봐요! 😊</p>", 
            unsafe_allow_html=True)

# 현재 단어 선택
if "writing_word" not in st.session_state:
    st.session_state.writing_word = random.choice(READING_WORDS)
    st.session_state.writing_input_key = 0

word_data = st.session_state.writing_word
word = word_data["word"]
emoji = word_data["emoji"]

# 단어 표시
st.markdown(f"""
<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #FFF9E6, #FFE66D); 
            border-radius: 30px; margin: 30px; border: 5px solid #FFB6C1;">
    <h1 style="font-size: 120px; margin: 20px;">{emoji}</h1>
    <h1 style="font-size: 80px; margin: 20px; color: #2D3436;">{word}</h1>
    <p style="font-size: 28px; color: #666;">이 단어를 따라 써봐요!</p>
</div>
""", unsafe_allow_html=True)

# 쓰기 연습
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>아래 칸에 글자를 써봐요! ✏️</h3>", 
            unsafe_allow_html=True)

user_input = st.text_input(
    "글자 입력",
    placeholder=f"'{word}'를 여기에 써봐요",
    key=f"writing_input_{st.session_state.writing_input_key}",
    label_visibility="collapsed"
)

# 입력 필드 스타일링
st.markdown("""
<style>
.stTextInput > div > div > input {
    font-size: 32px !important;
    text-align: center !important;
    padding: 20px !important;
    height: 80px !important;
}
</style>
""", unsafe_allow_html=True)

# 정답 확인
if user_input:
    if user_input.strip() == word:
        celebration()
        add_star(1)
        st.session_state.writing_word = random.choice(READING_WORDS)
        st.session_state.writing_input_key += 1
        st.rerun()
    else:
        encouragement()
        st.markdown(f"""
        <div style="text-align: center; padding: 20px; background: #FFF3CD; border-radius: 15px; margin: 20px;">
            <p style="font-size: 22px;">다시 한 번 해봐요! 정답은 <strong>{word}</strong>예요! 💪</p>
        </div>
        """, unsafe_allow_html=True)

# 힌트 버튼
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("💡 힌트 보기", use_container_width=True, key="btn_hint"):
        hint = get_ai_response(
            f"'{word}'라는 단어를 쓰는 방법을 한 글자씩 쉽게 설명해주세요.",
            system_prompt="당신은 친절한 선생님이에요. 한 글자씩 쉽게 설명해주세요."
        )
        st.info(f"💡 힌트: {hint}")

with col2:
    if st.button("🔄 다른 단어", use_container_width=True, key="btn_new_word"):
        st.session_state.writing_word = random.choice(READING_WORDS)
        st.session_state.writing_input_key += 1
        st.rerun()

with col3:
    if st.button("✅ 정답 확인", use_container_width=True, key="btn_check"):
        if user_input:
            if user_input.strip() == word:
                celebration()
                add_star(1)
                st.session_state.writing_word = random.choice(READING_WORDS)
                st.session_state.writing_input_key += 1
                st.rerun()
            else:
                encouragement()

# 홈으로 돌아가기
st.markdown("---")
if st.button("🏠 홈으로 돌아가기", use_container_width=True, key="btn_home"):
    st.switch_page("app.py")
