"""
내 상장 페이지
"""
import streamlit as st
from utils.ui_components import apply_custom_css, show_stars
from utils.gemini_client import check_api_key, get_ai_response

# 페이지 설정
st.set_page_config(
    page_title="내 상장",
    page_icon="🏆",
    layout="wide"
)

apply_custom_css()

# 제목
st.markdown("<h1 style='text-align: center;'>🏆 내 상장</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px;'>오늘 모은 별을 확인해봐요! 😊</p>", 
            unsafe_allow_html=True)

# 별 개수
stars = st.session_state.get("stars", 0)

# 상장 표시
if stars > 0:
    # 별 표시
    show_stars(stars)
    
    # 상장 디자인
    st.markdown(f"""
    <div style="text-align: center; padding: 50px; background: linear-gradient(135deg, #FFD700, #FFA500); 
                border-radius: 30px; margin: 30px; border: 10px solid #FF6B6B;">
        <h1 style="font-size: 60px; margin: 20px;">🏆</h1>
        <h1 style="font-size: 48px; margin: 20px; color: #2D3436;">수고했어요!</h1>
        <h2 style="font-size: 36px; margin: 20px; color: #2D3436;">오늘 {stars}개의 별을 모았어요!</h2>
        <p style="font-size: 28px; margin: 20px; color: #2D3436;">정말 대단해요! 최고예요! 🌟</p>
    </div>
    """, unsafe_allow_html=True)
    
    # AI 칭찬 메시지
    if check_api_key():
        with st.spinner("하늬 선생님이 칭찬 메시지를 준비하고 있어요..."):
            praise_message = get_ai_response(
                f"학생이 오늘 {stars}개의 별을 모았어요. 칭찬 메시지를 짧고 친절하게 써주세요.",
                system_prompt="당신은 친절한 선생님이에요. 학생을 칭찬하는 짧고 따뜻한 메시지를 써주세요. 이모지를 많이 써주세요."
            )
        
        st.markdown(f"""
        <div style="background: #E8F5E9; padding: 30px; border-radius: 20px; margin: 20px;">
            <h3 style="color: #2D3436;">💬 하늬 선생님의 칭찬:</h3>
            <p style="font-size: 24px;">{praise_message}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background: #E8F5E9; padding: 30px; border-radius: 20px; margin: 20px;">
            <h3 style="color: #2D3436;">💬 칭찬:</h3>
            <p style="font-size: 24px;">오늘 {stars}개의 별을 모았어요! 정말 대단해요! 🌟 최고예요! 🎉</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 성취 레벨 표시
    if stars >= 10:
        level = "🌟 골드 스타"
        emoji = "🌟"
    elif stars >= 5:
        level = "⭐ 실버 스타"
        emoji = "⭐"
    else:
        level = "✨ 브론즈 스타"
        emoji = "✨"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 30px; background: #FFF3CD; border-radius: 20px; margin: 20px;">
        <h2 style="font-size: 36px;">{emoji} {level}</h2>
        <p style="font-size: 22px;">계속 열심히 하면 더 많은 별을 받을 수 있어요! 💪</p>
    </div>
    """, unsafe_allow_html=True)
    
else:
    # 별이 없을 때
    st.markdown("""
    <div style="text-align: center; padding: 50px; background: #FFF3CD; border-radius: 30px; margin: 30px;">
        <h1 style="font-size: 80px; margin: 20px;">⭐</h1>
        <h2 style="font-size: 36px; margin: 20px;">아직 별이 없어요</h2>
        <p style="font-size: 24px; margin: 20px;">학습을 시작하면 별을 받을 수 있어요! 😊</p>
        <p style="font-size: 22px; margin: 20px;">읽기, 쓰기, 숫자 학습을 해봐요! 💪</p>
    </div>
    """, unsafe_allow_html=True)

# 홈으로 돌아가기
st.markdown("---")
if st.button("🏠 홈으로 돌아가기", use_container_width=True, key="btn_home"):
    st.switch_page("app.py")

# 별 초기화 버튼 (선택사항 - 개발용)
if st.button("🔄 별 초기화 (테스트용)", use_container_width=True, key="btn_reset"):
    st.session_state.stars = 0
    st.rerun()
