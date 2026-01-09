"""
학습 게임 로직
"""
import streamlit as st
from utils.constants import READING_WORDS, MATH_PROBLEMS
import random


def init_session_state():
    """세션 상태 초기화"""
    if "stars" not in st.session_state:
        st.session_state.stars = 0
    
    if "reading_index" not in st.session_state:
        st.session_state.reading_index = 0
    
    if "math_index" not in st.session_state:
        st.session_state.math_index = 0
    
    if "completed_words" not in st.session_state:
        st.session_state.completed_words = []
    
    if "completed_math" not in st.session_state:
        st.session_state.completed_math = []


def add_star(count: int = 1):
    """별 추가"""
    if "stars" not in st.session_state:
        st.session_state.stars = 0
    st.session_state.stars += count


def get_current_reading_word():
    """현재 읽기 학습 단어 가져오기"""
    if st.session_state.reading_index >= len(READING_WORDS):
        # 모든 단어를 다 배웠으면 처음부터
        st.session_state.reading_index = 0
    
    return READING_WORDS[st.session_state.reading_index]


def next_reading_word():
    """다음 읽기 학습 단어로 이동"""
    st.session_state.reading_index = (st.session_state.reading_index + 1) % len(READING_WORDS)


def get_current_math_problem():
    """현재 숫자 학습 문제 가져오기"""
    if st.session_state.math_index >= len(MATH_PROBLEMS):
        # 모든 문제를 다 풀었으면 처음부터
        st.session_state.math_index = 0
    
    return MATH_PROBLEMS[st.session_state.math_index]


def next_math_problem():
    """다음 숫자 학습 문제로 이동"""
    st.session_state.math_index = (st.session_state.math_index + 1) % len(MATH_PROBLEMS)


def check_math_answer(problem: dict, answer: int) -> bool:
    """숫자 문제 정답 확인"""
    if problem["type"] == "count":
        return answer == problem["count"]
    elif problem["type"] == "add":
        return answer == (problem["a"] + problem["b"])
    elif problem["type"] == "subtract":
        return answer == (problem["a"] - problem["b"])
    return False


def get_math_correct_answer(problem: dict) -> int:
    """숫자 문제의 정답 가져오기"""
    if problem["type"] == "count":
        return problem["count"]
    elif problem["type"] == "add":
        return problem["a"] + problem["b"]
    elif problem["type"] == "subtract":
        return problem["a"] - problem["b"]
    return 0
