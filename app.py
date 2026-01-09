"""
지적장애 학생을 위한 AI 기반 학습 웹 애플리케이션
메인 홈 화면
"""
import streamlit as st
from utils.ui_components import apply_custom_css
from utils.gemini_client import validate_api_key
from utils.game_logic import init_session_state

# 페이지 설정
st.set_page_config(
    page_title="즐거운 학습",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 적용
apply_custom_css()

# 세션 상태 초기화
init_session_state()

# 사이드바 - API 키 입력
with st.sidebar:
    st.title("⚙️ 설정")
    
    api_key = st.text_input(
        "🔑 Gemini API 키",
        type="password",
        placeholder="여기에 붙여넣기",
        value=st.session_state.get("api_key", ""),
        help="Google AI Studio에서 무료로 발급받을 수 있어요!",
        key="api_key_input"
    )
    
    # API 키가 변경되었는지 확인
    previous_key = st.session_state.get("api_key", "")
    key_changed = api_key != previous_key
    
    if api_key:
        # 키가 변경되었거나 아직 검증되지 않은 경우에만 검증
        if key_changed or not st.session_state.get("api_key_validated", False):
            with st.spinner("확인 중..."):
                is_valid, error_msg = validate_api_key(api_key)
                if is_valid:
                    st.session_state.api_key = api_key.strip()
                    st.session_state.api_key_validated = True
                    st.success("✅ 연결 완료!")
                else:
                    st.session_state.api_key_validated = False
                    st.error(f"❌ {error_msg}")
        else:
            # 이미 검증된 키인 경우
            if st.session_state.get("api_key_validated", False):
                st.success("✅ 연결 완료!")
    else:
        st.info("👆 API 키를 입력하면 시작할 수 있어요!")
        st.session_state.api_key_validated = False
    
    with st.expander("📖 API 키 받는 방법"):
        st.markdown("""
        ### API 키 받는 방법
        
        1️⃣ **Google AI Studio 접속**
           - [aistudio.google.com](https://aistudio.google.com) 클릭
        
        2️⃣ **로그인**
           - Google 계정으로 로그인해요
        
        3️⃣ **API 키 만들기**
           - "Get API Key" 버튼 클릭
           - "Create API Key" 클릭
        
        4️⃣ **키 복사하기**
           - 생성된 키를 복사해서 위에 붙여넣기!
        
        💡 **무료**로 사용할 수 있어요!
        """)
    
    # 디버깅 정보 (개발용)
    if st.session_state.get("api_key") and not st.session_state.get("api_key_validated", False):
        with st.expander("🔧 문제 해결 도움말", expanded=False):
            st.markdown("""
            ### API 키가 인식되지 않을 때:
            
            1. **키 앞뒤 공백 확인**: 복사할 때 공백이 포함되었는지 확인해주세요
            2. **키 형식 확인**: API 키는 'AIza'로 시작해야 해요
            3. **새로고침**: 페이지를 새로고침하고 다시 시도해보세요
            4. **새 키 발급**: 문제가 계속되면 Google AI Studio에서 새 키를 발급받아보세요
            
            💡 **팁**: API 키는 한 번에 하나만 활성화할 수 있어요
            """)
    
    st.divider()
    
    # 별 개수 표시
    stars = st.session_state.get("stars", 0)
    st.metric("내 별", f"⭐ {stars}개")

# 메인 화면
st.markdown("<h1 style='text-align: center;'>📚 즐거운 학습</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 24px;'>안녕! 오늘도 재미있게 공부해요! 😊</p>", 
            unsafe_allow_html=True)

# 마스코트 환영 메시지
st.markdown("""
<div style="text-align: center; padding: 20px; background: #FFF3CD; border-radius: 20px; margin: 20px;">
    <h2>👋 안녕하세요!</h2>
    <p style="font-size: 22px;">오늘 무엇을 배울까요?<br>재미있는 학습이 기다리고 있어요! 🌟</p>
</div>
""", unsafe_allow_html=True)

# 메뉴 버튼들
st.markdown("<h2 style='text-align: center; margin-top: 40px;'>학습 메뉴</h2>", 
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("📖\n\n**읽기 학습**\n\n단어를 배워요!", 
                 use_container_width=True, key="btn_read"):
        st.switch_page("pages/1_📖_읽기학습.py")
    
    if st.button("🔢\n\n**숫자 학습**\n\n숫자를 세어요!", 
                 use_container_width=True, key="btn_math"):
        st.switch_page("pages/3_🔢_숫자학습.py")

with col2:
    if st.button("✏️\n\n**쓰기 학습**\n\n글자를 써요!", 
                 use_container_width=True, key="btn_write"):
        st.switch_page("pages/2_✏️_쓰기학습.py")
    
    if st.button("💬\n\n**AI 선생님**\n\n하늬 선생님과 대화해요!", 
                 use_container_width=True, key="btn_chat"):
        st.switch_page("pages/4_💬_AI선생님.py")

# 하단 상장 버튼
st.markdown("---")
if st.button("🏆 내 상장 보기", use_container_width=True, key="btn_award"):
    st.switch_page("pages/5_🏆_내상장.py")
