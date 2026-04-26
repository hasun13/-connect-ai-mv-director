# app.py - Connect AI Collaboration Ver.
import streamlit as st
import importlib
import lyric_analyzer
import prompt_generator
import time

# 모듈 강제 리로드 (캐시 문제 해결)
importlib.reload(lyric_analyzer)
importlib.reload(prompt_generator)

from lyric_analyzer import analyze_lyrics
from prompt_generator import generate_prompts

# --- Page Config ---
st.set_page_config(
    page_title="Connect AI | Global MV Director Pro",
    page_icon="🎬",
    layout="wide"
)

# --- Premium CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
    .main { background: #050505; color: #ffffff; }
    .stButton>button {
        background: linear-gradient(90deg, #00C9FF, #92FE9D);
        color: #000; border: none; border-radius: 30px;
        padding: 15px 30px; font-weight: 800; width: 100%;
        transition: 0.4s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px #92FE9D; }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px; padding: 25px; margin-bottom: 20px;
    }
    h1, h2, h3 { color: #92FE9D !important; }
    .highlight-text { color: #00C9FF; font-weight: 800; }
    .prompt-box {
        background: rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.9em;
    }
    .video-label { color: #FF0080; font-weight: 700; margin-bottom: 5px; display: block; }
    .image-label { color: #00C9FF; font-weight: 700; margin-bottom: 5px; display: block; }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Header
    st.title("🚀 Global Analog MV Director Pro")
    st.markdown("Connect AI Collaboration: **Image & Video Prompts (15+ List)**")
    
    st.divider()

    # Sidebar
    st.sidebar.title("🎬 Director's Menu")
    selected_style = st.sidebar.selectbox(
        "Aesthetic Style",
        ("Vintage Analog Film (70s/80s)", "Hyper-Realistic Sci-Fi", "Artistic Watercolor (Anime)", "Luxury Fashion Editorial")
    )
    selected_ratio = st.sidebar.radio("Aspect Ratio", ("16:9", "9:16", "21:9", "1:1"), index=0)
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"🎯 Strategy: 15+ Numbered Shots\nDistinguished Visuals & Motion")

    # Layout
    col_in, col_out = st.columns([1, 1])

    with col_in:
        st.subheader("🎤 Song Lyrics")
        lyrics = st.text_area("Input lyrics...", height=350, placeholder="가사를 입력하세요...")
        gen_btn = st.button("✨ START PRODUCTION")

    with col_out:
        st.subheader("📊 Lyrical Analysis")
        if gen_btn and lyrics:
            with st.spinner("Analyzing themes and crafting prompts..."):
                analysis = analyze_lyrics(lyrics)
                time.sleep(1)
                prompts = generate_prompts(analysis, selected_style, selected_ratio)
            
            st.markdown(f"""
            <div class="glass-card">
                <p><b>🎭 Mood:</b> <span class="highlight-text">{analysis['mood']}</span></p>
                <p><b>🌍 Theme:</b> {analysis['theme']}</p>
                <p><b>📍 Setting:</b> {analysis['setting']}</p>
                <p><b>📊 Total Shots:</b> {prompts['total_count']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.success(f"Production of {prompts['total_count']} shots complete!")

    # Results
    if gen_btn and lyrics:
        st.divider()
        tab1, tab2 = st.tabs(["🖼️ Image Prompts (Visuals)", "🎥 Video Prompts (Motion)"])
        
        with tab1:
            st.subheader("Numbered Image Prompts for Midjourney/Flux")
            for p in prompts['image_prompts']:
                st.markdown(f"""
                <div class="prompt-box">
                    <span class="image-label">IMAGE PROMPT</span>
                    {p}
                </div>
                """, unsafe_allow_html=True)

        with tab2:
            st.subheader("Numbered Video Prompts for Runway/Luma/Kling")
            for p in prompts['video_prompts']:
                st.markdown(f"""
                <div class="prompt-box">
                    <span class="video-label">VIDEO PROMPT</span>
                    {p}
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
