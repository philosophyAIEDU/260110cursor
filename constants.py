"""
상수 및 프롬프트 정의
"""

TEACHER_PROMPT = """당신은 '하늬 선생님'이에요. 지적장애 학생을 가르치는 친절한 선생님이에요.

🌟 말하는 방법:
- 아주 짧고 쉬운 문장만 써요 (10글자 정도)
- 어려운 말은 쉬운 말로 바꿔요
- 항상 칭찬해요 ("잘했어!", "대단해!", "멋져!")
- 이모지를 많이 써요 😊👍🎉⭐
- 한 번에 한 가지만 이야기해요
- 틀려도 "괜찮아요!"라고 말해요
- 질문은 "네/아니오"로 대답할 수 있게 해요

🎯 대화 예시:
학생: 안녕
하늬: 안녕! 😊 반가워요! 오늘 기분이 좋아요? 👍

학생: 사과가 뭐야
하늬: 사과는 빨간 과일이에요! 🍎 맛있어요! 먹어본 적 있어요?

학생: 1+1은?
하늬: 1+1은 2예요! 👍 정말 잘했어요! 🎉"""

# 학습 단어 리스트
READING_WORDS = [
    {"word": "사과", "emoji": "🍎", "description": "빨간 과일이에요"},
    {"word": "강아지", "emoji": "🐶", "description": "귀여운 동물이에요"},
    {"word": "책", "emoji": "📚", "description": "읽는 것이에요"},
    {"word": "나무", "emoji": "🌳", "description": "큰 식물이에요"},
    {"word": "별", "emoji": "⭐", "description": "밤하늘에 빛나요"},
    {"word": "해", "emoji": "☀️", "description": "하늘에 떠있어요"},
    {"word": "물", "emoji": "💧", "description": "마시는 것이에요"},
    {"word": "꽃", "emoji": "🌸", "description": "예쁜 것이에요"},
]

# 숫자 학습 문제
MATH_PROBLEMS = [
    {"type": "count", "emoji": "🍎", "count": 3, "question": "사과가 몇 개예요?"},
    {"type": "count", "emoji": "🐶", "count": 5, "question": "강아지가 몇 마리예요?"},
    {"type": "add", "a": 2, "b": 3, "question": "2 + 3은 얼마예요?"},
    {"type": "add", "a": 1, "b": 4, "question": "1 + 4는 얼마예요?"},
    {"type": "subtract", "a": 5, "b": 2, "question": "5 - 2는 얼마예요?"},
    {"type": "subtract", "a": 4, "b": 1, "question": "4 - 1은 얼마예요?"},
]
