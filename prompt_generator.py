# prompt_generator.py - Connect AI Collaboration Ver. (15+ Shots)
import random

def generate_prompts(analysis: dict, style: str, ratio: str = "16:9"):
    """
    Connect AI 지침 반영: 이미지 프롬프트와 영상 프롬프트를 분리하여 총 15개 이상의 번호 나열형 프롬프트를 생성합니다.
    """
    
    style_guides = {
        "Vintage Analog Film (70s/80s)": "Shot on 35mm film, Kodak Portra 400, heavy film grain, light leaks, vintage retro aesthetic.",
        "Hyper-Realistic Sci-Fi": "Unreal Engine 5 render, cinematic lighting, 8k, volumetric fog, futuristic cyberpunk mood.",
        "Artistic Watercolor (Anime)": "Makoto Shinkai style, breathtaking sky, emotional lighting, soft cel shading.",
        "Luxury Fashion Editorial": "Vogue aesthetic, high-end fashion photography, minimalist composition, elegant lighting."
    }
    
    style_prompt = style_guides.get(style, "Cinematic 8k resolution, masterpiece.")
    neg_prompt = " --no text, words, watermark, logos, subtitles, signatures, low quality, blurry"
    aspect_ratio = f" --ar {ratio}"

    plot = analysis['plot_points']
    
    # 샷 유형 정의
    shot_types = [
        {"name": "Wide Shot", "desc": "Extreme wide angle establishing shot, grand scale, epic environment", "motion": "Slow majestic drone sweep, revealing the scale of the environment."},
        {"name": "Group/Medium Shot", "desc": "Medium shot showing subjects in context, cinematic composition", "motion": "Dolly in slowly towards the subjects, focusing on the atmosphere."},
        {"name": "Close-up", "desc": "Intense close-up focusing on emotional expression and fine details", "motion": "Subtle handheld micro-movements, focusing on eye reflections and depth."},
        {"name": "POV/Handheld", "desc": "First-person perspective or raw handheld camera feel, immersive", "motion": "Natural walking motion, shaky cam for realism, looking around the scene."},
        {"name": "Action/Dynamic", "desc": "High-speed motion blur, dynamic angle, capturing peak energy", "motion": "Fast tracking shot, following the subject with dynamic motion blur."}
    ]
    
    final_image_prompts = []
    final_video_prompts = []
    
    prompt_count = 1
    for i in range(len(plot)):
        step = plot[i]
        keyword = analysis['keywords'][i] if i < len(analysis['keywords']) else analysis['theme']
        
        for shot in shot_types:
            # 1. 이미지 프롬프트 (Visual focus)
            img_base = f"A cinematic {shot['desc']}, depicting {analysis['setting']}, themed '{analysis['theme']}', {analysis['mood']} mood, centered on {keyword}. {style_prompt}"
            img_full = f"{prompt_count}. {img_base}{aspect_ratio}{neg_prompt}"
            final_image_prompts.append(img_full)
            
            # 2. 영상 프롬프트 (Motion focus)
            vid_base = f"{shot['motion']} The scene shows {step} in {analysis['setting']}. {analysis['mood']} atmosphere, high quality video, fluid motion, cinematic lighting."
            vid_full = f"{prompt_count}. {vid_base}"
            final_video_prompts.append(vid_full)
            
            prompt_count += 1

    return {
        "image_prompts": final_image_prompts,
        "video_prompts": final_video_prompts,
        "total_count": prompt_count - 1
    }
