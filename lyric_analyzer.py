# lyric_analyzer.py - 고도화된 가사 분석 모듈 (Thematic Analysis)
import re

def analyze_lyrics(lyrics: str):
    """
    가사를 심층 분석하여 분위기, 테마, 시대적 배경, 핵심 키워드를 추출합니다.
    """
    clean_lyrics = re.sub(r'[^\w\s]', '', lyrics)
    words = clean_lyrics.split()
    
    # 1. 심층 감성/분위기 분석
    mood_map = {
        "Nostalgic & Warm (아날로그 감성)": ["추억", "기억", "옛날", "사진", "편지", "노을", "어린시절"],
        "Digital Melancholy (디지털 고독)": ["wifi", "connection", "signal", "loading", "buffer", "lag", "screen", "online", "heart"],
        "Cyberpunk & Intense (강렬한 도심)": ["도시", "네온", "빌딩", "차갑다", "데이터", "사이버", "거울"],
        "Melancholic & Deep (애틋한 고독)": ["이별", "눈물", "빗물", "바다", "그림자", "혼자", "침묵"],
        "Dreamy & Ethereal (몽환적 판타지)": ["우주", "별", "안개", "구름", "꿈", "신비", "천사"]
    }
    
    mood_scores = {mood: 0 for mood in mood_map}
    for word in words:
        for mood, keys in mood_map.items():
            if word in keys: mood_scores[mood] += 2 # 키워드 가중치
                
    mood = max(mood_scores, key=mood_scores.get) if any(mood_scores.values()) else "Nostalgic & Warm (아날로그 감성)"

    # 2. 글로벌 시장 겨냥 테마 추출
    theme = "Human Emotion"
    if "사랑" in lyrics or "연인" in lyrics: theme = "Eternal Love"
    elif "성공" in lyrics or "꿈" in lyrics: theme = "Ambition & Growth"
    elif "슬픔" in lyrics or "아픔" in lyrics: theme = "Healing & Resilience"
    elif any(word in lyrics for word in ["우주", "지구", "세계"]): theme = "Cosmic Connection"

    # 3. 비주얼 배경 (Global Appeal)
    setting = "Cinematic Landscape"
    if "Retro" in mood or "Nostalgic" in mood:
        setting = "1980s Vintage Seoul/Tokyo streets"
    elif "Cyber" in mood:
        setting = "Neo-Seoul High-tech District"
    elif "Dreamy" in mood:
        setting = "Floating islands in a nebula sky"
    else:
        setting = "Modern Minimalist Architecture"

    # 4. 키워드 및 플롯 (100만 조회수 연출용)
    keywords = [w for w in words if len(w) > 1][:7]
    
    # 조회수를 부르는 '하이라이트' 연출 포인트
    if theme == "Eternal Love":
        plot_points = ["슬로우 모션으로 교차하는 시선", "빛바랜 사진 속의 웃음", "비 내리는 거리에서의 포옹"]
    elif theme == "Ambition & Growth":
        plot_points = ["거친 파도를 헤치며 나아가는 배", "도시의 높은 곳에서 내려다보는 야경", "태양을 향해 뻗은 손"]
    else:
        plot_points = ["거울 속에 비친 낯선 자아", "끝없이 펼쳐진 사막의 고독", "어둠을 가르는 한 줄기 빛"]

    return {
        "mood": mood,
        "theme": theme,
        "setting": setting,
        "keywords": list(set(keywords)),
        "plot_points": plot_points
    }
