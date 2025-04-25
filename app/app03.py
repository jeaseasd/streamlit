import streamlit as st
import numpy as np
from PIL import Image

st.title('미디어 요소 활용하기 🖼️')

# 이미지 표시
st.header('이미지 표시')

# 로컬 이미지 또는 URL로 이미지 표시
st.subheader('방법 1: 이미지 파일 또는 URL')
st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', 
        caption='Streamlit 로고',
        width=300)

# 이미지 생성 후 표시
st.subheader('방법 2: 이미지 생성')
img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
st.image(img_array, caption='무작위 생성 이미지', width=300)

# 비디오 표시
st.header('비디오 표시')
video_file = open('sample_video.mp4', 'rb')  # 샘플 비디오 파일
video_bytes = video_file.read()
st.video(video_bytes)

# 오디오 표시
st.header('오디오 표시')
audio_file = open('sample_audio.mp3', 'rb')  # 샘플 오디오 파일
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')