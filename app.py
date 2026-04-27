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
    .main { background: #ffffff; color: #1a1a1a; }
    .stButton>button {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
        color: #ffffff; border: none; border-radius: 30px;
        padding: 15px 30px; font-weight: 800; width: 100%;
        transition: 0.4s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(0,114,255,0.4); }
    .glass-card {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 20px; padding: 25px; margin-bottom: 20px;
        color: #1a1a1a;
    }
    h1, h2, h3 { color: #0072ff !important; }
    .highlight-text { color: #0072ff; font-weight: 800; }
    .prompt-box {
        background: #f1f3f5; /* Light gray background */
        border: 2px solid #dee2e6;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px; 
        color: #1a1a1a !important; /* Dark text for readability */
        font-size: 1.2rem;
        line-height: 1.8;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        word-break: keep-all;
    }
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
                    {p}
                </div>
                """, unsafe_allow_html=True)

        with tab2:
            st.subheader("Numbered Video Prompts for Runway/Luma/Kling")
            for p in prompts['video_prompts']:
                st.markdown(f"""
                <div class="prompt-box">
                    {p}
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
