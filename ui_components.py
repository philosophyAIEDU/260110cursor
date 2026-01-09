"""
재사용 가능한 UI 컴포넌트
"""
import streamlit as st


def require_api_key():
    """API 키가 없으면 안내 메시지를 보여주고 중단합니다."""
    if "api_key" not in st.session_state or not st.session_state.api_key:
        st.markdown("""
        <div style="text-align: center; padding: 40px; 
                    background: #FFF3CD; border-radius: 20px; margin: 20px;">
            <h1>🔑</h1>
            <h2>API 키를 입력해주세요!</h2>
            <p style="font-size: 18px;">
                👈 왼쪽 메뉴에서 API 키를 넣어주세요
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.stop()


def big_card_button(label: str, emoji: str, description: str, key: str):
    """큰 카드 형태의 버튼"""
    clicked = st.button(
        f"{emoji}\n\n**{label}**\n\n{description}",
        key=key,
        use_container_width=True
    )
    return clicked


def show_stars(count: int):
    """별 개수를 표시합니다."""
    stars = "⭐" * count
    st.markdown(f"<h2 style='text-align: center;'>{stars}</h2>", 
                unsafe_allow_html=True)


def celebration():
    """축하 효과를 보여줍니다."""
    st.balloons()
    st.success("🎉 정말 잘했어요! 최고예요!")


def encouragement():
    """격려 메시지를 보여줍니다."""
    st.info("💪 괜찮아요! 다시 해볼까요? 할 수 있어요!")


def apply_custom_css():
    """접근성 높은 커스텀 CSS를 적용합니다."""
    st.markdown("""
    <style>
    /* 큰 버튼 */
    .stButton > button {
        font-size: 22px !important;
        padding: 25px !important;
        min-height: 100px !important;
        border-radius: 20px !important;
        border: 3px solid #FFB6C1 !important;
        background: linear-gradient(135deg, #FFF9E6, #FFE66D) !important;
        transition: transform 0.2s !important;
        color: #2D3436 !important;
    }
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    }
    
    /* 큰 텍스트 */
    .stMarkdown, .stText {
        font-size: 20px !important;
    }
    
    /* 입력 필드 */
    .stTextInput input {
        font-size: 18px !important;
        padding: 15px !important;
        border-radius: 10px !important;
    }
    
    /* 채팅 메시지 */
    .stChatMessage {
        font-size: 20px !important;
        padding: 15px !important;
    }
    
    /* 메트릭 */
    .stMetric {
        background: #FFF9E6;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #FFE66D;
    }
    
    /* 성공 메시지 */
    .stSuccess {
        font-size: 20px !important;
        padding: 20px !important;
        border-radius: 15px !important;
    }
    
    /* 정보 메시지 */
    .stInfo {
        font-size: 20px !important;
        padding: 20px !important;
        border-radius: 15px !important;
    }
    
    /* 에러 메시지 */
    .stError {
        font-size: 20px !important;
        padding: 20px !important;
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)


def show_api_required_message():
    """API 키가 없을 때 보여줄 안내 화면"""
    st.markdown("""
    <div style="text-align: center; padding: 50px;">
        <h1>🔑</h1>
        <h2>API 키가 필요해요!</h2>
        <p style="font-size: 20px;">
            왼쪽 설정에서 API 키를 입력해주세요.<br>
            선생님이나 부모님께 도움을 요청해도 좋아요! 😊
        </p>
    </div>
    """, unsafe_allow_html=True)
