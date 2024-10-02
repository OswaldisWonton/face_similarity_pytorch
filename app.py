import streamlit as st
import cv2
import numpy as np
import random
from utils.face_utils import FaceComparison
from utils.video_display import video_display, get_video_list
from utils.music_playing import MusicPlayer

# Streamlit 界面
st.title("人脸识别与展示")

# 上传图像文件
uploaded_file = st.file_uploader("请上传您的图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 将上传的文件读取为 OpenCV 图像格式
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # 显示上传的图像
    st.image(frame, channels="BGR", caption="上传的图像", use_column_width=True)

    # 初始化人脸模型
    face_model = FaceComparison("cpu")

    # 开始人脸对比
    result = []
    face_model.comparison(frame, result)

    if result[0]:
        face_label = result[0]
        st.write(f"您的脸型被识别为：{face_label}")

        # 选择对应的视频和音乐文件
        video_dict = get_video_list("videos")
        video_path = random.choice(video_dict[face_label])
        music_path = f'music/{face_label}.mp3'

        # 播放视频
        st.video(video_path)

        # 播放音乐
        st.audio(music_path)

