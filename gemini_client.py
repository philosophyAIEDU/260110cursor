"""
Gemini API 클라이언트
"""
import google.generativeai as genai
import streamlit as st
from typing import Tuple
from utils.constants import TEACHER_PROMPT


def validate_api_key(api_key: str) -> Tuple[bool, str]:
    """API 키가 유효한지 테스트합니다. (성공 여부, 에러 메시지) 반환"""
    if not api_key or not api_key.strip():
        return False, "API 키가 비어있어요"
    
    # API 키 형식 간단 체크 (Gemini API 키는 보통 "AIza"로 시작)
    api_key_clean = api_key.strip()
    if not api_key_clean.startswith("AIza"):
        return False, "API 키 형식이 올바르지 않아요. 'AIza'로 시작해야 해요"
    
    try:
        genai.configure(api_key=api_key_clean)
        model = genai.GenerativeModel("gemini-3-flash-preview")
        # 간단한 테스트 호출
        response = model.generate_content("안녕")
        # 응답이 제대로 왔는지 확인
        if response and response.text:
            return True, ""
        else:
            return False, "API 응답을 받을 수 없어요"
    except Exception as e:
        error_msg = str(e)
        # 친절한 에러 메시지로 변환
        if "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
            return False, "API 키가 유효하지 않아요. 다시 확인해주세요"
        elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
            return False, "API 사용 한도를 초과했어요"
        elif "permission" in error_msg.lower() or "forbidden" in error_msg.lower():
            return False, "API 키 권한이 없어요"
        else:
            return False, f"연결 오류: {error_msg[:100]}"


def get_ai_response(user_message: str, system_prompt: str = None) -> str:
    """세션의 API 키를 사용해 응답을 받습니다."""
    
    # API 키 확인
    if "api_key" not in st.session_state or not st.session_state.api_key:
        return "🔑 API 키를 먼저 입력해주세요!"
    
    try:
        genai.configure(api_key=st.session_state.api_key)
        
        # 시스템 프롬프트 설정
        prompt = system_prompt if system_prompt else TEACHER_PROMPT
        
        model = genai.GenerativeModel(
            model_name="gemini-3-flash-preview",
            system_instruction=prompt
        )
        
        response = model.generate_content(user_message)
        return response.text
    except Exception as e:
        return f"앗, 잠깐 문제가 생겼어요! 😅 다시 해볼까요? ({str(e)[:50]})"


def check_api_key() -> bool:
    """API 키가 유효한지 확인합니다."""
    return "api_key" in st.session_state and st.session_state.api_key


def get_word_explanation(word: str, emoji: str) -> str:
    """단어에 대한 쉬운 설명을 AI로 받아옵니다."""
    prompt = f"'{word}'라는 단어를 초등학생이 이해하기 쉽게 2-3줄로 설명해주세요. 이모지 {emoji}를 사용하고, 아주 쉬운 말로 써주세요."
    return get_ai_response(prompt, system_prompt="당신은 친절한 선생님이에요. 아주 쉬운 말로 설명해주세요. 이모지를 많이 써주세요.")


def get_encouragement_message() -> str:
    """격려 메시지를 AI로 받아옵니다."""
    messages = [
        "괜찮아요! 다시 해볼까요? 💪",
        "좋아요! 조금만 더 해봐요! 🌟",
        "할 수 있어요! 화이팅! 👍",
        "다시 생각해볼까요? 😊"
    ]
    import random
    return random.choice(messages)


def get_celebration_message() -> str:
    """축하 메시지를 AI로 받아옵니다."""
    messages = [
        "🎉 정말 잘했어요! 최고예요!",
        "⭐ 대단해요! 멋져요!",
        "👍 훌륭해요! 잘했어요!",
        "🌟 완벽해요! 최고예요!"
    ]
    import random
    return random.choice(messages)
