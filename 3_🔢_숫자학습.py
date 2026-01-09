"""
숫자 학습 페이지
"""
import streamlit as st
from utils.ui_components import apply_custom_css, require_api_key, celebration, encouragement
from utils.gemini_client import check_api_key
from utils.game_logic import (
    get_current_math_problem, 
    next_math_problem, 
    add_star,
    check_math_answer,
    get_math_correct_answer
)

# 페이지 설정
st.set_page_config(
    page_title="숫자 학습",
    page_icon="🔢",
    layout="wide"
)

apply_custom_css()

# API 키 확인
if not check_api_key():
    require_api_key()

# 제목
st.markdown("<h1 style='text-align: center;'>🔢 숫자 학습</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px;'>숫자를 세고 계산해봐요! 😊</p>", 
            unsafe_allow_html=True)

# 현재 문제 가져오기
problem = get_current_math_problem()

# 문제 표시
if problem["type"] == "count":
    # 세기 문제
    emoji = problem["emoji"]
    count = problem["count"]
    
    st.markdown(f"""
    <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #FFF9E6, #FFE66D); 
                border-radius: 30px; margin: 30px; border: 5px solid #FFB6C1;">
        <h2 style="font-size: 48px; margin: 20px;">{problem["question"]}</h2>
        <div style="font-size: 80px; margin: 30px;">
            {(emoji + " ") * count}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
elif problem["type"] == "add":
    # 덧셈 문제
    a = problem["a"]
    b = problem["b"]
    
    st.markdown(f"""
    <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #FFF9E6, #FFE66D); 
                border-radius: 30px; margin: 30px; border: 5px solid #FFB6C1;">
        <h2 style="font-size: 48px; margin: 20px;">{problem["question"]}</h2>
        <h1 style="font-size: 72px; margin: 30px;">
            {a} + {b} = ?
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
elif problem["type"] == "subtract":
    # 뺄셈 문제
    a = problem["a"]
    b = problem["b"]
    
    st.markdown(f"""
    <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #FFF9E6, #FFE66D); 
                border-radius: 30px; margin: 30px; border: 5px solid #FFB6C1;">
        <h2 style="font-size: 48px; margin: 20px;">{problem["question"]}</h2>
        <h1 style="font-size: 72px; margin: 30px;">
            {a} - {b} = ?
        </h1>
    </div>
    """, unsafe_allow_html=True)

# 답 입력
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>정답을 입력해봐요! 😊</h3>", 
            unsafe_allow_html=True)

# 숫자 버튼으로 답 선택
col1, col2, col3, col4, col5 = st.columns(5)

answer_options = [1, 2, 3, 4, 5]
if problem["type"] == "count":
    answer_options = list(range(1, 8))
elif problem["type"] in ["add", "subtract"]:
    correct = get_math_correct_answer(problem)
    # 정답 주변 숫자들 포함
    answer_options = list(range(max(1, correct - 2), correct + 3))

# 정답 확인
if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None

for i, num in enumerate(answer_options[:5]):
    with [col1, col2, col3, col4, col5][i]:
        if st.button(f"{num}", use_container_width=True, key=f"btn_{num}"):
            st.session_state.selected_answer = num
            if check_math_answer(problem, num):
                celebration()
                add_star(1)
                next_math_problem()
                st.session_state.selected_answer = None
                st.rerun()
            else:
                encouragement()
                correct_answer = get_math_correct_answer(problem)
                st.markdown(f"""
                <div style="text-align: center; padding: 20px; background: #FFF3CD; border-radius: 15px; margin: 20px;">
                    <p style="font-size: 22px;">정답은 <strong>{correct_answer}</strong>예요! 다시 해볼까요? 💪</p>
                </div>
                """, unsafe_allow_html=True)

# 더 많은 숫자 버튼 (필요한 경우)
if len(answer_options) > 5:
    col6, col7, col8, col9, col10 = st.columns(5)
    for i, num in enumerate(answer_options[5:10]):
        with [col6, col7, col8, col9, col10][i]:
            if st.button(f"{num}", use_container_width=True, key=f"btn_{num}"):
                st.session_state.selected_answer = num
                if check_math_answer(problem, num):
                    celebration()
                    add_star(1)
                    next_math_problem()
                    st.session_state.selected_answer = None
                    st.rerun()
                else:
                    encouragement()
                    correct_answer = get_math_correct_answer(problem)
                    st.markdown(f"""
                    <div style="text-align: center; padding: 20px; background: #FFF3CD; border-radius: 15px; margin: 20px;">
                        <p style="font-size: 22px;">정답은 <strong>{correct_answer}</strong>예요! 다시 해볼까요? 💪</p>
                    </div>
                    """, unsafe_allow_html=True)

# 다음 문제 버튼
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("➡️ 다음 문제", use_container_width=True, key="btn_next"):
        st.session_state.selected_answer = None
        next_math_problem()
        st.rerun()

with col2:
    if st.button("🔄 다시 풀기", use_container_width=True, key="btn_retry"):
        st.session_state.selected_answer = None
        st.rerun()

# 홈으로 돌아가기
st.markdown("---")
if st.button("🏠 홈으로 돌아가기", use_container_width=True, key="btn_home"):
    st.switch_page("app.py")
