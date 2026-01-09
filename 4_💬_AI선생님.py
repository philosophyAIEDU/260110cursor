"""
AI 선생님 대화 페이지
"""
import streamlit as st
from utils.ui_components import apply_custom_css, require_api_key
from utils.gemini_client import check_api_key, get_ai_response

# 페이지 설정
st.set_page_config(
    page_title="AI 선생님",
    page_icon="💬",
    layout="wide"
)

apply_custom_css()

# API 키 확인
if not check_api_key():
    require_api_key()

# 제목
st.markdown("<h1 style='text-align: center;'>💬 AI 선생님</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px;'>하늬 선생님과 대화해봐요! 😊</p>", 
            unsafe_allow_html=True)

# 선생님 소개
st.markdown("""
<div style="text-align: center; padding: 30px; background: #E8F5E9; border-radius: 20px; margin: 20px;">
    <h2>🧑‍🏫 하늬 선생님</h2>
    <p style="font-size: 22px;">안녕하세요! 저는 하늬 선생님이에요! 😊<br>
    무엇이든 물어보세요! 친절하게 알려드릴게요! 🌟</p>
</div>
""", unsafe_allow_html=True)

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕! 😊 나는 하늬 선생님이야! 오늘 무엇을 배우고 싶어? 무엇이든 물어봐도 돼! 👍"
        }
    ]

# 채팅 메시지 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div style="font-size: 20px;">{message["content"]}</div>', 
                   unsafe_allow_html=True)

# 사용자 입력
user_input = st.chat_input("하늬 선생님에게 말해봐요...")

if user_input:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # AI 응답 생성
    with st.spinner("하늬 선생님이 생각하고 있어요..."):
        ai_response = get_ai_response(user_input)
    
    # AI 메시지 추가
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    
    # 화면 새로고침
    st.rerun()

# 대화 초기화 버튼
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("🗑️ 대화 지우기", use_container_width=True, key="btn_clear"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "안녕! 😊 나는 하늬 선생님이야! 오늘 무엇을 배우고 싶어? 무엇이든 물어봐도 돼! 👍"
            }
        ]
        st.rerun()

with col2:
    if st.button("🏠 홈으로 돌아가기", use_container_width=True, key="btn_home"):
        st.switch_page("app.py")
